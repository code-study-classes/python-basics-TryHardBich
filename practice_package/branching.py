def is_weekend(day):
    return True if day in (6, 7) else False


def get_discount(amount):
    if amount >= 5000:
        return round(amount * 0.10, 2)
    elif amount >= 1000:
        return round(amount * 0.05, 2)
    else:
        return 0
    

def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    
    if n == 0:
        digit = "однозначное"
    elif 1 <= n <= 9:
        digit = "однозначное"
    elif 10 <= n <= 99:
        digit = "двузначное"
    else:
        digit = "трехзначное"
    
    return f"{parity} {digit} число"


def convert_to_meters(unitNumber, lengthInUnits):  # разраб линтера вонючка
    match unitNumber:
        case 1:
            return lengthInUnits * 0.1    # дц
        case 2:
            return lengthInUnits * 1000   # км
        case 3:
            return lengthInUnits * 1      # м
        case 4:
            return lengthInUnits * 0.001  # мм
        case 5:
            return lengthInUnits * 0.01   # см


def describe_age(age):
    tens = {
        2: "двадцать",
        3: "тридцать", 
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
        10: "сто"
    }
    
    units = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
    }
    
    if age % 10 == 0:
        word = "лет"
    elif 11 <= age % 100 <= 19:
        word = "лет"
    elif age % 10 == 1:
        word = "год"
    elif 2 <= age % 10 <= 4:
        word = "года"
    else:
        word = "лет"
    
    if age < 20:
        return f"{units[age]} {word}"
    elif age % 10 == 0:
        return f"{tens[age // 10]} {word}"
    else:
        return f"{tens[age // 10]} {units[age % 10]} {word}"