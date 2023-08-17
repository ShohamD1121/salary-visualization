get_remote_ratios_query = {
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

get_average_salary_by_company_size_query = {
    "size": 0,
    "aggs": {
        "job_titles": {
            "terms": {
                "field": "job_title",
                "size": 93,
                "order": {
                    "_key": "asc"
                }
            },
            "aggs": {
                "company_sizes": {
                    "terms": {
                        "field": "company_size",
                        "order": {
                            "_key": "asc"
                        }
                    },
                    "aggs": {
                        "average_salary": {
                            "avg": {
                                "field": "salary_in_usd"
                            }
                        }
                    }
                }
            }
        }
    }
}

get_average_salary_by_experience_query = {
    "size": 0,
    "aggs": {
        "job_titles": {
            "terms": {
                "field": "job_title",
                "size": 93,
                "order": {
                    "_key": "asc"
                }
            },
            "aggs": {
                "experience_levels": {
                    "terms": {
                        "field": "experience_level",
                        "order": {
                            "_key": "asc"
                        }
                    },
                    "aggs": {
                        "average_salary": {
                            "avg": {
                                "field": "salary_in_usd"
                            }
                        }
                    }
                }
            }
        }
    }
}
