from utils import APIRequest
from settings import token


def main():
    api = APIRequest(token)
    #api.get_random()
    #api.get_movie(891645)
    api.get_sesson(891645)
    
    
if __name__ == '__main__':
    main()