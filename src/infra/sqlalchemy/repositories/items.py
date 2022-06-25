from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositoryItems:
    def __init__(self, db: Session):
        self.db = db

    def create(self, item: schemas.Item):
        db_item = models.Item(code=item.code,
                              title=item.title,
                              category=item.category,
                              url_image=item.url_image,
                              brand=item.brand,
                              model=item.model,
                              description=item.description,
                              borrowed_to=item.borrowed_to,
                              price=item.price
                              )
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def list(self):
        itens = self.db.query(models.Item).all()
        return itens

    def get(self, item_id: int):
        statement = select(models.Item).filter_by(id=item_id)
        item = self.db.execute(statement).one()

        return item

    def delete(self, item_id: int):
        statement = delete(models.Item).where(models.Item.id == item_id)
        self.db.execute(statement)
        self.db.commit()

    # deploy
    def update(self, id_item: int, item: schemas.Item):
        update_stmt = update(models.Item).where(
            models.Item.id == id_item).values(code=item.code,
                                              title=item.title,
                                              category=item.category,
                                              url_image=item.url_image,
                                              brand=item.brand,
                                              model=item.model,
                                              description=item.description,
                                              borrowed_to=item.borrowed_to,
                                              price=item.price)

        self.db.execute(update_stmt)
        self.db.commit()
