from requests import Reqs

class Data:
    """
    Methods to get data from https://www.thecocktaildb.com/api.php
    """

    @staticmethod
    async def recipe(*, query, key: str = None, dict: bool = None): 
        # Key is only to be used if you Support them on patreon via https://www.patreon.com/thedatadb
        
        dict = dict or False
        key = key or 1
        url = f'https://www.thecocktaildb.com/api/json/v1/{key}/search.php?s={query}'
        data = await Reqs.get(url)
        data_dict = {
                'instructions': data['drinks'][0]['strInstructions'],
                'ing1': data['drinks'][0]['strIngredient1'], 
                'ing2': data['drinks'][0]['strIngredient2'], 
                'ing3': data['drinks'][0]['strIngredient3'], 
                'ing4': data['drinks'][0]['strIngredient4']
            }
        if dict:
            ## ingredients only goes up to 4
            return data_dict
        else:
            data = data_dict
            instructions = data['instructions']
            ing1 = data['ing1']
            ing2 = data['ing2']
            ing3 = data['ing3']
            ing4 = data['ing4']
            neat_data = f'{instructions}\nIngredients: {ing1}, {ing2}, {ing3}, {ing4}'
            return neat_data
