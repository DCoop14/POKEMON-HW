# import requests
# import app from routes





# def get_pokemon(id):
#     r = requests.get(f"http://pokeapi.co/api/v2/pokemon/{id}")
#     # print(r)
    
#     data = {
#         'name': r.json()['forms'][0]['name'],
#         'ability': r.json()['abilities'][1]['ability']['name'],
#         'base_experience': r.json()['base_experience'],
#         'img_url': r.json()['sprites']['front_shiny'],
#         'attack': r.json()['stats'][1]['stat']['url'],
#         'hp': r.json()['stats'][0]['stat']['url'],
#         'defense': r.json()['stats'][2]['stat']['url'],
#     }
#     return data