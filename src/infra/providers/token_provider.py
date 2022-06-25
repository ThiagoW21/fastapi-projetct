from datetime import datetime, timedelta
from jose import jwt


SECRET_KEY = 'secret-key'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 60


def create_access_token(data: dict):
    data_copy = data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    data_copy.update({'exp': expiration})

    token_jwt = jwt.encode(data_copy, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verify_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get('sub')
