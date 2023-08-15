from models import Movie, SeasonsInfo, Review

class Show:
    @staticmethod
    def show_movie(movie:Movie):
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
    def show_seasons(seasons):
        if seasons:
            season = iter(seasons)
            Show._rec_season(season)
        
        
    @staticmethod
    def _rec_season(iterable):
        try:
            season = next(iterable)
            Show.print_season(season)
            Show._rec_season(iterable)
        except StopIteration:
            return
            
    @staticmethod
    def print_season(season:SeasonsInfo):
        print('Сезон:', season.number)
        episodes = '\n'.join(str(i) for i in season.episodes)
        print(episodes)
        
    @staticmethod
    def show_review(reviews):
        if reviews:
            iterable = iter(reviews)
            Show._rec_review(iterable)
        
    @staticmethod
    def _rec_review(iterable):
        try:
            review = next(iterable)
            Show.print_review(review)
            Show._rec_review(iterable)
        except StopIteration:
            return
        
    @staticmethod
    def print_review(review:Review):
        print('Автор:', review.author)
        print('Заголовок:', review.title)
        print('Дата:', review.date)
        print('Оценка:', review.type)
        print('Текст:', review.review)
        print()