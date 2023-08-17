from elasticsearch import Elasticsearch
import utils.queries as queries


class SalaryRepository:
    def __init__(self, es_client: Elasticsearch):
        self.es_client = es_client
        self.index_name = "salaries_v2"

    def get_remote_ratios(self):
        result = self.es_client.search(
            index=self.index_name, body=queries.get_remote_ratios_query)
        remote_ratios = [
            {
                "remote_ratio": bucket["key"],
                "count": bucket["doc_count"]["value"]
            }
            for bucket in result["aggregations"]["equal_remote_ratios"]["buckets"]
        ]
        return remote_ratios

    def get_average_salary_by_company_size(self):

        result = self.es_client.search(
            index=self.index_name, body=queries.get_average_salary_by_company_size_query)
        formatted_result = []

        for job_bucket in result["aggregations"]["job_titles"]["buckets"]:
            formatted_entry = {"job_title": job_bucket["key"]}
            for size_bucket in job_bucket["company_sizes"]["buckets"]:
                formatted_entry[f"average_salary_{size_bucket['key']}"] = int(
                    size_bucket["average_salary"]["value"])
            formatted_result.append(formatted_entry)

        return formatted_result

    def get_average_salary_by_experience(self):
        result = self.es_client.search(
            index=self.index_name, body=queries.get_average_salary_by_experience_query)
        formatted_result = []

        for job_bucket in result["aggregations"]["job_titles"]["buckets"]:
            formatted_entry = {"job_title": job_bucket["key"]}
            for size_bucket in job_bucket["experience_levels"]["buckets"]:
                formatted_entry[f"average_salary_{size_bucket['key']}"] = int(
                    size_bucket["average_salary"]["value"])
            formatted_result.append(formatted_entry)

        return formatted_result
