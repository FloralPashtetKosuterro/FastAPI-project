from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, crud

from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/clients/{client_id}", response_model=schemas.Clients)
def read_clients(client_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_client(db, client_id = client_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Не найден ваш клиент, другого ищите.")
    return db_user


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id > 1:
        return {f"Вы перешли куда-то не туда по id: {item_id}, попробуйте использовать id 1"}
    else:
        result = item_id + item_id
    return {"Результат сложения айди": result}
