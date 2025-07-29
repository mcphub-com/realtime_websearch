```markdown
# Aigeon AI Real-Time Web Search

## Project Overview

Aigeon AI Real-Time Web Search is a Python-based server application designed to provide real-time organic search results from across the web. It leverages advanced search parameters and geo-targeting to simulate real user searches, offering support for various Google Search parameters and advanced search operators. This project is ideal for developers looking to integrate real-time search capabilities into their applications.

## Features Overview

- Real-time search results retrieval from the web.
- Support for Google Search parameters such as `gl`, `hl`, `tbs`, and more.
- City-level geo-targeting to simulate searches from specific locations.
- Integration of Google Advanced Search operators like `inurl:`, `site:`, and `intitle:`.
- Batch processing capability to handle up to 100 queries in a single request.

## Main Features and Functionality

### Real-Time Search

The application provides a tool to perform real-time searches using a variety of parameters to refine and target search results. It supports advanced search operators and allows for detailed customization of the search process, including language and region specifications.

### Batch Search

A lightning-fast endpoint is available for batch processing, enabling the submission of up to 100 queries in a single request. This feature is designed to efficiently handle large volumes of search requests, making it suitable for applications requiring high throughput.

## Main Functions Description

### `search`

This function retrieves real-time organic search results with support for various Google Search parameters and city-level geo-targeting. It allows for detailed customization of the search query through the following parameters:

- `q` (str): The search query.
- `num` (int|float, optional): Maximum number of results to return.
- `start` (int|float, optional): Number of results to skip for pagination.
- `gl` (str, optional): The country/region for the query.
- `hl` (str, optional): The language for the search.
- `tbs` (str, optional): Advanced search parameters.
- `location` (str, optional): The origin location of the search, recommended at the city level.
- `nfpr` (str, optional): Exclude or include results of auto-corrected queries.

### `batch_search`

This function provides a high-performance endpoint for retrieving organic search results in real-time, supporting up to 100 queries in a single request. It is designed for applications that require processing multiple search queries efficiently.

---

This project is a robust solution for integrating real-time web search capabilities into applications, offering flexibility and efficiency through its advanced features and functionalities.
```