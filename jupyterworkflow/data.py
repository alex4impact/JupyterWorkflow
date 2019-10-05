import os
from urllib.request import urlretrieve
import pandas as pd

# Setting URL to retrieve the data
FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    """ Download and cache the frmeont data
    
    Parameters
    ----------
    filename: string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force redownload of data
        
    Returns
    -------
    data : padas.Dataframe
        The fremont bridge data
    """    
    if force_download or not os.path.exists(filename):
        # Downloading data from the URL
        urlretrieve(url, filename)
    # Loading the data in the notebook with Pandas
    # Setting the index column to the 'Date' column
    # Parsing the 'Date' column from strings to date type
    data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    # Changing the legend to 'East' and 'West'
    data.columns = ['East', 'West']
    # Adding the sum of the trends
    data['Total'] = data['East'] + data['West']
    return data