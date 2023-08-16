from utils import APIRequest
from messages import Show
from settings import get_token


def main() -> None:
    token = get_token()
    if not token:
        return
    api = APIRequest(token)
    while True:
        print('\nВыберите одно из возможных действий:')
        print('1 - случайный фильм; 2 - получить информацию о фильме;')
        print('3 - получить все сезоны и эпизоды; 4 - отзывы пользователей')
        print('Все остальные значения - выход')
        action = int(input('Выберите действие: '))

        if action == 1:
            movie = api.get_random()
            Show.show_movie(movie)
        elif action == 2:
            movie_id = int(input('Введите id: '))
            movie = api.get_movie(movie_id)
            Show.show_movie(movie)
        elif action == 3:
            movie_id = int(input('Введите id: '))
            seasons = api.get_sesson(movie_id)
            Show.show_seasons(seasons)
        elif action == 4:
            movie_id = int(input('Введите id: '))
            reviews = api.get_review(movie_id)
            Show.show_review(reviews)
        else:
            print('Выход')
            break
        
        print()
    
if __name__ == '__main__':
    main()