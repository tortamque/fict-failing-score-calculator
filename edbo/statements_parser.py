from config.config import headers, speciality_ids
from classes.statement import Statement

import requests


def parse_all_statements(speciality_number: str):
    statements_json = []
    counter = 0

    while True:
        payload = {
            "id": speciality_ids[speciality_number],
            "last": counter
        }

        response = requests.post("https://vstup.edbo.gov.ua/offer-requests/", headers=headers, data=payload)
        response_json = response.json()

        if len(response_json["requests"]) == 0:
            break

        statements_json.extend(response_json["requests"])

        if counter == 1000:
            break

        counter += 200

    return statements_json


def check_kvota(statement):
    marks = statement["rss"]

    for mark in marks:
        if "sn" in mark:
            if mark["sn"] == "Квота 1":
                return 1
            elif mark["sn"] == "Квота 2":
                return 2

    return 0


def parse_statement_objects(statements_json):
    statements = []

    for statement in statements_json:
        kvota = check_kvota(statement)

        statement_obj = Statement(statement["fio"], statement["p"], statement["kv"], kvota)
        statements.append(statement_obj)

    return statements


def parse(speciality_number: str):
    statements_json = parse_all_statements(speciality_number)
    statements = parse_statement_objects(statements_json)

    return statements
