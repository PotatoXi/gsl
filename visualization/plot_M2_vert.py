#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

def main():

    # Load data
    data = load_data(filename='2012jb009865_table_s1.txt')
    # Compute marker size from M2 amplitude
    s = 5 * data['m2_amp']

    fig = plt.figure(figsize=(10, 10))

    # Label axes of a Plate Carree projection with a central longitude of 205:
    proj = ccrs.PlateCarree(central_longitude=205)
    ax1 = fig.add_subplot(1, 1, 1, projection=proj)
    ax1.set_global()
    ax1.coastlines()

    # Plot scatter data
    sc = ax1.scatter(data['lon'], data['lat'], s=s, c='C0', linewidths=0.75, edgecolors='k',
                     alpha=0.75, transform=ccrs.Geodetic())

    # Produce a legend with a cross section of sizes from the scatter
    handles, labels = sc.legend_elements(prop='sizes', num=4, alpha=0.6,
                                         markerfacecolor='C0', func=lambda x: x/5)
    legend2 = ax1.legend(handles, labels, bbox_to_anchor=(1.01, 1.0), ncols=2,
                         frameon=False, title='M2 amplitude')

    ax1.set_xticks([0, 60, 120, 180, 240, 300, 360], crs=ccrs.PlateCarree())
    ax1.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=ccrs.PlateCarree())
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax1.xaxis.set_major_formatter(lon_formatter)
    ax1.yaxis.set_major_formatter(lat_formatter)

    plt.tight_layout()
    plt.show()

    # Make another figure using Robinson projection
    fig = plt.figure(figsize=(8, 10))
    ax1 = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
    ax1.set_global()
    ax1.coastlines()

    # Plot scatter data
    ax1.scatter(data['lon'], data['lat'], s=s, c='C0', linewidths=0.75, edgecolors='k',
                alpha=0.75, transform=ccrs.Geodetic())

    # Produce a legend with a cross section of sizes from the scatter
    handles, labels = sc.legend_elements(prop='sizes', num=4, alpha=0.6,
                                         markerfacecolor='C0', func=lambda x: x/5)
    legend2 = ax1.legend(handles, labels, bbox_to_anchor=(0.62, 1.2), ncols=2,
                         frameon=False, title='M2 amplitude')

    plt.tight_layout()
    plt.show()


def load_data(filename):

    # Create empty lists for data
    names = []
    lat = []
    lon = []
    m2_amp = []
    m2_phs = []

    # Loop over lines
    with open(filename, 'r') as fid:
        for raw_line in fid:

            # Skip comments
            if raw_line.startswith('#'):
                continue

            # Strip off empty spaces
            line = raw_line.strip()

            # Split line into space-delimited strings
            fields = line.split()
            
            # Check for lines that contain station name and coordinates
            if len(fields) > 18:
                names.append(fields[0])
                lat.append(float(fields[1]))
                lon.append(float(fields[2]))

            # Now skip lines that don't start with 'U'
            if not line.startswith('U'):
                continue

            # Store M2 amp and phase
            m2_amp.append(float(fields[1]))
            m2_phs.append(float(fields[2]))

    # Store final data into dictionary (could also use a pd.DataFrame)
    data = {'names': names,
            'lat': np.array(lat),
            'lon': np.array(lon),
            'm2_amp': np.array(m2_amp),
            'm2_phs': np.array(m2_phs)}

    return data
        
if __name__ == '__main__':
    main()

# end of file
