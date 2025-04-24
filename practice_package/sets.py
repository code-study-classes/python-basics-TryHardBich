# тесты ваще ещкере хайп свага лол сигма мем ржака хахич
def find_common_elements(set1, set2):
    return {item for item in set1 if item in set2}


def is_superset(set_a, set_b):
    return all(item in set_a for item in set_b)


def remove_duplicates(items):
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]


def count_unique_words(text):
    return len({word.lower() for word in text.split()})


def find_shared_items(*sets):
    if not sets:
        return set()
    shared = sets[0].copy()
    for s in sets[1:]:
        shared.intersection_update(s)
    return shared