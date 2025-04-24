# Задача 1
def count_char_occurrences(text):
    from collections import defaultdict
    counts = defaultdict(int)
    for char in text.lower():
        if char.isalpha():
            counts[char] += 1
    return dict(counts)


# Задача 2
def merge_dicts(dict1, dict2, conflict_resolver):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = conflict_resolver(key, result[key], value)
        else:
            result[key] = value
    return result


# Задача 3
def invert_dictionary(original_dict):
    inverted = {}
    for key, value in original_dict.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)
    return inverted


# Задача 4
def dict_to_table(data_dict, columns):
    # Подготовка данных
    rows = []
    columns = [col.upper() for col in columns]
    
    # Сбор всех строк и определение максимальных длин
    max_lengths = {col: len(col) for col in columns}
    for item in data_dict.values():
        row = []
        for col in columns:
            value = str(item.get(col.lower(), 'N/A'))
            row.append(value)
            max_lengths[col] = max(max_lengths[col], len(value))
        rows.append(row)
    
    # Форматирование заголовка
    header = "|" + "|".join(
        f" {col.ljust(max_lengths[col])} " for col in columns
    ) + "|"
    
    # Форматирование разделителя
    separator = "|" + "|".join(
        "-" * (max_lengths[col] + 2) for col in columns
    ) + "|"
    
    # Форматирование строк
    formatted_rows = []
    for row in rows:
        formatted_row = "|" + "|".join(
            f" {value.ljust(max_lengths[col])} " 
            for col, value in zip(columns, row)
        ) + "|"
        formatted_rows.append(formatted_row)
    
    # Сборка итоговой таблицы
    return "\n".join([header, separator] + formatted_rows)


# Задача 5
def deep_update(base_dict, update_dict):
    result = base_dict.copy()
    for key, value in update_dict.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = deep_update(result[key], value)
            else:
                result[key] = value
    return result