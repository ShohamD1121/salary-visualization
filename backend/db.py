from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

ES_HOST = os.getenv("ES_HOST", "http://localhost:9200")
es = Elasticsearch(ES_HOST)
