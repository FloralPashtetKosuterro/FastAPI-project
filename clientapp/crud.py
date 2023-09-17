from sqlalchemy.orm import Session

from . import models, schemas


def get_client(db: Session, user_id: int):
    return db.query(models.Clients).filter(models.Clients.id == user_id).first()


def create_clients(db: Session, client: schemas.ClientsCreate):
    fake_hashed_password = client.surname + "notreallyhashed"
    db_user = models.Clients(name=client.name, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
