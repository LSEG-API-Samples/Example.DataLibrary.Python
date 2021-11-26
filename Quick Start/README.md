# Refinitiv Data Library for Python

## Summary

These Python tutorials demonstrate how to programmatically access content residing within the **Refinitiv Data Platform (RDP)** using a single, ease of use Library called the **Refinitiv Data Library for Python**.  The platform refers to the layer of data services providing both streaming and non-streaming content serving different clients, from the simple desktop interface to the enterprise application. 

The **Refinitiv Data Library for Python** is a Refinitiv supported Library  
It is available on PyPi at https://pypi.org/project/refinitiv-data/

The Refinitiv Data Library for Python is structured as a stack of interfaces and libraries designed to foster the adoption of our platform by both financial coders and professional developers to programmatically access financial content.    
  
Based on this stack of interfaces, the examples defined within this section have been organized into the following folders:

### **Configuration**

This folder contains the configuration file - ***refinitiv-data.config.json*** - for the Refinitiv Data Library for Python. Before running any of the tutorials, you must modify this file depending on the access channel and connection parameters that you will use to connect to the Refinitiv Data Platform. This necessary configuration step is explained in the [Quick Start guide](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/quick-start)

### **Quick Start**

The *Quick Start* example focuses on choosing the correct session type (Platform/Desktop/Deployed) and establishing a connection to validate your credentials/connectivity parameters.


### **Tutorials\\Content**

The *Content* examples target higher-level abstractions representing financial items like Pricing, News, Historical Data, etc. The *Content* layer can easily be used by both professional developers and financial coders. It provides great flexibility for commonly used financial objects.

### **Tutorials\\Delivery**

The *Delivery* examples target the interfaces defined within the lowest abstraction layer of the library.  The examples provide core level services including logging and WebSocket customization.  In addition, different delivery service examples such as Request/Reply data endpoints and real-time streaming data.

The examples should be used in conjunction with the **Tutorials** and **Documentation** available on the [Refinitiv Developer Portal](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python)
