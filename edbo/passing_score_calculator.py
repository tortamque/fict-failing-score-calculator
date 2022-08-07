from classes.statement import Statement
from config.config import positions_count as positions_count_config


def get_kvota_only_statements(kvota: int, all_statements):
    statements_kvota = []

    for statement in all_statements:
        if statement.get_kvota() == kvota:
            statements_kvota.append(statement)

    sorted_statements = sorted(statements_kvota, key=lambda statement: statement.get_kb(), reverse=True)

    return sorted_statements


def calculate_last_person(priority: int, positions_count: int, statements):
    passing_score_statements = []

    for statement in statements:
        if statement.get_priority() <= priority and len(passing_score_statements) <= positions_count:
            passing_score_statements.append(statement)

    if len(passing_score_statements) > 1:
        last_person = passing_score_statements[-1]
        return last_person
    else:
        return Statement("-", "0", "0.0", 0)


def calculate_passing_score_person(priority: int, positions_count: int, statements, kvota: int):
    # если нет квоты, то рассматрияваем все заявления вместе
    if kvota == 0:
        # все заявления
        statements = sorted(statements, key=lambda statement: statement.get_kb(), reverse=True)
    else:
        # заявления только с квотами
        statements = get_kvota_only_statements(kvota, statements)

    last_person = calculate_last_person(priority, positions_count, statements)

    return last_person


def calculate(priority: int, speciality_number: str, statements):
    positions_count = positions_count_config[speciality_number]

    all = calculate_passing_score_person(priority, positions_count["default"], statements, 0)
    kvota1 = calculate_passing_score_person(priority, positions_count["kvota1"], statements, 1)
    kvota2 = calculate_passing_score_person(priority, positions_count["kvota2"], statements, 2)

    return all, kvota1, kvota2
