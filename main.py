from fastapi import FastAPI
from datetime import datetime
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "kiki"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

#query parameter
@app.get("/raspberry")
async def read_item(time:str = datetime.now().strftime("%Y%m%d %H:%M:%S"),light: float = 0.0, temperature: float = 0.0):
    
    return {
        "時間":time,
        "光線":light,
        "溫度":temperature
    }