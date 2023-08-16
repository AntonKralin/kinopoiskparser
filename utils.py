import requests
import json
from models import Movie, SeasonsInfo, Review

class APIRequest:
    LINK = "https://api.kinopoisk.dev/v1/"
    RANDOM = f"{LINK}movie/random"
    MOVIE = f"{LINK}movie/"
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
        
    def get_random(self) -> Movie | None:
        response = requests.request('GET', self.RANDOM, headers=self._headers)
        if response.status_code == requests.codes.OK:
            api_json = json.loads(response.text)
            movie = Movie(**api_json)
            return movie
        return None
    
    def get_movie(self, id:int=0) -> Movie | None:
        response = requests.request('GET', self.MOVIE+str(id), headers=self._headers)
        if response.status_code == requests.codes.OK:
            api_json = json.loads(response.text)
            movie = Movie(**api_json)
            return movie
        return None
    
    def get_sesson(self, id_movie:int=None) -> SeasonsInfo | None:
        param = {}
        if id:
            param['movieId'] = id_movie
        response = requests.request('GET', self.SEASON, headers=self._headers, params=param)
        if response.status_code == requests.codes.OK:
            api_json = json.loads(response.text)
            docs = api_json.get('docs', [])
            if len(docs) > 0:
                seasons = [SeasonsInfo(**i) for i in docs]
                return seasons          
        return None
    
    def get_review(self, id_movie:int=None) -> Review | None:
        param = {}
        if id_movie:
            param['movieId'] = id_movie
            
        response = requests.request('GET', self.REVIEW, headers=self._headers, params=param)
        if response.status_code == requests.codes.OK:
            api_json = json.loads(response.text)
            docs = api_json.get('docs', [])
            if len(docs) > 0:
                reviews = [Review(**r) for r in docs]
                return reviews
        return None