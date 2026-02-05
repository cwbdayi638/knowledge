# Testing Guide for Seismic Waveform Fetching

## Overview

This guide covers testing procedures for the seismic waveform fetching system.

## Prerequisites

Before running tests, ensure dependencies are installed:

```bash
pip install obspy matplotlib numpy
```

## Running Unit Tests

### Quick Test Run

Run all unit tests with verbose output:

```bash
cd scripts
python3 test_fetch_seismic_waveforms.py
```

### Test Coverage

The test suite includes 16 comprehensive tests covering:

#### 1. Waveform Data Validation (4 tests)
- `test_validate_none_data`: Validates handling of None input
- `test_validate_empty_stream`: Validates empty data stream handling
- `test_validate_valid_stream`: Validates correct data acceptance
- `test_validate_insufficient_data_points`: Validates minimum data requirements

#### 2. FDSN Client Connection (3 tests)
- `test_get_fdsn_client_success_first_try`: Tests immediate successful connection
- `test_get_fdsn_client_retry_logic`: Tests retry mechanism with exponential backoff
- `test_get_fdsn_client_all_fail`: Tests graceful failure when all providers are down

#### 3. Waveform Fetching (2 tests)
- `test_fetch_waveforms_success`: Tests successful data retrieval
- `test_fetch_waveforms_failure`: Tests error handling during fetch

#### 4. Plotting Functionality (5 tests)
- `test_plot_waveforms_single_trace`: Tests single trace plotting
- `test_plot_waveforms_multiple_traces`: Tests multi-trace plotting
- `test_plot_waveforms_none_data`: Tests None data handling
- `test_plot_waveforms_empty_stream`: Tests empty stream handling
- `test_generate_demo_plot`: Tests demo data generation

#### 5. Main Function Integration (2 tests)
- `test_main_success_with_real_data`: Tests complete workflow with real data
- `test_main_fallback_to_demo`: Tests fallback to demo data

## Manual Testing

### Test Script Execution

Run the script manually to test real-world behavior:

```bash
cd /home/runner/work/knowledge/knowledge
python3 scripts/fetch_seismic_waveforms.py
```

Expected output:
- Connection attempts to multiple FDSN providers
- Retry logic with exponential backoff
- Either real waveform data or demo data generation
- PNG plot saved to `seismic_waveforms/` directory

### Test Generated Plots

Check the generated plots:

```bash
ls -lh seismic_waveforms/*.png
```

View the latest plot to verify:
- Three-component waveforms (if real data)
- Proper labeling and timestamps
- Clear visualization

### Test Different Scenarios

1. **Normal Operation** (FDSN services available):
   - Script should connect and fetch real data
   - Validation should pass
   - Plots should show actual seismic waveforms

2. **Service Unavailable** (FDSN services down):
   - Script should retry with exponential backoff
   - Should try multiple providers
   - Should fallback to demo data gracefully
   - Plots should be marked as "DEMO DATA"

3. **Network Timeout**:
   - Script should respect 30-second timeout
   - Should retry failed connections
   - Should eventually fallback to demo data

## Testing Checklist

Before committing changes, verify:

- [ ] All 16 unit tests pass
- [ ] Script executes without errors
- [ ] PNG plots are generated correctly
- [ ] Error messages are informative
- [ ] Retry logic works as expected
- [ ] Demo data fallback functions properly
- [ ] Data validation catches invalid data
- [ ] Timeouts are respected

## Continuous Integration

The GitHub Actions workflow (`.github/workflows/seismic-waveforms.yml`) automatically:
1. Installs dependencies
2. Runs the fetch script
3. Commits generated plots

### Testing Workflow Locally

Simulate the CI workflow:

```bash
# Install dependencies
pip install obspy matplotlib numpy

# Run the script
python3 scripts/fetch_seismic_waveforms.py

# Check output
ls seismic_waveforms/waveform_*.png
```

## Troubleshooting

### Tests Fail to Import Module

```bash
# Ensure you're in the correct directory
cd /home/runner/work/knowledge/knowledge/scripts
python3 test_fetch_seismic_waveforms.py
```

### Dependencies Missing

```bash
pip install obspy matplotlib numpy
```

### No Plot Generated

Check the console output for error messages. The script should fallback to demo data if FDSN services are unavailable.

### All FDSN Providers Fail

This is expected behavior when services are temporarily down. The script will:
1. Try all configured providers
2. Retry with exponential backoff
3. Generate demo data as fallback
4. Exit successfully

## Test Improvements Made

### 1. Enhanced Error Handling
- Added retry logic with exponential backoff (1s, 2s delays)
- Multiple FDSN provider fallback (IRIS, USGS)
- Graceful degradation to demo data

### 2. Data Validation
- Added `validate_waveform_data()` function
- Checks for None, empty, or insufficient data
- Validates data quality when available

### 3. Improved Timeout Handling
- Configurable timeout (30 seconds)
- Applied to all FDSN connections
- Prevents hanging on slow networks

### 4. Better Service Provider Configuration
- Structured provider configuration
- Both named services and base URLs
- Easy to add new providers

### 5. Comprehensive Testing
- 16 unit tests covering all major functions
- Mock-based testing for reliability
- Integration tests for full workflow

## Success Criteria

✅ All tests pass  
✅ Script handles service unavailability gracefully  
✅ Retry logic works with exponential backoff  
✅ Data validation catches invalid inputs  
✅ Plots are generated correctly  
✅ Demo data fallback works  
✅ Error messages are informative  
✅ Code is well-documented  

---

*Last updated: 2026-02-05*
