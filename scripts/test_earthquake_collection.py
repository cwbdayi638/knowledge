#!/usr/bin/env python3
"""
Test script for earthquake collection - specifically testing None value handling
"""

import sys
import os

# Add the parent directory to the path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the function we want to test
from collect_earthquake_info import generate_markdown

def test_none_values_in_felt_reports():
    """Test that None values in felt reports don't cause TypeError"""
    
    # Create a mock earthquake with None for 'felt' field
    earthquakes = [
        {
            'properties': {
                'mag': 4.5,
                'place': 'Test Location',
                'time': 1707502800000,  # Some timestamp
                'alert': None,
                'tsunami': None,
                'felt': None,  # This is the problematic field
                'url': 'https://example.com'
            },
            'geometry': {
                'coordinates': [-122.0, 37.0, 10.0]
            }
        }
    ]
    
    print("Testing generate_markdown with None values...")
    try:
        markdown = generate_markdown(earthquakes)
        print("✅ Test PASSED: No TypeError occurred")
        print(f"Generated {len(markdown)} characters of markdown")
        
        # Verify that felt reports are not shown when None
        if 'Felt Reports' in markdown:
            print("⚠️  Warning: Felt Reports shown even though value was None")
        else:
            print("✅ Felt Reports correctly not shown for None value")
        
        return True
    except TypeError as e:
        print(f"❌ Test FAILED: TypeError occurred: {e}")
        return False

def test_zero_felt_reports():
    """Test that zero felt reports are handled correctly"""
    
    earthquakes = [
        {
            'properties': {
                'mag': 3.0,
                'place': 'Test Location 2',
                'time': 1707502800000,
                'alert': 'green',
                'tsunami': 0,
                'felt': 0,  # Explicit zero
                'url': 'https://example.com'
            },
            'geometry': {
                'coordinates': [-122.0, 37.0, 10.0]
            }
        }
    ]
    
    print("\nTesting generate_markdown with zero felt reports...")
    try:
        markdown = generate_markdown(earthquakes)
        print("✅ Test PASSED: No TypeError occurred")
        
        # Verify that felt reports are not shown when 0
        if 'Felt Reports' in markdown:
            print("⚠️  Warning: Felt Reports shown even though value was 0")
        else:
            print("✅ Felt Reports correctly not shown for zero value")
        
        return True
    except TypeError as e:
        print(f"❌ Test FAILED: TypeError occurred: {e}")
        return False

def test_positive_felt_reports():
    """Test that positive felt reports are shown correctly"""
    
    earthquakes = [
        {
            'properties': {
                'mag': 5.5,
                'place': 'Test Location 3',
                'time': 1707502800000,
                'alert': 'yellow',
                'tsunami': 0,
                'felt': 123,  # Positive value
                'url': 'https://example.com'
            },
            'geometry': {
                'coordinates': [-122.0, 37.0, 10.0]
            }
        }
    ]
    
    print("\nTesting generate_markdown with positive felt reports...")
    try:
        markdown = generate_markdown(earthquakes)
        print("✅ Test PASSED: No TypeError occurred")
        
        # Verify that felt reports ARE shown when positive
        if 'Felt Reports' in markdown and '123' in markdown:
            print("✅ Felt Reports correctly shown for positive value")
        else:
            print("⚠️  Warning: Felt Reports not shown even though value was 123")
        
        return True
    except TypeError as e:
        print(f"❌ Test FAILED: TypeError occurred: {e}")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("Running Earthquake Collection Tests")
    print("=" * 60)
    
    results = []
    results.append(test_none_values_in_felt_reports())
    results.append(test_zero_felt_reports())
    results.append(test_positive_felt_reports())
    
    print("\n" + "=" * 60)
    if all(results):
        print("✅ All tests PASSED!")
        print("=" * 60)
        sys.exit(0)
    else:
        print("❌ Some tests FAILED!")
        print("=" * 60)
        sys.exit(1)
