import re
from models import Movie, SeasonsInfo, Review


class Show:
    @staticmethod
    def show_movie(movie:Movie) -> None:
        if movie:
            print('id:', movie.id)
            print('Название:', movie.name)
            print('Слоган:', movie.slogan)
            print('Рейтинг:', movie.rating)
            print('Описание:', movie.description)
            print('Год:', movie.year)
            print('Жанр:', movie.genres)
            print('Страна:', movie.countries)
            actors = '; '.join(str(i) for i in movie.persons)
            print('Актеры:', actors)
            if movie.isSeries:
                season_info = ', '.join(str(i) for i in movie.seasonsInfo)
                print('Сезон:', season_info)

    @staticmethod
    def show_seasons(seasons) -> None:
        if seasons:
            season = iter(seasons)
            Show._rec_season(season)
        
        
    @staticmethod
    def _rec_season(iterable) -> None:
        try:
            season = next(iterable)
            Show.print_season(season)
            Show._rec_season(iterable)
        except StopIteration:
            return
            
    @staticmethod
    def print_season(season:SeasonsInfo) -> None:
        print('Сезон:', season.number)
        if len(season.episodes) > 0:
            episodes = '\n'.join(str(i) for i in season.episodes)
            print(episodes)
        
    @staticmethod
    def show_review(reviews) -> None:
        if reviews:
            iterable = iter(reviews)
            Show._rec_review(iterable)
        
    @staticmethod
    def _rec_review(iterable) -> None:
        try:
            review = next(iterable)
            Show.print_review(review)
            Show._rec_review(iterable)
        except StopIteration:
            return
        
    @staticmethod
    def print_review(review:Review) -> None:
        print('Автор:', review.author)
        print('Заголовок:', review.title)
        print('Дата:', review.date)
        print('Оценка:', review.type)
        text = re.sub(r'<.*?>', '', review.review)
        print('Текст:', text)
        print()