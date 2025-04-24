check_between_numbers = lambda A, B, C: (A < B < C) or (A > B > C) # noqa E731

check_odd_three = lambda number: (100 <= abs(number) <= 999) and (number % 2 != 0) # noqa E731

check_unique_digits = lambda number: (100 <= abs(number) <= 999) and len(set(str(abs(number)))) == 3 # noqa E731


def check_palindrome_number(number): # noqa E731
    num_str = str(abs(number))
    return num_str == num_str[::-1]


check_ascending_digits = lambda number: (100 <= abs(number) <= 999) and \
(lambda d: d[0] < d[1] < d[2])([int(c) for c in str(abs(number))]) # noqa E731