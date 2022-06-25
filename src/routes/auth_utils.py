from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.data_base import get_db
from src.infra.providers import token_provider
from jose import JWSError
from src.infra.sqlalchemy.repositories.users import RepositoryUsers


oaut2_schema = OAuth2PasswordBearer(tokenUrl='token')


def get_logged_in_user(token: str = Depends(oaut2_schema), session: Session = Depends(get_db)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')


    try:
        email = token_provider.verify_access_token(token)
    except JWSError:
        raise exception

    if not email:
        raise exception

    user = RepositoryUsers(session).get_by_email(email)

    if not user:
        raise exception

    return user
