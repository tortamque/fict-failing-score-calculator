from classes.statement import Statement
from config.config import positions_count as positions_count_config


def get_not_kvota_only_statements(all_statements, speciality_number: str):
    kvota1_positions_count = positions_count_config[speciality_number]["kvota1"]
    kvota2_positions_count = positions_count_config[speciality_number]["kvota2"]

    statements_kvota1, statements_kvota2, statements_all = [], [], []

    kvota1_counter, kvota2_counter = 0, 0

    for statement in all_statements:
        if statement.get_kvota() == 1 and kvota1_counter <= kvota1_positions_count:
            statements_kvota1.append(statement)
            kvota1_counter += 1
        elif statement.get_kvota() == 2 and kvota2_counter <= kvota2_positions_count:
            statements_kvota2.append(statement)
            kvota2_counter += 1
        elif statement.get_kvota() == 0 or (statement.get_kvota() == 1 and kvota1_counter > kvota1_positions_count) or (statement.get_kvota() == 2 and kvota2_counter > kvota2_positions_count):
            statements_all.append(statement)

    statements_all = sorted(statements_all, key=lambda _statement: _statement.get_kb(), reverse=True)

    for i in statements_all:
        print(i)

    return statements_all


def get_kvota_only_statements(kvota: int, all_statements):
    statements_kvota = []

    for statement in all_statements:
        if statement.get_kvota() == kvota:
            statements_kvota.append(statement)

    sorted_statements = sorted(statements_kvota, key=lambda _statement: _statement.get_kb(), reverse=True)

    return sorted_statements


def cut_reduntant_priority(priority: int, statements):
    clipped_statements = []

    for statement in statements:
        if priority >= statement.get_priority() >= 1:
            clipped_statements.append(statement)

    return clipped_statements


def calculate_last_person(priority: int, positions_count: int, statements):
    clipped_statements = cut_reduntant_priority(priority, statements)

    if len(clipped_statements) >= positions_count:
        last_person = clipped_statements[positions_count-1]

        return last_person
    elif len(clipped_statements) == 0:
        return Statement("-", "0", "0.0", 0)
    else:
        last_person = clipped_statements[-1]

        return last_person


def calculate_passing_score_person(priority: int, positions_count: int, statements, kvota: int, speciality_number: str):
    # если нет квоты, то рассматрияваем все заявления вместе
    if kvota == 0:
        # все заявления
        statements_sorted = sorted(statements, key=lambda _statement: _statement.get_kb(), reverse=True)

        statements = get_not_kvota_only_statements(statements_sorted, speciality_number)
    else:
        # заявления только с квотами
        statements = get_kvota_only_statements(kvota, statements)

    last_person = calculate_last_person(priority, positions_count, statements)

    return last_person


def calculate(priority: int, speciality_number: str, statements):
    positions_count = positions_count_config[speciality_number]

    all = calculate_passing_score_person(priority, positions_count["default"], statements, 0, speciality_number)
    kvota1 = calculate_passing_score_person(priority, positions_count["kvota1"], statements, 1, speciality_number)
    kvota2 = calculate_passing_score_person(priority, positions_count["kvota2"], statements, 2, speciality_number)

    return all, kvota1, kvota2
