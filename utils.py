import requests
import json
from models import Movie, SeasonsInfo

class APIRequest:
    LINK = "https://api.kinopoisk.dev/v1/"
    RANDOM = f"{LINK}movie/random"
    MOVIE = f"{LINK}movie"
    SEASON = f"{LINK}season"
    REVIEW = f"{LINK}review"
    PERSON = f"{LINK}person"

    def __init__(self, key):
        self._key = key
        self._headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'identity',
            'X-API-KEY': key
        }
        
    def get_random(self) -> Movie:
        response = requests.request('GET', self.RANDOM, headers=self._headers)
        if response.status_code == requests.codes.OK:
            api_json = json.loads(response.text)
            movie = Movie(**api_json)
            return movie
        return None
    
    def get_movie(self, id:int=0) -> Movie:
        param = {'id': str(id)}
        response = requests.request('GET', self.MOVIE, headers=self._headers, params=param)
        if response.status_code == requests.codes.OK:
            api_json = json.loads(response.text)
            docs = api_json.get('docs', [])
            if len(docs) > 0:
                movie = Movie(**docs[0])
                print(movie)
                return movie
        return None
    
    def get_sesson(self, id_movie:int=None) -> SeasonsInfo:
        param = {}
        if id:
            param = {"movieId": id_movie}
        response = requests.request('GET', self.SEASON, headers=self._headers, params=param)
        if response.status_code == requests.codes.OK:
            api_json = json.loads(response.text)
            docs = api_json.get('docs', [])
            if len(docs) > 0:
                season = SeasonsInfo(docs[0])
                print(season)
                return season
            
        return None