import cocktaildb

async def tequila_info():
  return await cocktaildb.search(query='tequila')

async def list_of_categories():
  return await cocktaildb.categories()
