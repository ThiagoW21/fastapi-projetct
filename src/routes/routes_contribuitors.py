from fastapi import APIRouter, status, HTTPException, Depends
from src.infra.sqlalchemy.repositories.contribuitors import RepositoryContribuitors
from src.schemas.schemas import Collaborator
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.data_base import get_db
from typing import List


router = APIRouter()


@router.get("/contributors", status_code=status.HTTP_200_OK, response_model=List[Collaborator])
def list_contribuitors(db: Session = Depends(get_db)):
    contribuitors = RepositoryContribuitors(db).list()
    return contribuitors


@router.get("/contributors/{id_colaborattor}", status_code=status.HTTP_200_OK)
def get_colaborattor(id_colaborattor: int, db: Session = Depends(get_db)):
    try:
        colaborattor = RepositoryContribuitors(db).get(id_colaborattor)
        return colaborattor
    except Exception:
        raise HTTPException(status_code=404, detail="Colaborator not found")


@router.post("/contributors", status_code=status.HTTP_201_CREATED, response_model=Collaborator)
def add_colaborattor(colaborattor: Collaborator, db: Session = Depends(get_db)):
    colaborattor_create = RepositoryContribuitors(db).create(colaborattor)
    return colaborattor_create


@router.put("/contributors/{id_colab}", status_code=status.HTTP_204_NO_CONTENT)
def update_colaborattor(id_colab: int, colaborattor: Collaborator, db: Session = Depends(get_db)):
    RepositoryContribuitors(db).update(id_colab, colaborattor)
    colaborattor.id = id_colab
    return colaborattor


@router.delete("/contributors/{id_colaborattor}", status_code=status.HTTP_204_NO_CONTENT)
def delete_colaborattor(id_colaborattor: int, db: Session = Depends(get_db)):
    RepositoryContribuitors(db).delete(id_colaborattor)