from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette.responses import HTMLResponse
from pydantic import BaseModel
import random
import json

app = FastAPI()

items = {}
indexHTML = ''

class WeirdThing(BaseModel):
    id: int
    name: str
    description: str

class WeirdThingIn(BaseModel):
    name: str
    description: str

def update_db():
    global items
    with open('weird.db', mode='w') as file:
        file.write(json.dumps(jsonable_encoder(items)))

@app.on_event('startup')
def startup():
    global indexHTML
    global items

    with open('index.html') as file:
        indexHTML = file.read()
    
    try:
        with open('weird.db') as file:
            items = json.loads(file.read())
    except FileNotFoundError:
        print('No weird database, creating...')

        with open('weird.db') as file:
            items = json.loads(file.read())
    
    print(f'Loaded items')

@app.on_event('shutdown')
def shutdown():
    update_db()    

@app.get("/", response_class=HTMLResponse)
async def root():
    if len(items) > 0:
        return indexHTML.replace('PUTITRIGHTHEREPYTHON', random.choice(items.values()))
    else:
        return indexHTML.replace('PUTITRIGHTHEREPYTHON', 'There are no things in the database! So weird!')


@app.get("/weird/{item_id}", response_model=WeirdThing)
async def get_weird(item_id: int):
    if str(item_id) in items.keys():
        return items[str(item_id)]
    else:
        raise HTTPException(status_code=404, detail='Item not in database')

@app.get("/weird", response_model=WeirdThing)
async def get_random_weird():
    if len(items) > 0:
        return random.choice(items.values())
    else:
        raise HTTPException(status_code=404, detail='No items in database')

@app.post("/add", response_model=WeirdThing)
async def post_weird(item: WeirdThingIn):
    global items

    newId = random.randrange(0, 1_000_000)
    while newId in items.keys():
        newId = random.randrange(0, 1_000_000)
    
    items[str(newId)] = WeirdThing(id=newId, **item.dict())

    update_db()

    return items[newId]