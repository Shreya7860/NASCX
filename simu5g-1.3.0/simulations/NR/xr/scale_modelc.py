#!/usr/bin/env python3
"""
Scale down the size_bytes in ModelC_results.csv to have mean around 60 KB
"""

import pandas as pd

# Read the current file
df = pd.read_csv('ModelC_results.csv')

print("Current data:")
print(f"  Rows: {len(df)}")
print(f"  Current mean size: {df['size_bytes'].mean():,.0f} bytes ({df['size_bytes'].mean()/1024:.1f} KB)")
print(f"  Current range: {df['size_bytes'].min():,} to {df['size_bytes'].max():,} bytes")

# Scale to target mean of 60 KB
target_mean = 60000  # 60 KB in bytes
current_mean = df['size_bytes'].mean()
scaling_factor = target_mean / current_mean

print(f"\nScaling:")
print(f"  Target mean: {target_mean:,} bytes ({target_mean/1024:.1f} KB)")
print(f"  Scaling factor: {scaling_factor:.6f}")

# Apply scaling
df['size_bytes'] = (df['size_bytes'] * scaling_factor).round().astype(int)

print(f"\nNew data:")
print(f"  New mean size: {df['size_bytes'].mean():,.0f} bytes ({df['size_bytes'].mean()/1024:.1f} KB)")
print(f"  New range: {df['size_bytes'].min():,} to {df['size_bytes'].max():,} bytes")

# Save back to file
df.to_csv('ModelC_results.csv', index=False)
print(f"\nSaved to ModelC_results.csv")

# Show first few rows
print("\nFirst 5 rows:")
print(df.head())
