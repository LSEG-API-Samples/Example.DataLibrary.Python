# Refinitiv Data Platform Library for Python
# This demonstrates how to use the content pricing interface to request streaming Quote and Trade data
# via a Script as opposed to running in a Jupyter Notebook

# As these tutorial Notebooks are categorised into sub-folders and to avoid the need for multiple config files, we will use the
# _RD_LIB_CONFIG_PATH_ environment variable to point to a single instance of the config file in the 
# top-level ***Configuration*** folder.
# Before proceeding, please **ensure you have entered your credentials** into the config file in the ***Configuration*** folder.
import os
os.environ["RD_LIB_CONFIG_PATH"] = "../../../Configuration"
import refinitiv.data as rd
import datetime
import json
import time
import asyncio

# Run the example for 30 seconds
exit_time = time.time() + 30 

# Callback function to display data or status events
# Function to handle the intial Refresh for each item
def handle_refresh(streaming_prices, instrument_name, fields):
    # One way to access data - get dataframe
    print(f"Refresh : {streaming_prices.get_snapshot()}")
    return

# Function to update dataframe, when we receive updates for individual items
def handle_update(streaming_prices, instrument_name, fields):
    # Alternative way of accesing data - access the updated fields
    print(f"Update : {instrument_name}:{fields}")
    
# Function to extract status code for an item as & when received from server
# Status contains a 'code' and a more detailed 'message'
def handle_status(streaming_prices, instrument_name, status):
    print(f"Status : {instrument_name}:{status['code']}:{status['message']}")

# Our main code section

# Open a session using the helper functions in the above Credentials section
rd.open_session()

# Define our Streaming Price object
streams = rd.content.pricing.Definition(
    ['EUR=', 'GBP=', 'JPY='],
    fields=['BID', 'ASK','BID_NET_CH','IRGPRC']
).get_stream()

# Callback for if we wanted to handle invidiual Refresh for each item
streams.on_refresh(handle_refresh)
# Specify callback handler for any updates
streams.on_update(handle_update)
# Specify callback handler for any updates
streams.on_status(handle_status)

# Send the requests to the server and open the streams for all items
streams.open()
# We should now start to receive the initial Refresh for the current field values
# followed by updates for the fields as and when they occur

# Loop until specified end time 
while (time.time() < exit_time):
    # The following line ensures the async event callback mechanism works
    asyncio.get_event_loop().run_until_complete(asyncio.sleep(1))
    
streams.close()
rd.close_session()
