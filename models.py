import dataclasses


class Movie(object):
    def __init__(self, name='', id='', rating='', description='', premiere='', isSeries='',
                 year='', slogan='', genres='', countries='', persons='',
                 seasonsInfo='', **kwargs):
        self.name, self.id, self.rating, self.description = name, id, rating, description
        self.premiere, self.year, self.slogan = premiere, year, slogan
        self.persons = [Actor(**obj) for obj in persons]
        self.genres  = [name['name'] for name in genres]
        self.countries = [name['name'] for name in countries]
        
        self.isSeries = isSeries
        if isSeries:
            self.seasonsInfo = seasonsInfo
            
    
    def __str__(self):
        return ";".join([str(self.id), self.name])
    
    
class Actor(object):
    def __init__(self, id='', name='', enName='', **kwargs):
        self.id, self.name, self.enName = id, name, enName
        
    def __str__(self):
        return ';'.join([str(self.id), self.name])
    

class SeasonsInfo(object):
    def __init__(self, movieId='', number='', episodes='', **kwargs):
        self.movie_id, self.number = movieId, number
        self.episodes = [Episod(obj) for obj in episodes]
        
    def __str__(self):
        return ";".join([str(self.movie_id), str(self.number)])
    
    
class Episod(object):
    def __init__(self, number='', name='', enName='', description='', **kwargs):
        self.number, self.name, self.enName = number, name, enName
        self.description = description
        
    def __str__(self):
        return ";".join([str(self.number), self.name])