from flask import Flask, request, jsonify

app = Flask(__name__)


fields = [
    {"id": 1, "name": "Civil and Environmental Engineering"},
    {"id": 2, "name": "Applied Natural Sciences"},
    {"id": 3, "name": "Healthcare Sciences"},
    {"id": 4, "name": "Informatics"},
    {"id": 5, "name": "Design and Media"},
    {"id": 6, "name": "Electrical Engineering and Information Technology"},
    {"id": 7, "name": "Mechanical Engineering and Mechatronics"},
    {"id": 8, "name": "Economics"},
    {"id": 9, "name": "Extra-occupational Degrees"}
]


def _find_next_id():
    return max(i["id"] for i in fields) + 1


@app.get("/fields")
def get_fields():
    return jsonify(fields)


@app.post("/fields")
def add_field():

    if request.is_json:
        field = request.get_json()
        field["id"] = _find_next_id()
        fields.append(field)
        return field, 201
    return {"error": "Request must be JSON"}, 415
