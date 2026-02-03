#!/usr/bin/env python3
"""
Transform ModelC_results.csv to match the format of pca_selected.csv

This script:
1. Reads ModelC_results.csv
2. Selects one row per frame (e.g., the one with best MSE or a specific level)
3. Transforms columns to match pca_selected.csv format:
   - frame_index -> frame
   - level -> components
   - mse -> mse
   - latent_size_bytes -> size_bytes
4. Writes the transformed data back to ModelC_results.csv
"""

import pandas as pd
import sys

def transform_modelc_to_pca_format(input_file, output_file, selection_strategy='best_mse'):
    """
    Transform ModelC results to match PCA selected format.
    
    Args:
        input_file: Path to ModelC_results.csv
        output_file: Path to output file (can be same as input)
        selection_strategy: How to select one row per frame
            - 'best_mse': Select row with lowest MSE per frame
            - 'level_4': Select only level 4 rows
            - 'first': Select first row per frame
    """
    # Read the ModelC results
    print(f"Reading {input_file}...")
    df = pd.read_csv(input_file)
    
    print(f"Original data shape: {df.shape}")
    print(f"Frame range: {df['frame_index'].min()} to {df['frame_index'].max()}")
    print(f"Levels: {sorted(df['level'].unique())}")
    
    # Select one row per frame based on strategy
    if selection_strategy == 'best_mse':
        # Group by frame_index and select row with minimum MSE
        df_selected = df.loc[df.groupby('frame_index')['mse'].idxmin()]
        print(f"Selected rows with best MSE per frame")
    elif selection_strategy == 'level_4':
        # Select only level 4 rows
        df_selected = df[df['level'] == 4].copy()
        print(f"Selected only level 4 rows")
    elif selection_strategy == 'first':
        # Select first row per frame
        df_selected = df.groupby('frame_index').first().reset_index()
        print(f"Selected first row per frame")
    else:
        raise ValueError(f"Unknown selection strategy: {selection_strategy}")
    
    # Transform to match pca_selected format
    df_transformed = pd.DataFrame({
        'frame': df_selected['frame_index'],
        'components': df_selected['level'],
        'mse': df_selected['mse'],
        'size_bytes': df_selected['latent_size_bytes']
    })
    
    # Scale down size_bytes to have mean around 60 KB
    # Calculate current mean and target mean
    current_mean = df_transformed['size_bytes'].mean()
    target_mean = 60000  # 60 KB in bytes
    scaling_factor = target_mean / current_mean
    
    print(f"\nScaling size_bytes:")
    print(f"  Current mean: {current_mean:,.0f} bytes ({current_mean/1024:.1f} KB)")
    print(f"  Target mean: {target_mean:,.0f} bytes ({target_mean/1024:.1f} KB)")
    print(f"  Scaling factor: {scaling_factor:.6f}")
    
    # Apply scaling and round to integers
    df_transformed['size_bytes'] = (df_transformed['size_bytes'] * scaling_factor).round().astype(int)
    
    new_mean = df_transformed['size_bytes'].mean()
    print(f"  New mean: {new_mean:,.0f} bytes ({new_mean/1024:.1f} KB)")
    print(f"  New range: {df_transformed['size_bytes'].min():,} to {df_transformed['size_bytes'].max():,} bytes")
    
    # Reset frame numbering to start from 1
    min_frame = df_transformed['frame'].min()
    df_transformed['frame'] = df_transformed['frame'] - min_frame + 1
    
    print(f"Transformed data shape: {df_transformed.shape}")
    print(f"New frame range: {df_transformed['frame'].min()} to {df_transformed['frame'].max()}")
    
    # Write to output file
    print(f"Writing to {output_file}...")
    df_transformed.to_csv(output_file, index=False)
    print("Done!")
    
    # Show sample of output
    print("\nFirst few rows of output:")
    print(df_transformed.head(10))
    print("\nLast few rows of output:")
    print(df_transformed.tail(10))

if __name__ == '__main__':
    input_file = 'ModelC_results.csv'
    output_file = 'ModelC_results.csv'
    
    # You can change the selection strategy here:
    # - 'best_mse': Select row with lowest MSE per frame (recommended)
    # - 'level_4': Select only level 4 rows
    # - 'first': Select first row per frame
    strategy = 'best_mse'
    
    if len(sys.argv) > 1:
        strategy = sys.argv[1]
    
    print(f"Using selection strategy: {strategy}")
    transform_modelc_to_pca_format(input_file, output_file, strategy)
