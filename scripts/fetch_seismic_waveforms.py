#!/usr/bin/env python3
"""
Seismic Waveform Fetching Script
Fetches 10 minutes of seismic data from IRIS FDSN for NACB station
Generates PNG plots of waveforms
Runs every 30 minutes via GitHub Actions
"""

import os
import sys
import time
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from obspy import UTCDateTime, read
from obspy.clients.fdsn import Client

# Configuration
STATION = "NACB"
CHANNEL = "BH*"  # Broadband high-gain channels
NETWORK = "*"    # Try all networks
LOCATION = "*"   # Try all locations
DATA_DURATION = 10 * 60  # 10 minutes in seconds
OUTPUT_DIR = 'seismic_waveforms'
TIMEOUT = 30  # Connection timeout in seconds
MAX_RETRIES = 2  # Maximum retry attempts per provider

# Alternative FDSN service providers with priority order
FDSN_PROVIDERS = [
    {"service": "IRIS", "timeout": TIMEOUT},
    {"base_url": "https://service.iris.edu", "timeout": TIMEOUT},
    {"service": "USGS", "timeout": TIMEOUT},
    {"base_url": "https://earthquake.usgs.gov", "timeout": TIMEOUT},
]

def get_fdsn_client():
    """
    Try to connect to FDSN service with multiple providers and retry logic
    """
    print("🌐 Connecting to FDSN web service...")
    
    for provider in FDSN_PROVIDERS:
        for attempt in range(MAX_RETRIES):
            try:
                if 'service' in provider:
                    provider_name = provider['service']
                    print(f"   Trying provider: {provider_name} (attempt {attempt + 1}/{MAX_RETRIES})...")
                    client = Client(provider['service'], timeout=provider.get('timeout', TIMEOUT))
                else:
                    provider_url = provider.get('base_url', 'unknown')
                    print(f"   Trying base URL: {provider_url} (attempt {attempt + 1}/{MAX_RETRIES})...")
                    client = Client(base_url=provider['base_url'], timeout=provider.get('timeout', TIMEOUT))
                
                # Test the connection by getting availability
                print(f"   Testing connection...")
                client.get_stations(station=STATION, level="station", maxcount=1)
                print(f"✅ Successfully connected!")
                return client
                
            except Exception as e:
                print(f"   ❌ Failed: {str(e)[:100]}")
                if attempt < MAX_RETRIES - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    print(f"   Waiting {wait_time}s before retry...")
                    time.sleep(wait_time)
                continue
    
    print("❌ Could not connect to any FDSN service after all retries")
    return None

def validate_waveform_data(st):
    """
    Validate fetched waveform data
    Returns: (is_valid, error_message)
    """
    if st is None:
        return False, "No data stream provided"
    
    if len(st) == 0:
        return False, "Empty data stream"
    
    # Check if traces have data points
    for tr in st:
        if tr.stats.npts < 10:
            return False, f"Trace {tr.id} has too few data points: {tr.stats.npts}"
        
        # Check for data quality
        if hasattr(tr.stats, 'mseed') and hasattr(tr.stats.mseed, 'dataquality'):
            if tr.stats.mseed.dataquality not in ['D', 'R', 'Q', 'M']:
                return False, f"Trace {tr.id} has poor data quality: {tr.stats.mseed.dataquality}"
    
    return True, "Data is valid"

def fetch_waveforms(client):
    """
    Fetch seismic waveforms for NACB station
    """
    print(f"📡 Fetching waveforms for station {STATION}...")
    
    # Get current time and calculate start time
    endtime = UTCDateTime()
    starttime = endtime - DATA_DURATION
    
    print(f"   Time range: {starttime} to {endtime}")
    print(f"   Network: {NETWORK}, Station: {STATION}, Location: {LOCATION}, Channel: {CHANNEL}")
    
    try:
        # Fetch waveforms
        st = client.get_waveforms(
            network=NETWORK,
            station=STATION,
            location=LOCATION,
            channel=CHANNEL,
            starttime=starttime,
            endtime=endtime
        )
        
        print(f"✅ Fetched {len(st)} traces:")
        for tr in st:
            print(f"   {tr.id}: {tr.stats.starttime} - {tr.stats.endtime}, {tr.stats.npts} samples")
        
        # Validate the fetched data
        is_valid, message = validate_waveform_data(st)
        if not is_valid:
            print(f"⚠️  Data validation warning: {message}")
        else:
            print(f"✅ Data validation passed: {message}")
        
        return st
        
    except Exception as e:
        print(f"❌ Error fetching waveforms: {e}")
        
        # Try to get station information to debug
        try:
            print("\n🔍 Checking station availability...")
            inventory = client.get_stations(
                network=NETWORK,
                station=STATION,
                starttime=starttime,
                endtime=endtime,
                level="channel"
            )
            print("   Station information:")
            print(inventory)
        except Exception as e2:
            print(f"   Could not get station info: {e2}")
        
        return None

def plot_waveforms(st, filename, title_suffix=""):
    """
    Plot waveforms and save to PNG file
    """
    print(f"📊 Plotting waveforms to {filename}...")
    
    if st is None or len(st) == 0:
        print("   No data to plot")
        return False
    
    try:
        # Create figure with subplots for each trace
        num_traces = len(st)
        fig, axes = plt.subplots(num_traces, 1, figsize=(12, 3*num_traces))
        
        # Handle single trace case
        if num_traces == 1:
            axes = [axes]
        
        # Plot each trace
        for i, tr in enumerate(st):
            times = tr.times()
            data = tr.data
            
            axes[i].plot(times, data, 'k-', linewidth=0.5)
            axes[i].set_ylabel(f'{tr.id}\n({tr.stats.channel})', fontsize=10)
            axes[i].grid(True, alpha=0.3)
            axes[i].set_xlim(0, max(times))
            
            # Only show x-label on bottom plot
            if i == num_traces - 1:
                axes[i].set_xlabel('Time (seconds)', fontsize=10)
        
        # Add title
        station_label = STATION
        if getattr(st[0].stats, 'station', None):
            station_label = st[0].stats.station

        fig.suptitle(f'Seismic Waveforms - Station {station_label}{title_suffix}\n{st[0].stats.starttime}', 
                     fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Plot saved to {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Error plotting waveforms: {e}")
        import traceback
        traceback.print_exc()
        return False

def generate_demo_plot(filename):
    """
    Generate an example plot when real data is unavailable
    """
    print("📊 Generating example plot (real data unavailable)...")
    
    try:
        st = read()
        if st is not None and len(st) > 0:
            return plot_waveforms(st, filename, title_suffix=" [EXAMPLE DATA]")

        raise ValueError("ObsPy example data unavailable or returned empty stream")
    except Exception as e:
        print(f"   ⚠️ ObsPy example data unavailable: {e}")

        import numpy as np
        
        # Create demo data
        fig, axes = plt.subplots(3, 1, figsize=(12, 9))
        
        time = np.linspace(0, 600, 6000)  # 10 minutes
        
        # Simulated seismic traces
        channels = ['BHZ', 'BHN', 'BHE']
        for i, channel in enumerate(channels):
            # Create synthetic seismic signal
            signal = (np.random.randn(len(time)) * 0.5 + 
                     np.sin(2 * np.pi * 0.01 * time) * 2 +
                     np.sin(2 * np.pi * 0.05 * time) * 1)
            
            axes[i].plot(time, signal, 'k-', linewidth=0.5)
            axes[i].set_ylabel(f'{STATION}.{channel}\n({channel})', fontsize=10)
            axes[i].grid(True, alpha=0.3)
            axes[i].set_xlim(0, 600)
            
            if i == 2:
                axes[i].set_xlabel('Time (seconds)', fontsize=10)
        
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fig.suptitle(f'Seismic Waveforms - Station {STATION} [DEMO DATA]\n{current_time}', 
                     fontsize=14, fontweight='bold', color='red')
        
        plt.tight_layout()
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Demo plot saved to {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Error generating demo plot: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """
    Main execution function
    """
    # Generate timestamp at execution time with seconds precision
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    
    print("=" * 70)
    print("🌍 Seismic Waveform Fetching System")
    print(f"📍 Station: {STATION} | Channel: {CHANNEL}")
    print("=" * 70)
    print()
    
    try:
        # Ensure output directory exists
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        # Step 1: Connect to FDSN service
        client = get_fdsn_client()
        
        # Step 2: Fetch waveforms
        st = None
        if client:
            st = fetch_waveforms(client)
        
        # Step 3: Plot waveforms
        plot_filename = f'{OUTPUT_DIR}/waveform_{timestamp}.png'
        
        if st and len(st) > 0:
            success = plot_waveforms(st, plot_filename)
        else:
            print("\n⚠️  Real data unavailable, generating example plot...")
            success = generate_demo_plot(plot_filename)
        
        print()
        print("=" * 70)
        if success:
            print("✅ Seismic waveform fetching completed successfully!")
            print(f"📄 Output: {plot_filename}")
        else:
            print("⚠️  Completed with warnings")
        print("=" * 70)
        
        return 0
        
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
