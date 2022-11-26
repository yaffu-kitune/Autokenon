from fastapi import FastAPI
from pydantic import BaseModel
import script
app = FastAPI()

class Item(BaseModel):
    number: str
    pwd: str
    switch : str


@app.post("/week")
def update_item(item: Item):
    num = item.number
    ps = item.pwd
    week = item.switch
    script.start(num, ps, week)