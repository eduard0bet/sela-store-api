from ctypes import Union
import os
from multiprocessing.connection import Client
from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

url = os.getenv('SUPABASE_SUPAFAST_URL')
key = os.getenv('SUPABASE_SUPAFAST_KEY')
supabase: Client = create_client(url, key)


@app.get("/")
async def root():
    return {"hello there!"}


@app.get("/api/v1/store/all")
async def stores():
    stores = supabase.table(os.getenv('STORES_TABLE')).select('*').execute()
    return stores


@app.get("/api/v1/store")
async def getstores(id):
    getstores = supabase.table(os.getenv('STORES_TABLE')).select('*').eq('siteid', id).execute()
    resp = {
        "status": getstores.data[0]["status"],
        "countryCode": getstores.data[0]["country"],
        "id": getstores.data[0]["siteid"],
        "customer": getstores.data[0]["account"],
        "marketingName": getstores.data[0]["mso_name"],
        "gscmName": getstores.data[0]["site_name"],
        "lat": getstores.data[0]["latitude"],
        "long": getstores.data[0]["longitude"],
    }
    print(resp)
    return resp
