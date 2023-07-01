from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymongo
from utils.data_processing import create_bins, calculate_average_salary

# for app starting ---> python -m uvicorn main:app --reload

app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["data-db"]
collection = db["Salaries"]


@app.get("/remote-ratios")
def get_remote_ratios():
    result = collection.find()
    remote_ratios = [doc["remote_ratio"] for doc in result]
    remote_ratios_json = create_bins(remote_ratios)
    return remote_ratios_json


@app.get("/salaries-average")
def get_remote_ratios():
    data = collection.find()
    return calculate_average_salary(data)
