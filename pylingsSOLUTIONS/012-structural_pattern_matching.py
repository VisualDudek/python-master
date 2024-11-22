# capture value of key "statuscode" and "id"
# from following json_string
import json


json_string = """
{
    "status": "OK",
    "statuscode": 200,
    "message": "success",
    "apps": [
        {
            "id": "675832210",
            "title": "AGED"
        }
    ]
}
"""

match json.loads(json_string):
    case {"statuscode": statuscode, "apps": [{"id": id}]}:
        print(f"{statuscode=}, {id=}")
    case _:
        raise ValueError("Unsupported JSON structure")
