from fastapi import FastAPI
from pydantic import BaseModel
import script
app = FastAPI()

class Item(BaseModel):
    number: str
    pwd: str


@app.post("/week")
def update_item(item: Item):
    num = item.number
    ps = item.pwd
    script.start(num, ps)

@app.post("/rest")
def update_item(item: Item):
    num = item.number
    ps = item.pwd
    script.start1(num, ps)
    