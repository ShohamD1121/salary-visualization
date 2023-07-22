from fastapi import APIRouter
from utils.data_processing import create_bins, calculate_average_salary_by_company_size, calculate_average_salary_by_experience
from db import es
import requests

router = APIRouter()
index_name = "salaries"
base_url = "http://localhost:9200"


@router.get("/remote-ratios")
def get_remote_ratios():
    search_query = {
        "_source": ["remote_ratio"],
        "size": 3755
    }

    result = es.search(index=index_name, body=search_query)

    # Extract the "remote_ratio" field from each document in the search results
    remote_ratios = [doc["_source"]["remote_ratio"]
                     for doc in result["hits"]["hits"]]

    remote_ratios_json = create_bins(remote_ratios)
    return remote_ratios_json


@router.get("/average-salary-by-company-size")
def get_remote_ratios():
    search_query = {
        "query": {
            "match_all": {}
        },
        "size": 3755
    }

    # Execute the search request to retrieve all documents in the index
    result = es.search(index=index_name, body=search_query)

    # Extract the "hits" from the search result, which contains all documents
    all_documents = result["hits"]["hits"]
    return calculate_average_salary_by_company_size(all_documents)


@router.get("/average-salary-by-experience-level")
def get_average_salary_by_experience():

    search_query = {
        "query": {
            "match_all": {}
        },
        "size": 3755
    }

    # Execute the search request to retrieve all documents in the index
    result = es.search(index=index_name, body=search_query)

    # Extract the "hits" from the search result, which contains all documents
    all_documents = result["hits"]["hits"]
    return calculate_average_salary_by_experience(all_documents)


@router.get("/search")
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

    # Test Here! check who's faster
    fast_search_query = {
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
