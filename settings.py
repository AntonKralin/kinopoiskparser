from dotenv import dotenv_values
from myexception import ValueNoException

def get_token() -> str | None:
    try:
        env_dict = dotenv_values('.env')
        if not env_dict.get('token'):
            raise ValueNoException("token")
        return env_dict.get('token')
    except ValueNoException:
        print('token not found')
        return None