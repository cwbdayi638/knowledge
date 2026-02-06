#!/usr/bin/env python3
"""
Unit tests for fetch_seismic_waveforms.py
Tests the waveform fetching and plotting functionality
"""

import os
import sys
import unittest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime
MISSING_DEPENDENCIES = []

try:
    import numpy as np
except ImportError:
    np = None
    MISSING_DEPENDENCIES.append('numpy')

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Mock matplotlib before importing the module
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib = None
    plt = None
    MISSING_DEPENDENCIES.append('matplotlib')

try:
    # Check if obspy is available for waveform tests.
    import obspy  # noqa: F401
except ImportError:
    MISSING_DEPENDENCIES.append('obspy')

SKIP_REASON = (
    "Missing dependencies: " + ", ".join(MISSING_DEPENDENCIES)
    if MISSING_DEPENDENCIES
    else None
)

# Import the module to test (when dependencies are available)
if SKIP_REASON is None:
    import fetch_seismic_waveforms as fws
else:
    fws = None

TEST_TRACE_SAMPLES = 6000  # 10 minutes at 10 Hz sample rate


@unittest.skipIf(SKIP_REASON, SKIP_REASON or "Missing dependencies")
class TestWaveformValidation(unittest.TestCase):
    """Test waveform data validation functions"""
    
    def test_validate_none_data(self):
        """Test validation with None data"""
        is_valid, message = fws.validate_waveform_data(None)
        self.assertFalse(is_valid)
        self.assertIn("No data stream", message)
    
    def test_validate_empty_stream(self):
        """Test validation with empty stream"""
        from obspy import Stream
        st = Stream()
        is_valid, message = fws.validate_waveform_data(st)
        self.assertFalse(is_valid)
        self.assertIn("Empty data stream", message)
    
    def test_validate_valid_stream(self):
        """Test validation with valid stream"""
        from obspy import Stream, Trace
        import numpy as np
        
        # Create a valid trace
        tr = Trace(data=np.random.randn(1000))
        tr.stats.station = 'NACB'
        tr.stats.channel = 'BHZ'
        
        st = Stream([tr])
        is_valid, message = fws.validate_waveform_data(st)
        self.assertTrue(is_valid)
        self.assertIn("valid", message.lower())
    
    def test_validate_insufficient_data_points(self):
        """Test validation with too few data points"""
        from obspy import Stream, Trace
        import numpy as np
        
        # Create a trace with insufficient data
        tr = Trace(data=np.random.randn(5))
        tr.stats.station = 'NACB'
        tr.stats.channel = 'BHZ'
        
        st = Stream([tr])
        is_valid, message = fws.validate_waveform_data(st)
        self.assertFalse(is_valid)
        self.assertIn("too few data points", message)


@unittest.skipIf(SKIP_REASON, SKIP_REASON or "Missing dependencies")
class TestClientConnection(unittest.TestCase):
    """Test FDSN client connection functionality"""
    
    @patch('fetch_seismic_waveforms.Client')
    @patch('fetch_seismic_waveforms.time.sleep')
    def test_get_fdsn_client_success_first_try(self, mock_sleep, mock_client_class):
        """Test successful connection on first attempt"""
        mock_client = MagicMock()
        mock_client.get_stations.return_value = Mock()
        mock_client_class.return_value = mock_client
        
        client = fws.get_fdsn_client()
        
        self.assertIsNotNone(client)
        self.assertEqual(mock_client_class.call_count, 1)
        mock_sleep.assert_not_called()
    
    @patch('fetch_seismic_waveforms.Client')
    @patch('fetch_seismic_waveforms.time.sleep')
    def test_get_fdsn_client_retry_logic(self, mock_sleep, mock_client_class):
        """Test retry logic with exponential backoff"""
        # First attempt fails, second succeeds
        mock_client = MagicMock()
        mock_client.get_stations.return_value = Mock()
        mock_client_class.side_effect = [
            Exception("Connection failed"),
            mock_client
        ]
        
        client = fws.get_fdsn_client()
        
        self.assertIsNotNone(client)
        # Should have tried at least twice
        self.assertGreaterEqual(mock_client_class.call_count, 2)
        # Sleep should be called for retry
        mock_sleep.assert_called()
    
    @patch('fetch_seismic_waveforms.Client')
    @patch('fetch_seismic_waveforms.time.sleep')
    def test_get_fdsn_client_all_fail(self, mock_sleep, mock_client_class):
        """Test when all providers fail"""
        mock_client_class.side_effect = Exception("Connection failed")
        
        client = fws.get_fdsn_client()
        
        self.assertIsNone(client)


@unittest.skipIf(SKIP_REASON, SKIP_REASON or "Missing dependencies")
class TestWaveformFetching(unittest.TestCase):
    """Test waveform fetching functionality"""
    
    @patch('fetch_seismic_waveforms.UTCDateTime')
    def test_fetch_waveforms_success(self, mock_utc):
        """Test successful waveform fetching"""
        from obspy import Stream, Trace, UTCDateTime
        import numpy as np
        
        # Use real UTCDateTime
        mock_utc.return_value = UTCDateTime()
        
        # Create mock client
        mock_client = MagicMock()
        
        # Create mock stream
        tr = Trace(data=np.random.randn(TEST_TRACE_SAMPLES))
        tr.stats.station = 'NACB'
        tr.stats.channel = 'BHZ'
        tr.stats.npts = TEST_TRACE_SAMPLES
        st = Stream([tr])
        
        mock_client.get_waveforms.return_value = st
        
        result = fws.fetch_waveforms(mock_client)
        
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        mock_client.get_waveforms.assert_called_once()
    
    def test_fetch_waveforms_failure(self):
        """Test waveform fetching failure"""
        mock_client = MagicMock()
        mock_client.get_waveforms.side_effect = Exception("Network error")
        mock_client.get_stations.side_effect = Exception("Station not found")
        
        result = fws.fetch_waveforms(mock_client)
        
        self.assertIsNone(result)


@unittest.skipIf(SKIP_REASON, SKIP_REASON or "Missing dependencies")
class TestPlotting(unittest.TestCase):
    """Test plotting functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_output_dir = '/tmp/test_waveforms'
        os.makedirs(self.test_output_dir, exist_ok=True)
    
    def tearDown(self):
        """Clean up test files"""
        import shutil
        if os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)
    
    def test_plot_waveforms_single_trace(self):
        """Test plotting with a single trace"""
        from obspy import Stream, Trace
        import numpy as np
        
        tr = Trace(data=np.random.randn(TEST_TRACE_SAMPLES))
        tr.stats.station = 'NACB'
        tr.stats.channel = 'BHZ'
        st = Stream([tr])
        
        filename = os.path.join(self.test_output_dir, 'test_single.png')
        result = fws.plot_waveforms(st, filename)
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(filename))
        self.assertGreater(os.path.getsize(filename), 0)
    
    def test_plot_waveforms_multiple_traces(self):
        """Test plotting with multiple traces"""
        from obspy import Stream, Trace
        import numpy as np
        
        channels = ['BHZ', 'BHN', 'BHE']
        traces = []
        for channel in channels:
            tr = Trace(data=np.random.randn(TEST_TRACE_SAMPLES))
            tr.stats.station = 'NACB'
            tr.stats.channel = channel
            traces.append(tr)
        
        st = Stream(traces)
        filename = os.path.join(self.test_output_dir, 'test_multiple.png')
        result = fws.plot_waveforms(st, filename)
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(filename))

    def test_plot_waveforms_station_label(self):
        """Test station label selection in plot title"""
        from obspy import Stream, Trace
        import numpy as np

        tr = Trace(data=np.random.randn(TEST_TRACE_SAMPLES))
        tr.stats.station = 'TEST'
        tr.stats.channel = 'BHZ'
        st = Stream([tr])

        filename = os.path.join(self.test_output_dir, 'test_station_label.png')
        fig, ax = plt.subplots(1, 1, figsize=(12, 3))
        with patch('fetch_seismic_waveforms.plt.subplots', return_value=(fig, ax)), \
             patch('fetch_seismic_waveforms.plt.close'):
            result = fws.plot_waveforms(st, filename)

        self.assertTrue(result)
        self.assertIn('Station TEST', fig._suptitle.get_text())
        plt.close(fig)

    def test_plot_waveforms_none_data(self):
        """Test plotting with None data"""
        filename = os.path.join(self.test_output_dir, 'test_none.png')
        result = fws.plot_waveforms(None, filename)
        
        self.assertFalse(result)
        self.assertFalse(os.path.exists(filename))
    
    def test_plot_waveforms_empty_stream(self):
        """Test plotting with empty stream"""
        from obspy import Stream
        
        st = Stream()
        filename = os.path.join(self.test_output_dir, 'test_empty.png')
        result = fws.plot_waveforms(st, filename)
        
        self.assertFalse(result)
    
    def test_generate_demo_plot(self):
        """Test example plot generation"""
        filename = os.path.join(self.test_output_dir, 'test_demo.png')
        result = fws.generate_demo_plot(filename)
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(filename))
        self.assertGreater(os.path.getsize(filename), 0)

    @patch('fetch_seismic_waveforms.read')
    @patch('fetch_seismic_waveforms.plot_waveforms')
    def test_generate_demo_plot_uses_example_data(self, mock_plot, mock_read):
        """Test that example data is used when available"""
        from obspy import Stream, Trace
        import numpy as np

        st = Stream([Trace(data=np.random.randn(10))])
        mock_read.return_value = st
        mock_plot.return_value = True

        filename = os.path.join(self.test_output_dir, 'test_example.png')
        result = fws.generate_demo_plot(filename)

        self.assertTrue(result)
        mock_read.assert_called_once()
        mock_plot.assert_called_once_with(st, filename, title_suffix=' [EXAMPLE DATA]')


@unittest.skipIf(SKIP_REASON, SKIP_REASON or "Missing dependencies")
class TestMainFunction(unittest.TestCase):
    """Test main execution function"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_output_dir = '/tmp/test_waveforms_main'
        self.original_output_dir = fws.OUTPUT_DIR
        fws.OUTPUT_DIR = self.test_output_dir
        os.makedirs(self.test_output_dir, exist_ok=True)
    
    def tearDown(self):
        """Clean up test files"""
        import shutil
        fws.OUTPUT_DIR = self.original_output_dir
        if os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)
    
    @patch('fetch_seismic_waveforms.get_fdsn_client')
    @patch('fetch_seismic_waveforms.fetch_waveforms')
    @patch('fetch_seismic_waveforms.plot_waveforms')
    def test_main_success_with_real_data(self, mock_plot, mock_fetch, mock_get_client):
        """Test main function with successful data fetch"""
        from obspy import Stream, Trace
        import numpy as np
        
        # Setup mocks
        mock_client = Mock()
        mock_get_client.return_value = mock_client
        
        tr = Trace(data=np.random.randn(TEST_TRACE_SAMPLES))
        tr.stats.station = 'NACB'
        st = Stream([tr])
        mock_fetch.return_value = st
        mock_plot.return_value = True
        
        result = fws.main()
        
        self.assertEqual(result, 0)
        mock_get_client.assert_called_once()
        mock_fetch.assert_called_once_with(mock_client)
        mock_plot.assert_called_once()
    
    @patch('fetch_seismic_waveforms.get_fdsn_client')
    @patch('fetch_seismic_waveforms.generate_demo_plot')
    def test_main_fallback_to_demo(self, mock_demo, mock_get_client):
        """Test main function fallback to example data"""
        mock_get_client.return_value = None
        mock_demo.return_value = True
        
        result = fws.main()
        
        self.assertEqual(result, 0)
        mock_demo.assert_called_once()


def run_tests():
    """Run all tests and return results"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(run_tests())
