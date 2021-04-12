import aiohttp
from requests import Reqs
from cocktaildb import search, categories, ingredients, glasses

async def tequila_info():
  return await search(query='tequila')

async def list_of_categories():
  return await cocktaildb.categories()
