from requests import Reqs

class Data:
    """
    Methods to get data from https://www.thecocktaildb.com/api.php
    """

    @staticmethod
    async def search(*, query: str = None, key: str = None, dict: bool = None, first_letter_only: bool = None, ingredient: bool = None, id: str = None): 
        # Key is only to be used if you Support them on patreon via https://www.patreon.com/thedatadb
        # First letter bool gives a list of names cocktails given the first letter

        dict = dict or False
        first_letter_only = first_letter_only or False
        ingredient = ingredient or False
        key = key or 1
        query = query or id

        if dict:
            if first_letter_only:
                # Returns a dict with 5 cocktail names that starts with the one-letter-query

                names_url = f'https://www.thecocktaildb.com/api/json/v1/{key}/search.php?f={query}'
                data_names = await Reqs.get(names_url)

                names_data_dict = {
                    'cocktail1': data_names['drinks'][0]['strDrink'],
                    'cocktail2': data_names['drinks'][1]['strDrink'],
                    'cocktail3': data_names['drinks'][2]['strDrink'],
                    'cocktail4': data_names['drinks'][3]['strDrink'],
                    'cocktail5': data_names['drinks'][4]['strDrink'],
                }
                print("Use `await recipe('drink from list')`")
                return names_data_dict
            
            elif ingredient:
                # Returns a dict information on an ingredient

                ingr_url = f'https://www.thecocktaildb.com/api/json/v1/{key}/search.php?i={query}'
                data_ingr = await Reqs.get(ingr_url)

                if data_ingr['ingredients'][0]['strAlcohol'] == 'Yes':
                    ingr_dict = {
                        'ingredientData': data_ingr['ingredients'][0]['strDescription'],
                        'Alcoholic': True
                    }

                else:
                    ingr_dict = {
                        'ingredientData': data_ingr['ingredients'][0]['strDescription'],
                        'Alcoholic': False
                    }
                return ingr_dict

            else:
                # Ingredients only goes up to 4

                url = f'https://www.thecocktaildb.com/api/json/v1/{key}/search.php?s={query}'
                data = await Reqs.get(url)

                data_dict = {
                    'instructions': data['drinks'][0]['strInstructions'],
                    'ing1': data['drinks'][0]['strIngredient1'], 
                    'ing2': data['drinks'][0]['strIngredient2'], 
                    'ing3': data['drinks'][0]['strIngredient3'], 
                    'ing4': data['drinks'][0]['strIngredient4']
                }
                return data_dict

        
        elif not dict:
            if first_letter_only:
                # Returns 5 cocktail names in a string that starts with the one-letter-query
                
                names_url = f'https://www.thecocktaildb.com/api/json/v1/{key}/search.php?f={query}'
                data_names = await Reqs.get(names_url)
                
                names_list = {
                    data_names['drinks'][0]['strDrink'],
                    data_names['drinks'][1]['strDrink'],
                    data_names['drinks'][2]['strDrink'],
                    data_names['drinks'][3]['strDrink'],
                    data_names['drinks'][4]['strDrink']
                }
                names = ', '.join(names_list)
                string = f'Names: {names}'
                
                print("Use `await recipe('drink from list')`")
                return string
            
            elif ingredient:
                # Returns a string of information on a given ingredient

                ingr_url = f'https://www.thecocktaildb.com/api/json/v1/{key}/search.php?i={query}'
                data_ingr = await Reqs.get(ingr_url)

                if data_ingr['ingredients'][0]['strAlcohol'] == 'Yes':
                    alcoholic = 'Ingredient is alcoholic.'
                else:
                    alcoholic = "Ingredient isn't alcoholic."

                description = data_ingr['ingredients'][0]['strDescription']
                string = f'{description} {alcoholic}'
                return string

            else:
                # Returns a string with instructions and ingredients
                
                url = f'https://www.thecocktaildb.com/api/json/v1/{key}/search.php?f={query}'
                data = await Reqs.get(url)

                data = data_dict
                instructions = data['instructions']
                ing1 = data['ing1']
                ing2 = data['ing2']
                ing3 = data['ing3']
                ing4 = data['ing4']
                string = f'{instructions}\nIngredients: {ing1}, {ing2}, {ing3}, {ing4}'
                return string

        else:
            print('That grouping of arguments is not supported.')
        