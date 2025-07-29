import requests
from datetime import datetime
from typing import Union
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

mcp = FastMCP('real-time-web-search')

@mcp.tool()
def search(q: Annotated[str, Field(description="Search query.")],
           num: Annotated[Union[int|float], Field(description="Maximum number of results to return.")] = None,
           start: Annotated[Union[int|float], Field(description="Number of results to skip (for pagination).")] = None,
           gl: Annotated[str, Field(description="The country / region for which to make the query.")] = None,
           hl: Annotated[str, Field(description="The language to use for the search (Google's hl parameter).")] = None,
           tbs: Annotated[str, Field(description="This parameter defines advanced search parameters that aren't available using regular query parameters (to be searched).")] = None,
           location: Annotated[str, Field(description="Where you want the search to originate from. It is recommended to specify location at the city level in order to simulate a real user’s search (e.g. London, England, United Kingdom).")] = None,
           nfpr: Annotated[str, Field(description="Exclude results of auto-corrected query when the original query is misspelled with nfpr=1 and include them with nfpr=0 (default).")] = None) -> dict:
    '''Get real-time organic search results from across the web with support for Google Search parameters (gl, hl, tbs, etc) and city level geo targeting. Supports all Google Advanced Search operators such (e.g. inurl:, site:, intitle:, etc).'''
    url = 'https://real-time-web-search.p.rapidapi.com/search-advanced'
    headers = {'x-rapidapi-host': 'real-time-web-search.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'num': num,
        'start': start,
        'gl': gl,
        'hl': hl,
        'tbs': tbs,
        'location': location,
        'nfpr': nfpr,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def batch_search() -> dict:
    '''Lightning fast endpoint for getting organic search results from across the web in real-time with support for up to 100 queries in a single request. Supports all Google Advanced Search operators such (e.g. inurl:, site:, intitle:, etc).'''
    url = 'https://real-time-web-search.p.rapidapi.com/search'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'real-time-web-search.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    response = requests.post(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")