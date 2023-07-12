import json
from pprint import pprint
from typing import TypedDict

# dumps = jogar (pra fora) - s no final signigica string
# loads = carregar (pra dentro) - s no final signigica string


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: float | None


string_json = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
'''
movie: Movie = json.loads(string_json)
pprint(movie)

dumps_json = json.dumps(movie, ensure_ascii=False, indent=2)
print(dumps_json)
