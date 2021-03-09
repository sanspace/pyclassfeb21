# Day 17

## Topics

  - Settings
  - Filtering
  - Status Codes
  - Testing
  - Caching
  - Throttling
  - Versioning
  - Exceptions
  - 12 Factor App

## Refer

  - Settings https://www.django-rest-framework.org/api-guide/settings/
  - Filtering https://www.django-rest-framework.org/api-guide/filtering/
  - Status Codes https://www.django-rest-framework.org/api-guide/status-codes/
  - Testing https://www.django-rest-framework.org/api-guide/testing/
  - Caching
    - https://www.django-rest-framework.org/api-guide/caching/
    - https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching

    > Today, most web applications are built upon APIs. An API generally is a RESTful web service that can be accessed over HTTP and exposes resources that allow the user to interact with the application. When designing an API, it’s important to consider the expected load on the API, the authorization to it, the effects of version changes on the API consumers and most importantly the API’s ease of use, among other considerations. It’s not always the case that an API needs to instantiate business logic and/or make a backend requests to a database on every request. Sometimes serving a cached result of the API will deliver the most optimal and cost-effective response. This is especially true when you are able to cache the API response to match the rate of change of the underlying data. Say for example, you exposed a product listing API to your users and your product categories only change once per day. Given that the response to a product category request will be identical throughout the day every time a call to your API is made, it would be sufficient to cache your API response for the day. By caching your API response, you eliminate pressure to your infrastructure including your application servers and databases. You also gain from faster response times and deliver a more performant API.

    https://aws.amazon.com/caching/#Application_Programming_Interfaces_.28APIs.29

  - 12 Factor App https://12factor.net/

## Practice

  - Try improvising your API with the topics we have seen today and come up with a plan for improvements.

## Bonus Challenge

  - Grade your app against the below parameters
    - Exception Handling
    - Testing
    - Logging
    - and more from the above resources
