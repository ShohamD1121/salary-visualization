from fastapi import APIRouter
from db import es
from repositories.salary_repository import SalaryRepository
from services.salary_service import SalaryService
import requests

router = APIRouter()
index_name = "salaries"
base_url = "http://localhost:9200"
salary_repository = SalaryRepository(es_client=es)
salary_service = SalaryService()


@router.get("/remote-ratios")
def get_remote_ratios():
    remote_ratios = salary_repository.get_remote_ratios(
        index_name=index_name)
    return remote_ratios


@router.get("/average-salary-by-company-size")
def get_average_salary_by_company_size(size: int = 3755):
    salary_data = salary_repository.get_average_salary_by_company_size(
        index_name=index_name, size=size)
    return salary_service.calculate_average_salary_by_company_size(salary_data)


@router.get("/average-salary-by-experience-level")
def get_average_salary_by_experience(size: int = 3755):
    salary_data = salary_repository.get_average_salary_by_experience(
        index_name=index_name, size=size)
    return salary_service.calculate_average_salary_by_experience(salary_data)


@router.get("/search")
# This will be Search by something Endpoint...
def search_documents():
    # Define the fields you want to include in the search results
    source_fields = ["job_title", "experience_level", "salary_in_usd"]

    # Test Here! check who's faster
    slow_search_query = {
        "_source": source_fields,
        "query": {
            "match_all": {}
        },
        "size": 3755
    }

    # Execute the search request to retrieve the specified fields from all documents in the index
    result = es.search(index=index_name, body=slow_search_query)

    return result["hits"]["hits"]


@router.get("/index_stats")
def get_index_stats():
    url = f"{base_url}/{index_name}/_stats"

    try:
        response = requests.get(url)
        response.raise_for_status()
        index_stats = response.json()
        return index_stats
    except requests.exceptions.RequestException as e:
        return {"error": f"Error while fetching index stats: {e}"}


@router.get("/data-db/_count")
def get_index_count():
    url = f"{base_url}/{index_name}/_count"

    try:
        response = requests.get(url)
        response.raise_for_status()
        index_count = response.json()
        return index_count
    except requests.exceptions.RequestException as e:
        return {"error": f"Error while fetching index count: {e}"}
