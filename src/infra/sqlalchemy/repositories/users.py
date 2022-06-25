from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositoryUsers:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: schemas.User):
        db_user = models.User(username=user.username,
                              email=user.email,
                              password=user.password
                              )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_by_email(self, email) -> models.User:
        query = select(models.User).where(models.User.email == email)
        return self.db.execute(query).scalars().first()
