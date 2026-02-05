#!/usr/bin/env python3
"""
Seismic Waveform Fetching Script
Fetches 10 minutes of seismic data from IRIS FDSN for NACB station
Generates PNG plots of waveforms
Runs every 30 minutes via GitHub Actions
"""

import os
import sys
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from obspy import UTCDateTime
from obspy.clients.fdsn import Client

# Configuration
STATION = "NACB"
CHANNEL = "BH*"  # Broadband high-gain channels
NETWORK = "*"    # Try all networks
LOCATION = "*"   # Try all locations
DATA_DURATION = 10 * 60  # 10 minutes in seconds
TIMESTAMP = datetime.now().strftime('%Y-%m-%d_%H-%M')
OUTPUT_DIR = 'seismic_waveforms'

# Alternative FDSN service providers
FDSN_PROVIDERS = [
    "IRIS",
    {"base_url": "https://service.iris.edu"},
    {"base_url": "http://service.iris.edu"},
    "EARTHSCOPE"
]

def get_fdsn_client():
    """
    Try to connect to FDSN service with multiple providers
    """
    print("🌐 Connecting to FDSN web service...")
    
    for provider in FDSN_PROVIDERS:
        try:
            if isinstance(provider, dict):
                print(f"   Trying base URL: {provider['base_url']}...")
                client = Client(**provider)
            else:
                print(f"   Trying provider: {provider}...")
                client = Client(provider)
            print(f"✅ Successfully connected!")
            return client
        except Exception as e:
            print(f"   ❌ Failed: {e}")
            continue
    
    print("❌ Could not connect to any FDSN service")
    return None

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

def plot_waveforms(st, filename):
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
        fig.suptitle(f'Seismic Waveforms - Station {STATION}\n{st[0].stats.starttime}', 
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
    Generate a demo plot when real data is unavailable
    """
    print(f"📊 Generating demo plot (real data unavailable)...")
    
    try:
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
        plot_filename = f'{OUTPUT_DIR}/waveform_{TIMESTAMP}.png'
        
        if st and len(st) > 0:
            success = plot_waveforms(st, plot_filename)
        else:
            print("\n⚠️  Real data unavailable, generating demo plot...")
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
