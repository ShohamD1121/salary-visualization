from fastapi import APIRouter
from db import es
from repositories.salary_repository import SalaryRepository
import requests

router = APIRouter()
index_name = "salaries"
base_url = "http://localhost:9200"
salary_repository = SalaryRepository(es_client=es)


@router.get("/remote-ratios")
def get_remote_ratios():
    remote_ratios = salary_repository.get_remote_ratios()
    return remote_ratios


@router.get("/average-salary-by-company-size")
def get_average_salary_by_company_size():
    salary_data = salary_repository.get_average_salary_by_company_size()
    return salary_data


@router.get("/average-salary-by-experience-level")
def get_average_salary_by_experience():
    return salary_repository.get_average_salary_by_experience()
