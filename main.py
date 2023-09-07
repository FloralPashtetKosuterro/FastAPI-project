
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    if item_id == "2":
        return{"Вы перешли куда-то не туда"}
    else:
        result = int(item_id + item_id)
    return {"Результат сложения айди по джаваскрипту :^)": result}