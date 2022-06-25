from fastapi import APIRouter, status, HTTPException, Depends
from src.infra.sqlalchemy.repositories.items import RepositoryItems
from src.schemas.schemas import Item
from sqlalchemy.orm import Session
from typing import List
from src.infra.sqlalchemy.config.data_base import get_db


ITEM_NOT_FOUND = HTTPException(status_code=404, detail="Item not found")

router = APIRouter()


@router.get("/items", status_code=status.HTTP_200_OK, response_model=List[Item])
def list_items(db: Session = Depends(get_db)):
    items = RepositoryItems(db).list()
    return items


@router.delete("/items/{id_item}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    RepositoryItems(db).delete(item_id)


@router.put("/items/{id_item}", status_code=status.HTTP_204_NO_CONTENT)
def update_item(id_item: int, item: Item, db: Session = Depends(get_db)):
    RepositoryItems(db).update(id_item, item)
    item.id = id_item
    return item


@router.post("/items", status_code=status.HTTP_201_CREATED, response_model=Item)
def add_item(item: Item, db: Session = Depends(get_db)):
    item_create = RepositoryItems(db).create(item)
    return item_create


@router.get("/items/{id_item}", status_code=status.HTTP_200_OK)
def get_item(id_item: int, db: Session = Depends(get_db)):
    try:
        item = RepositoryItems(db).get(id_item)
        return item
    except Exception:
        raise ITEM_NOT_FOUND