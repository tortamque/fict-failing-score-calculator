from edbo.passing_score_calculator import calculate
from edbo.statements_parser import parse

from datetime import datetime


def get_result():
    statements_121 = parse(121)
    statements_123 = parse(123)
    statements_126 = parse(126)

    #1 приоритет
    all_121_1, kvota1_121_1, kvota2_121_1 = calculate(1, "121", statements_121)
    all_123_1, kvota1_123_1, kvota2_123_1 = calculate(1, "123", statements_123)
    all_126_1, kvota1_126_1, kvota2_126_1 = calculate(1, "126", statements_126)

    #1 и 2 приоритеты
    all_121_2, kvota1_121_2, kvota2_121_2 = calculate(2, "121", statements_121)
    all_123_2, kvota1_123_2, kvota2_123_2 = calculate(2, "123", statements_123)
    all_126_2, kvota1_126_2, kvota2_126_2 = calculate(2, "126", statements_126)

    result = f"""
    Непрохідні бали станом на {datetime.now().strftime("%d.%m.%y %H:%M")}
    
<b>Тільки перший пріоритет!</b>
121: 
    Всі вступники: {all_121_1}
    Тільки квота-1: {kvota1_121_1} 
    Тільки квота-2: {kvota2_121_1}
    
123:
    Всі вступники: {all_123_1}
    Тільки квота-1: {kvota1_123_1}
    Тільки квота-2: {kvota2_123_1}
    
126:
    Всі вступники: {all_126_1}
    Тільки квота-1: {kvota1_126_1}
    Тільки квота-2: {kvota2_126_1}
    
    
<b>Перший і другий пріоритети!</b>
121: 
    Всі вступники: {all_121_2}
    Тільки квота-1: {kvota1_121_2} 
    Тільки квота-2: {kvota2_121_2}
    
123:
    Всі вступники: {all_123_2}
    Тільки квота-1: {kvota1_123_2}
    Тільки квота-2: {kvota2_123_2}
    
126:
    Всі вступники: {all_126_2}
    Тільки квота-1: {kvota1_126_2}
    Тільки квота-2: {kvota2_126_2}"""

    return result


def get_result_121():
    statements_121 = parse(121)

    # 1 приоритет
    all_121_1, kvota1_121_1, kvota2_121_1 = calculate(1, "121", statements_121)

    # 1 и 2 приоритеты
    all_121_2, kvota1_121_2, kvota2_121_2 = calculate(2, "121", statements_121)

    result = f"""
Інформація про <b>121</b> спеціальність

Непрохідні бали станом на {datetime.now().strftime("%d.%m.%y %H:%M")}

<b>Тільки перший пріоритет!</b>
    Всі вступники: {all_121_1}
    Тільки квота-1: {kvota1_121_1} 
    Тільки квота-2: {kvota2_121_1}

<b>Перший і другий пріоритети!</b>
    Всі вступники: {all_121_2}
    Тільки квота-1: {kvota1_121_2} 
    Тільки квота-2: {kvota2_121_2}"""

    return result


def get_result_123():
    statements_123 = parse(123)

    # 1 приоритет
    all_123_1, kvota1_123_1, kvota2_123_1 = calculate(1, "123", statements_123)

    # 1 и 2 приоритеты
    all_123_2, kvota1_123_2, kvota2_123_2 = calculate(2, "123", statements_123)

    result = f"""
Інформація про <b>123</b> спеціальність

Непрохідні бали станом на {datetime.now().strftime("%d.%m.%y %H:%M")}

<b>Тільки перший пріоритет!</b>
    Всі вступники: {all_123_1}
    Тільки квота-1: {kvota1_123_1}
    Тільки квота-2: {kvota2_123_1}


<b>Перший і другий пріоритети!</b>
    Всі вступники: {all_123_2}
    Тільки квота-1: {kvota1_123_2}
    Тільки квота-2: {kvota2_123_2}"""

    return result


def get_result_126():
    statements_126 = parse(126)

    # 1 приоритет
    all_126_1, kvota1_126_1, kvota2_126_1 = calculate(1, "126", statements_126)

    # 1 и 2 приоритеты
    all_126_2, kvota1_126_2, kvota2_126_2 = calculate(2, "126", statements_126)

    result = f"""
Інформація про <b>126</b> спеціальність
    
Непрохідні бали станом на {datetime.now().strftime("%d.%m.%y %H:%M")}

<b>Тільки перший пріоритет!</b>
    Всі вступники: {all_126_1}
    Тільки квота-1: {kvota1_126_1}
    Тільки квота-2: {kvota2_126_1}


<b>Перший і другий пріоритети!</b>
    Всі вступники: {all_126_2}
    Тільки квота-1: {kvota1_126_2}
    Тільки квота-2: {kvota2_126_2}"""

    return result
