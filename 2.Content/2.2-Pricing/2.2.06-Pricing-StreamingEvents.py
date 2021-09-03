# Refinitiv Data Platform Library for Python
## Delivery - OMMItemStream - Market Price data via callback inside a Python Script

#This demonstrates how to use the OMM Item Stream interface to request streaming Quote and Trade data
#via a Script as opposed to running in a Jupyter Notebook

import refinitiv.data as rd
from refinitiv.data._data.legacy import get_default_session, set_default_session
from refinitiv.data.delivery import endpoint_request
import datetime
import json
import time
import logging.config
import configparser as cp
import asyncio
import os

APP_KEY                     = os.environ['APP_KEY'] # 'YOUR_APP_KEY'
RDP_LOGIN                   = os.environ['RDP_LOGIN'] # 'YOUR_REFINITIV_DATA_PLATFORM_LOGIN'
RDP_PASSWORD                = os.environ['RDP_PASSWORD'] # 'YOUR_REFINITIV_DATA_PLATFORM_PASSWORD'
DEPLOYED_PLATFORM_HOST      = 'THE_HOST:PORT_OF_YOUR_DEPLOYED_PLATFORM'  # e.g. 'myADS:15000'
DEPLOYED_PLATFORM_USER_NAME = 'YOUR_USER_NAME_ON_YOUR_DEPLOYED_PLATFORM' # DACS user name 

# Some Global variables
session=None # Our session

# Run for 180 seconds
exit_time = time.time() + 180 


def open_session(session_type=None):
    session = get_default_session()
    if session is None:
        if session_type == "desktop":
            session = rd.session.desktop.Definition(APP_KEY).get_session()
        elif session_type == "rdp":
            session = rd.session.platform.Definition(
                app_key=APP_KEY,
                grant=rd.session.platform.GrantPassword(
                    username=RDP_LOGIN,
                    password=RDP_PASSWORD
                )
            ).get_session()
        elif session_type == "deployed":
            session = rd.session.platform.Definition(
                app_key=APP_KEY,
                deployed_platform_host = DEPLOYED_PLATFORM_HOST,
                deployed_platform_username = DEPLOYED_PLATFORM_USER_NAME
            ).get_session()

    if session is None:
        raise Exception(f"Wrong session_type: {session_type}. It must be ['desktop', 'rdp', 'deployed']")
    else:
        #session.set_log_level(logging.DEBUG)
        session.set_log_level(logging.WARNING)
        set_default_session(session)
        session.open()
        return session
    
def close_session():
    session = get_default_session()
    if session:
        session.close()

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
open_session('rdp')

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
close_session()