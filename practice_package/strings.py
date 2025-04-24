def extract_file_name(full_file_name):
    filename = full_file_name.split('/')[-1]
    if filename.startswith('.'):
        return filename
    parts = filename.split('.', 1)
    return parts[0] if len(parts) > 1 else filename


def encrypt_sentence(sentence):
    even_chars = []
    odd_chars = []
    for i, char in enumerate(sentence):
        if i % 2 == 1:
            even_chars.append(char)
        else:
            odd_chars.append(char)
    return ''.join(even_chars + odd_chars[::-1])


def check_brackets(expression):
    openNum = 0
    closeNum = 0
    pos = 0
    for i in range(0, len(expression)):
        if expression[i] != ' ':
            pos += 1
        if expression[i] == '(':
            openNum += 1
        elif expression[i] == ')':
            closeNum += 1
        if closeNum > openNum:
            return pos
    if openNum > closeNum:
        return -1
    return 0


def reverse_domain(domain):
    parts = domain.split('.')
    return '.'.join(reversed(parts))


def count_vowel_groups(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    in_vowel_group = False
    for char in word.lower():
        if char in vowels:
            if not in_vowel_group:
                count += 1
                in_vowel_group = True
        else:
            in_vowel_group = False
    return count
# тесты 10 из 10, ставлю лайк, мне понравилось :D