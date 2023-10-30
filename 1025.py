# importing modules and ibraries
import pandas as pd
import cartopy
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os
import numpy as np

########################################################################
#################### MAIN ####################
########################################################################
if __name__ == '__main__':
    start_time = time.time()
    program_path = os.getcwd()+'/'
    print('working directory ', program_path)
    # defining the paths
#    INPUT_PATH = program_path + 'INPUT/'
#    OUTPUT_PATH = program_path + 'OUTPUT/'
    # Read the Excel file
    df = pd.read_excel('wind_energy_data.xlsx')
#    df = pd.read_excel(INPUT_PATH+'wind_energy_data.xlsx')

    
    # Extracting the header
    # Get the header (column names) of the DataFrame
    header = df.columns
    print('your type header is ', type(header))
    print('your header is ', header)
    # Convert the header to a list
    # header.tolist() converts the Index object to a list of column names,
    header_list = header.tolist()
    # Print the list of column names
    print(header_list)
     # Extracting the variables for the dataframe
    lon = df['Longitude'].values
    lon2 = df.iloc[:,1].values
    #print(lon2[0:5])
    lat = df['Latitude'].values
    cost = df['Wind Energy Cost'].values
    bio_i = df['Biodiversity Impact'].values
    #flag = lon == lon2
    #print(flag)
    print(type(lon))
    
    # Printing some basic info about your data
    print('Your total cost is ', cost.sum())
    print('Your average cost is ', cost.mean())
    print('Your min, max cost are ', cost.min(), cost.max())
    print('MY FILE LENGTH ', len(cost))