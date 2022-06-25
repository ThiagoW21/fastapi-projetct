from fastapi import APIRouter, status, HTTPException, Depends
from src.infra.sqlalchemy.repositories.users import RepositoryUsers
from src.schemas.schemas import User, UserSimple, LoginData, LoginSucess, Token
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.data_base import get_db
from src.infra.providers import hash_provider, token_provider
from src.routes.auth_utils import get_logged_in_user


router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserSimple)
def add_user(user: User, db: Session = Depends(get_db)):
    email_registered = RepositoryUsers(db).get_by_email(user.email)
    if email_registered:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email já registrado")

    user.password = hash_provider.generate_hash(user.password)
    user_create = RepositoryUsers(db).create(user)
    return user_create


@router.post('/token', response_model=LoginSucess)
def login(login_data: LoginData, db: Session = Depends(get_db)):
    password = login_data.password
    email = login_data.email

    user = RepositoryUsers(db).get_by_email(email)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email ou senha incorreto')

    password_valid = hash_provider.verify_hash(password, user.password)

    if not password_valid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email ou senha incorreto')

    token = token_provider.create_access_token({'sub': user.email})

    return LoginSucess(user=user, access_token=token)

# Deploy
@router.get('/me', response_model=UserSimple)
def me(token: Token = Depends(get_logged_in_user), db: Session = Depends(get_db)):
    return token
