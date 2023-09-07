
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    if item_id > 1:
        return{f"Вы перешли куда-то не туда по id: {item_id}, попробуйте использовать id 1"}
    else:
        result = item_id + item_id
    return {"Результат сложения айди": result}