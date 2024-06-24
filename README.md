<img src="https://developers.lseg.com/content/dam/devportal/icons/logo/lseg-logo.svg" width="20%" style="vertical-align: top;">

# Data Library for Python

## Summary

The LSEG Data Library for Python provides a set of ease-of-use interfaces offering coders uniform access to the breadth and depth of financial data and services available on the LSEG Data Platform. The platform refers to the layer of data services providing streaming and non-streaming content, bulk content and even more, serving different client types from the simple desktop interface to the enterprise application. With the LSEG Data Library, the same Python code can be used to retrieve data regardless of which access point you choose to connect to the platform. The series of examples presented in this project demonstrate how to use the LSEG Data Library for these different use cases.

The library provides multiple layers of abstraction allowing for different styles and programming technics suitable for all developers, from financial coders to seasoned developers:


 - The *__Access layer__* is the easiest way to get LSEG data. It provides simple interfaces allowing you to quickly prototype solutions in interactive environments such as Jupyter Notebooks. It was designed for quick experimentation with our data and for the specific needs of financial coders. 
 - The *__Content layer__* is the foundation of the _Access layer_. It provides developers with interfaces suitable for more advanced use cases (synchronous function calls, async/await, event driven). The _Content layer_ refers to logical market data objects such as market data prices and quotes, fundamental & reference data, historical data, company research data and so on. 
 - The *__Delivery layer__* is a lower abstraction layer that allows your applications to retrieve data using the service agnostic delivery mechanisms defined by the LSEG Data Platform. The _Delivery layer_ is a foundational component of the _Content layer_.
 - The *__Session layer__* defines interfaces allowing your application to connect to the LSEG Data Platform via its various access points (either via a direct connection, via Eikon, via the LSEG Workspace, via CodeBook or even via a local Real-Time Distribution System).

The organisation of this section is based on these layers so that you can quickly find the examples that best suit your specific use case.

## Learn more

To learn more about the LSEG Data Library for Python simply log into the LSEG Developer Community. By [registering](https://developers.refinitiv.com/iam/register) and [logging in](https://developers.refinitiv.com/content/devportal/en_us/initCookie.html) to the LSEG Developer Community portal you will have free access to a number of learning materials such as [Quick Start guides](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/quick-start), [Tutorials](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/tutorials), [Documentation](https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/documentation) and much more.

## Help and Support

If you have any questions regarding using the API, please post them on the [LSEG Data Q&A Forum](https://community.developers.refinitiv.com/spaces/321/index.html). The LSEG Developer Community will be very pleased to help you. 
