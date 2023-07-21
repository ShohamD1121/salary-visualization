import pymongo
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import pandas as pd

es = Elasticsearch("http://localhost:9200")

df = (
    pd.read_csv("wiki_movie_plots_deduped.csv")
    .dropna()
    .sample(5000, random_state=42)
    .reset_index()
)

mappings = {
    "properties": {
        "title": {"type": "text", "analyzer": "english"},
        "ethnicity": {"type": "text", "analyzer": "standard"},
        "director": {"type": "text", "analyzer": "standard"},
        "cast": {"type": "text", "analyzer": "standard"},
        "genre": {"type": "text", "analyzer": "standard"},
        "plot": {"type": "text", "analyzer": "english"},
        "year": {"type": "integer"},
        "wiki_page": {"type": "keyword"}
    }
}

# How to create an index with ElasticSearch
# es.indices.create(index="movies", mappings=mappings)

# How to place data in the index?
# bulk_data = []
# for i, row in df.iterrows():
#     bulk_data.append(
#         {
#             "_index": "movies",
#             "_id": i,
#             "_source": {
#                 "title": row["Title"],
#                 "ethnicity": row["Origin/Ethnicity"],
#                 "director": row["Director"],
#                 "cast": row["Cast"],
#                 "genre": row["Genre"],
#                 "plot": row["Plot"],
#                 "year": row["Release Year"],
#                 "wiki_page": row["Wiki Page"],
#             }
#         }
#     )
# bulk(es, bulk_data)

# es.indices.refresh(index="movies")
# es.cat.count(index="movies", format="json")


client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["data-db"]
salaries = db["Salaries"]
