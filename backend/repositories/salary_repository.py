from elasticsearch import Elasticsearch
from dataclasses import dataclass
from typing import Optional


@dataclass
class SalaryData:
    job_title: str
    salary: int
    company_size: Optional[str] = None
    experience_level: Optional[str] = None


class SalaryRepository:
    def __init__(self, es_client: Elasticsearch):
        self.es_client = es_client

    def get_remote_ratios(self, index_name: str, size: int):
        search_query = {
            "_source": ["remote_ratio"],
            "size": size
        }

        result = self.es_client.search(index=index_name, body=search_query)
        remote_ratios = [doc["_source"]["remote_ratio"]
                         for doc in result["hits"]["hits"]]

        return remote_ratios

    def get_average_salary_by_company_size(self, index_name: str, size: int):
        search_query = {
            "query": {
                "match_all": {}
            },
            "size": size
        }

        result = self.es_client.search(index=index_name, body=search_query)
        all_documents = result["hits"]["hits"]
        salary_data_list = [SalaryData(
            job_title=doc["_source"]["job_title"],
            company_size=doc["_source"]["company_size"],
            salary=doc["_source"]["salary_in_usd"]
        ) for doc in all_documents]

        return salary_data_list

    def get_average_salary_by_experience(self, index_name: str, size: int):
        search_query = {
            "query": {
                "match_all": {}
            },
            "size": size
        }

        result = self.es_client.search(index=index_name, body=search_query)
        all_documents = result["hits"]["hits"]
        salary_data_list = [SalaryData(
            job_title=doc["_source"]["job_title"],
            experience_level=doc["_source"]["experience_level"],
            salary=doc["_source"]["salary_in_usd"]
        ) for doc in all_documents]

        return salary_data_list
