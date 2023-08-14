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

    def get_remote_ratios(self, index_name: str):
        query = {
            "size": 0,
            "aggs": {
                "equal_remote_ratios": {
                    "terms": {
                        "field": "remote_ratio",
                        "size": 10,
                        "include": [0, 50, 100],
                        "order": {
                            "_key": "asc"
                        },
                    },
                    "aggs": {
                        "doc_count": {
                            "value_count": {
                                "field": "remote_ratio"
                            }
                        }
                    }
                }
            }
        }
        result = self.es_client.search(index=index_name, body=query)
        remote_ratios = [
            {
                "remote_ratio": bucket["key"],
                "count": bucket["doc_count"]["value"]
            }
            for bucket in result["aggregations"]["equal_remote_ratios"]["buckets"]
        ]
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
