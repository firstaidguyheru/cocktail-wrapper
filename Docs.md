Usage of search function:
```python
import cocktaildb 

async def tequila_info():
  return await cocktaildb.search(query='tequila')
```
Parameters include query, id, key, category, dict: bool, first_letter_only: bool, ingredient: bool, random: bool. 
All of which default to either None or False.

Lists of categories, ingredients etc. that may appear:
```
import cocktaildb

# This is in literally a list, not in the form of a dict or string
async def list_of_categories():
   return await cocktaildb.categories()
```
There are more functions such as glasses() and ingredients().

This is a simple api wrapper that only supports free endpoints (for now atleast).
