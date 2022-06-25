from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositoryContribuitors:
    def __init__(self, db: Session):
        self.db = db

    def create(self, colaborattor: schemas.Collaborator):
        db_colaborattor = models.Colaborattor(full_name=colaborattor.full_name,
                                              gender=colaborattor.gender,
                                              tel=colaborattor.tel,
                                              email=colaborattor.email,
                                              office=colaborattor.office,
                                              cep=colaborattor.cep,
                                              city=colaborattor.city,
                                              state=colaborattor.state,
                                              public_place=colaborattor.public_place,
                                              number=colaborattor.number,
                                              complement=colaborattor.complement,
                                              district=colaborattor.district,
                                              data_nasc=colaborattor.data_nasc,
                                              reference_point=colaborattor.reference_point
                                              )
        self.db.add(db_colaborattor)
        self.db.commit()
        self.db.refresh(db_colaborattor)
        return db_colaborattor

    def list(self):
        colaborattor = self.db.query(models.Colaborattor).all()
        return colaborattor

    def get(self, colaborattor_id: int):
        statement = select(models.Colaborattor).filter_by(id=colaborattor_id)
        colaborattor = self.db.execute(statement).one()

        return colaborattor

    def delete(self, colaborattor_id: int):
        statement = delete(models.Colaborattor).where(models.Colaborattor.id == colaborattor_id)
        self.db.execute(statement)
        self.db.commit()

    def update(self, id_colab: int, colaborattor: schemas.Collaborator):
        update_stmt = update(models.Colaborattor).where(
            models.Colaborattor.id == id_colab).values(full_name=colaborattor.full_name, gender=colaborattor.gender,
                                                       tel=colaborattor.tel, email=colaborattor.email,
                                                       office=colaborattor.office, cep=colaborattor.cep,
                                                       city=colaborattor.city, state=colaborattor.state,
                                                       public_place=colaborattor.public_place,
                                                       number=colaborattor.number,
                                                       complement=colaborattor.complement,
                                                       )
        self.db.execute(update_stmt)
        self.db.commit()
