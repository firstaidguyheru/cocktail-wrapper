from requests import Reqs

"""Function responsible for getting data from https://www.thecocktaildb.com/api.php"""
	
class UnexpectedArgs(Exception):
	def __init__(self, message):
		super(UnexpectedArgs, self).__init__(message)

class UnsubscriptableKey(Exception):
	def __init__(self, message):
		super(UnsubscriptableKey, self).__init__(message)

async def categories():
	# Returns a list of categories 

	category_url = 'https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list'
	data_categories = await Reqs.get(category_url)
	
	l = [category['strCategory'] for category in data_categories['drinks']]

	return l

async def search(*, query: str = None, id: any = None, key: str = None, category: str = None, dict: bool = False, first_letter_only: bool = False, ingredient: bool = False, random: bool = False): 
	"""
	Key is only to be used if you Support them on patreon via https://www.patreon.com/thedatadb
	First letter bool gives a list of names cocktails given the first letter
	"""

	key = key or 1
	query = query or id

	if category and query \
		or category and id:
		raise UnexpectedArgs('That grouping of arguments is not supported.')
		
	elif category:
		# Returns a list of ids given a category
		
		category_url = f'https://www.thecocktaildb.com/api/json/v1/{key}/filter.php?c={category}'
		data_category = await Reqs.get(url=category_url)
		
		try:
			l = [id_dict['idDrink'] for id_dict in data_category['drinks']]
			
			return l

		except TypeError:
			raise UnsubscriptableKey('Category not found.')

	elif dict:
		if category:
			raise UnexpectedArgs('That grouping of arguments is not supported.')

		elif random and query \
			or id and random:
			raise UnexpectedArgs('That grouping of arguments is not supported.')
		
		elif random:
			# Random cocktail dict, ingredients only go up to 4

			random_url = f'https://www.thecocktaildb.com/api/json/v1/{key}/random.php'
			data_random = await Reqs.get(random_url) 

			data_dict = {
				'instructions': data_random['drinks'][0]['strInstructions'],
				'ing1': data_random['drinks'][0]['strIngredient1'], 
				'ing2': data_random['drinks'][0]['strIngredient2'], 
				'ing3': data_random['drinks'][0]['strIngredient3'], 
				'ing4': data_random['drinks'][0]['strIngredient4']
			}
			return data_dict

		elif first_letter_only:
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
			print("Use `await search(query='drink from list')`")
			return names_data_dict

		elif query == id and id == query:
			raise UnexpectedArgs('That grouping of arguments is not supported.')

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
		
		elif query:
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
		
		else:
			raise UnexpectedArgs('That grouping of arguments is not supported.')

	elif not dict:
		if random and query \
			or id and random:
			raise UnexpectedArgs('That grouping of arguments is not supported.')
			
		elif random:
			# Refuses to work so capping to only dict version
		
			raise UnexpectedArgs('That grouping of arguments is not supported.')

		if first_letter_only:
			# Returns 5 cocktail names in a string that starts with the one-letter-query
			
			names_url = f'https://www.thecocktaildb.com/api/json/v1/{key}/search.php?f={query}'
			data_names = await Reqs.get(names_url)
			
			names_list = [
				data_names['drinks'][0]['strDrink'],
				data_names['drinks'][1]['strDrink'],
				data_names['drinks'][2]['strDrink'],
				data_names['drinks'][3]['strDrink'],
				data_names['drinks'][4]['strDrink']
			]
			names = ', '.join([not_none for not_none in list(map(str, names_list)) if not not_none == 'null'])
			string = f'Names: {names}.'
			
			print("Use `await search(query='drink from list')`")
			return string

		elif query == id and id == query:
			raise UnexpectedArgs('That grouping of arguments is not supported.')

		elif ingredient:
			# Returns a string of information on a given ingredient

			ingr_url = f'https://www.thecocktaildb.com/api/json/v1/{key}/search.php?i={query}'
			data_ingr = await Reqs.get(ingr_url)

			if data_ingr['ingredients'][0]['strAlcohol'] == 'Yes':
				alcoholic = 'Ingredient is alcoholic.'
			else:
				alcoholic = "Ingredient isn't alcoholic."

			description = data_ingr['ingredients'][0]['strDescription']
			string = f'{description}. {alcoholic}.'
			return string

		elif query:
			# Returns a string with instructions and ingredients
			
			url = f'https://www.thecocktaildb.com/api/json/v1/{key}/search.php?s={query}'
			data = await Reqs.get(url)

			data_dict = {
				'instructions': data['drinks'][0]['strInstructions'],
				'ing1': data['drinks'][0]['strIngredient1'], 
				'ing2': data['drinks'][0]['strIngredient2'], 
				'ing3': data['drinks'][0]['strIngredient3'], 
				'ing4': data['drinks'][0]['strIngredient4']
			}
			data = data_dict

			instructions = data['instructions']
			ingr_list = [
				data['ing1'],
				data['ing2'],
				data['ing3'],
				data['ing4']
			]
			ingrs = ', '.join([not_none for not_none in list(map(str, ingr_list)) if not not_none == 'null'])
			string = f'{instructions}. Ingredients: {ingrs}.'
			return string

		else:
			raise UnexpectedArgs('That grouping of arguments is not supported.')