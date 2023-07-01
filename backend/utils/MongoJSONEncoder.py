import json
from datetime import datetime
from typing import Any
from bson import ObjectId

# Incase objectId is needed to be returned to the client with json format
class MongoJSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)
