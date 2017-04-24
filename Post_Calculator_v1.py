import pandas as pd
import math as m
from geopy.distance import vincenty
#from decimal import *

## Import post code data
postcodes = pd.read_csv('ukpostcodes.csv')
#postcodes.head()
#postcodes.tail()
#postcodes.info()
#postcodes.describe()

postcodes.set_index('id', inplace=True) # Remove automatic index

# Convert lat and long to radians for faster code later
postcodes['latitude_rad'] = postcodes['latitude'].apply(m.radians)
postcodes['longitude_rad'] = postcodes['longitude'].apply(m.radians)

## Function to first get bounding coordinates and then only postcodes closest to our submission
def closest(postcode, kilometers):
    
    latitude_rad = postcodes[postcodes['postcode']==postcode]['latitude_rad'].values
    longitude_rad = postcodes[postcodes['postcode']==postcode]['longitude_rad'].values
    
    latitude = postcodes[postcodes['postcode']==postcode]['latitude'].values
    longitude = postcodes[postcodes['postcode']==postcode]['longitude'].values
    
    r = (kilometers / 6371)# Angular radius / 6371km = aprox radius of the earth 
    
    lat_min = float(latitude_rad - r)# Get min/max latitudes of our bounding box
    lat_max = float(latitude_rad + r)
    
    delta_long = m.asin(m.sin(r)/m.cos(latitude_rad))
    
    long_min = float(longitude_rad - delta_long)# Get min/max longitude of our bounding box
    long_max = float(longitude_rad + delta_long)
    
    # Get all postcodes within the bounding box and calculate the distance to these
    postcodes_within = postcodes[(postcodes['latitude_rad'] > lat_min) & (postcodes['latitude_rad'] < lat_max)
            & (postcodes['longitude_rad'] > long_min) & (postcodes['longitude_rad'] < long_max)][['postcode','latitude','longitude']]
    
    M = (latitude, longitude) #This is the center
    
    distance = [] # Create an empty list to store distance values
    
    for row in postcodes_within.itertuples():   # Iterate over postcodes to get distance values
        b = (float(row.latitude), float(row.longitude))
        distance.append(vincenty(M, b).kilometers)
    
    postcodes_within['distance'] = distance   # add distance results to dataframe
    
    postcodes_final = postcodes_within[postcodes_within['distance'] < kilometers] # filter results that are too far away
    
    return postcodes_final #return results
 
