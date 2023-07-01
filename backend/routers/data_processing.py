from fastapi import APIRouter
from utils.data_processing import create_bins, calculate_average_salary
from db import salaries

router = APIRouter()


@router.get("/remote-ratios")
def get_remote_ratios():
    result = salaries.find()
    remote_ratios = [doc["remote_ratio"] for doc in result]
    remote_ratios_json = create_bins(remote_ratios)
    return remote_ratios_json


@router.get("/salaries-average")
def get_remote_ratios():
    data = salaries.find()
    return calculate_average_salary(data)
