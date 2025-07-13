#!/usr/bin/env python3
"""
3D Uranium Concentration Visualization Tool
==========================================

A comprehensive tool for visualizing uranium concentrations in groundwater
using interactive 3D maps with PyDeck.

Usage:
    python uranium_visualizer.py --input data.csv --output uranium_map.html
    python uranium_visualizer.py --input data.csv --color viridis --style dark
"""

import pandas as pd
import pydeck as pdk
import numpy as np
import warnings
import argparse
import os
import sys
from typing import List

# Configuration constants
DEFAULT_COLOR_SCHEMES = {
    'green_to_red': 'Green for low, red for high concentrations',
    'blue_to_red': 'Blue for low, red for high concentrations',
    'viridis': 'Scientific color scheme (purple to yellow)',
    'plasma': 'Scientific color scheme (purple to pink)'
}

MAP_STYLES = {
    'light': 'mapbox://styles/mapbox/light-v10',
    'dark': 'mapbox://styles/mapbox/dark-v10',
    'satellite': 'mapbox://styles/mapbox/satellite-v9',
    'outdoors': 'mapbox://styles/mapbox/outdoors-v11',
    'streets': 'mapbox://styles/mapbox/streets-v11'
}

class UraniumVisualizer:
    """Main class for creating 3D uranium concentration visualizations"""

    def __init__(self, csv_file: str, output_file: str = None):
        self.csv_file = csv_file
        self.output_file = output_file or 'uranium_3d_map.html'
        self.df = None
        self.stats = {}

    def load_and_validate_data(self) -> pd.DataFrame:
        """Load and validate uranium concentration data from CSV"""
        try:
            print(f"Loading data from {self.csv_file}...")
            self.df = pd.read_csv(self.csv_file)
            print(f"Initial data shape: {self.df.shape}")

            # Check for required columns
            required_columns = ['City', 'Latitude', 'Longitude', 'Uranium concentration (µg/L)']
            missing_columns = [col for col in required_columns if col not in self.df.columns]

            if missing_columns:
                print(f"ERROR: Missing required columns: {missing_columns}")
                print(f"Available columns: {list(self.df.columns)}")
                raise ValueError(f"Missing required columns: {missing_columns}")

            # Data cleaning and validation
            self.df = self._clean_data()
            self._calculate_statistics()

            print(f"Final data shape: {self.df.shape}")
            return self.df

        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise

    def _clean_data(self) -> pd.DataFrame:
        """Clean and validate the dataset"""
        df = self.df.copy()

        # Convert uranium concentration to numeric
        df['Uranium concentration (µg/L)'] = pd.to_numeric(
            df['Uranium concentration (µg/L)'], 
            errors='coerce'
        )

        # Remove rows with invalid coordinates
        initial_count = len(df)
        df = df.dropna(subset=['Latitude', 'Longitude'])
        if len(df) < initial_count:
            print(f"Removed {initial_count - len(df)} rows with invalid coordinates")

        # Handle negative or zero uranium concentrations
        negative_mask = df['Uranium concentration (µg/L)'] <= 0
        if negative_mask.any():
            negative_count = negative_mask.sum()
            warnings.warn(f"Found {negative_count} rows with negative/zero uranium concentrations. Setting to 0.1 µg/L.")
            df.loc[negative_mask, 'Uranium concentration (µg/L)'] = 0.1

        # Remove rows with NaN uranium concentrations
        df = df.dropna(subset=['Uranium concentration (µg/L)'])

        # Validate coordinate ranges
        valid_lat = (df['Latitude'] >= -90) & (df['Latitude'] <= 90)
        valid_lon = (df['Longitude'] >= -180) & (df['Longitude'] <= 180)

        if not valid_lat.all() or not valid_lon.all():
            invalid_count = (~valid_lat | ~valid_lon).sum()
            print(f"Removing {invalid_count} rows with invalid coordinates")
            df = df[valid_lat & valid_lon]

        return df

    def _calculate_statistics(self):
        """Calculate comprehensive statistics for the dataset"""
        uranium_values = self.df['Uranium concentration (µg/L)']

        self.stats = {
            'count': len(uranium_values),
            'min': uranium_values.min(),
            'max': uranium_values.max(),
            'mean': uranium_values.mean(),
            'median': uranium_values.median(),
            'std': uranium_values.std(),
            'q25': uranium_values.quantile(0.25),
            'q75': uranium_values.quantile(0.75),
            'range': uranium_values.max() - uranium_values.min(),
            'center_lat': self.df['Latitude'].mean(),
            'center_lon': self.df['Longitude'].mean(),
            'lat_range': self.df['Latitude'].max() - self.df['Latitude'].min(),
            'lon_range': self.df['Longitude'].max() - self.df['Longitude'].min()
        }

        print("\n" + "="*50)
        print("DATASET STATISTICS")
        print("="*50)
        print(f"Total locations: {self.stats['count']}")
        print(f"Uranium concentration (µg/L):")
        print(f"  Min:    {self.stats['min']:.2f}")
        print(f"  Max:    {self.stats['max']:.2f}")
        print(f"  Mean:   {self.stats['mean']:.2f}")
        print(f"  Median: {self.stats['median']:.2f}")
        print(f"  Std:    {self.stats['std']:.2f}")
        print(f"Geographic coverage:")
        print(f"  Center: ({self.stats['center_lat']:.4f}, {self.stats['center_lon']:.4f})")
        print("="*50)

    def create_color_scale(self, value: float, color_scheme: str = 'green_to_red') -> List[int]:
        """Create dynamic color scale based on data range extracted from CSV"""
        min_val = self.stats['min']
        max_val = self.stats['max']

        if max_val == min_val:
            return [128, 128, 128]  # Gray for uniform data

        # Normalize to [0, 1]
        normalized = (value - min_val) / (max_val - min_val)
        normalized = max(0, min(1, normalized))

        if color_scheme == 'green_to_red':
            if normalized <= 0.5:
                r = int(255 * (normalized * 2))
                g = 255
                b = 0
            else:
                r = 255
                g = int(255 * (2 - (normalized * 2)))
                b = 0

        elif color_scheme == 'blue_to_red':
            r = int(255 * normalized)
            g = int(255 * (1 - normalized) * 0.5)
            b = int(255 * (1 - normalized))

        elif color_scheme == 'viridis':
            # Viridis approximation
            r = int(255 * (0.267 + 0.005 * normalized + 0.334 * normalized**2))
            g = int(255 * (0.004 + 0.632 * normalized + 0.021 * normalized**2))
            b = int(255 * (0.329 + 0.549 * normalized - 0.137 * normalized**2))

        elif color_scheme == 'plasma':
            # Plasma approximation
            r = int(255 * (0.050 + 0.900 * normalized + 0.100 * normalized**2))
            g = int(255 * (0.030 + 0.350 * normalized + 0.100 * normalized**2))
            b = int(255 * (0.800 + 0.100 * normalized - 0.600 * normalized**2))

        else:
            raise ValueError(f"Unknown color scheme: {color_scheme}")

        return [max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b))]

    def calculate_height_scaling(self) -> callable:
        """Calculate optimal height scaling function based on CSV data range"""
        min_val = self.stats['min']
        max_val = self.stats['max']

        if max_val / min_val > 100:
            print("Using logarithmic height scaling for wide concentration range")
            return lambda x: np.log10(x + 1) * 1000
        else:
            print("Using linear height scaling")
            return lambda x: x * (5000 / max_val)

    def calculate_optimal_zoom(self) -> int:
        """Calculate optimal zoom level based on data spread"""
        max_range = max(self.stats['lat_range'], self.stats['lon_range'])

        if max_range > 10:
            return 5
        elif max_range > 5:
            return 6
        elif max_range > 2:
            return 7
        else:
            return 8

    def create_pydeck_visualization(self, 
                                   color_scheme: str = 'green_to_red',
                                   map_style: str = 'light') -> pdk.Deck:
        """Create PyDeck 3D visualization"""

        if self.df is None:
            raise ValueError("Data not loaded. Call load_and_validate_data() first.")

        print(f"\nCreating PyDeck visualization with {color_scheme} color scheme...")
        print(f"Using data range: {self.stats['min']:.2f} - {self.stats['max']:.2f} µg/L")

        # Prepare data
        df_viz = self.df.copy()

        # Add colors based on CSV data range
        df_viz['color'] = df_viz['Uranium concentration (µg/L)'].apply(
            lambda x: self.create_color_scale(x, color_scheme)
        )

        # Add heights
        height_scaler = self.calculate_height_scaling()
        df_viz['height'] = df_viz['Uranium concentration (µg/L)'].apply(height_scaler)

        # Create enhanced tooltips
        df_viz['tooltip'] = df_viz.apply(
            lambda row: (
                f"City: {row['City']}\n"
                f"Uranium: {row['Uranium concentration (µg/L)']:.1f} µg/L\n"
                f"Coordinates: ({row['Latitude']:.4f}, {row['Longitude']:.4f})"
            ),
            axis=1
        )

        # Define view state
        view_state = pdk.ViewState(
            latitude=self.stats['center_lat'],
            longitude=self.stats['center_lon'],
            zoom=self.calculate_optimal_zoom(),
            pitch=60,
            bearing=0,
            height=600,
            width=800
        )

        # Create column layer
        column_layer = pdk.Layer(
            'ColumnLayer',
            data=df_viz,
            get_position=['Longitude', 'Latitude'],
            get_elevation='height',
            get_fill_color='color',
            elevation_scale=1,
            radius=max(1000, 50000 / len(df_viz)),
            pickable=True,
            extruded=True,
            coverage=1,
            auto_highlight=True
        )

        # Create deck
        deck = pdk.Deck(
            layers=[column_layer],
            initial_view_state=view_state,
            tooltip={
                'text': '{tooltip}',
                'style': {
                    'color': 'white',
                    'backgroundColor': 'rgba(0,0,0,0.8)',
                    'fontSize': '12px',
                    'padding': '10px',
                    'borderRadius': '5px',
                    'whiteSpace': 'pre-line'
                }
            },
            map_style=MAP_STYLES.get(map_style, MAP_STYLES['light'])
        )

        return deck

    def save_visualization(self, deck: pdk.Deck, add_metadata: bool = True):
        """Save visualization with optional metadata"""

        # Save basic HTML
        deck.to_html(self.output_file)

        if add_metadata:
            # Add metadata to HTML
            self._add_metadata_to_html()

        print(f"\n✅ Visualization saved to: {self.output_file}")
        print(f"📊 Data points: {self.stats['count']}")
        print(f"📍 Geographic center: ({self.stats['center_lat']:.4f}, {self.stats['center_lon']:.4f})")
        print(f"🎨 Color range: {self.stats['min']:.1f} - {self.stats['max']:.1f} µg/L")

    def _add_metadata_to_html(self):
        """Add metadata and statistics to HTML file"""
        try:
            with open(self.output_file, 'r') as f:
                content = f.read()

            # Create metadata section
            metadata_html = f"""
            <!-- Uranium Visualization Metadata -->
            <div id="metadata" style="position: fixed; top: 10px; right: 10px; background: rgba(255,255,255,0.9); padding: 10px; border-radius: 5px; font-family: Arial, sans-serif; font-size: 12px; z-index: 1000; max-width: 300px;">
                <h3 style="margin: 0 0 10px 0; color: #333;">Uranium Concentration Data</h3>
                <p><strong>Data Points:</strong> {self.stats['count']}</p>
                <p><strong>Concentration Range:</strong> {self.stats['min']:.1f} - {self.stats['max']:.1f} µg/L</p>
                <p><strong>Mean:</strong> {self.stats['mean']:.1f} µg/L</p>
                <p><strong>Median:</strong> {self.stats['median']:.1f} µg/L</p>
                <p style="margin: 10px 0 0 0; font-size: 10px; color: #666;">
                    💡 Hover over columns for details<br>
                    🖱️ Click and drag to rotate<br>
                    📋 Source: {os.path.basename(self.csv_file)}
                </p>
            </div>
            """

            # Insert metadata before closing body tag
            content = content.replace('</body>', metadata_html + '\n</body>')

            with open(self.output_file, 'w') as f:
                f.write(content)

        except Exception as e:
            print(f"Warning: Could not add metadata to HTML: {str(e)}")

def main():
    """Main function with command-line interface"""
    parser = argparse.ArgumentParser(
        description="Create 3D visualization of uranium concentration data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python uranium_visualizer.py --input data.csv
    python uranium_visualizer.py --input data.csv --output my_map.html --color green_to_red
    python uranium_visualizer.py --input data.csv --style dark --color viridis
        """
    )

    parser.add_argument('--input', '-i', required=True, help='Input CSV file path')
    parser.add_argument('--output', '-o', help='Output HTML file path')
    parser.add_argument('--color', '-c', default='green_to_red', 
                        choices=list(DEFAULT_COLOR_SCHEMES.keys()),
                        help='Color scheme for visualization')
    parser.add_argument('--style', '-s', default='light', 
                        choices=list(MAP_STYLES.keys()),
                        help='Map style')
    parser.add_argument('--no-metadata', action='store_true', 
                        help='Disable metadata overlay')

    args = parser.parse_args()

    # Validate input file
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.")
        sys.exit(1)

    # Create output filename if not provided
    if not args.output:
        base_name = os.path.splitext(os.path.basename(args.input))[0]
        args.output = f"{base_name}_3d_map.html"

    try:
        # Create visualizer
        visualizer = UraniumVisualizer(args.input, args.output)

        # Load and validate data
        visualizer.load_and_validate_data()

        # Create visualization
        deck = visualizer.create_pydeck_visualization(
            color_scheme=args.color,
            map_style=args.style
        )

        # Save visualization
        visualizer.save_visualization(deck, add_metadata=not args.no_metadata)

        print(f"\n🎉 Success! Open '{args.output}' in your web browser to view the visualization.")
        print("\n📚 For hosting instructions, see: hosting_guide.md")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
