
def square_odds(numbers):
    return [x**2 for x in numbers if x % 2 != 0]


def normalize_names(names):
    return [name.capitalize() for name in names]


def remove_invalid_emails(emails):
    return [email for email in emails 
            if email.count('@') == 1 
            and len(email) >= 5 
            and not email.startswith('@') 
            and not email.endswith('@')]


def filter_palindromes(words):
    return [word for word in words 
            if word.lower() == word.lower()[::-1]]


def calculate_factorial(n):
    from math import prod
    return prod(range(1, n + 1)) if n > 0 else 1


def find_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix