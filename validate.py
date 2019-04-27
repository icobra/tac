"""
validation of web password

len min 8 symbols

min 1 - number

min 1 - upper case

min 1 - low case

min 1 symbol not (number, upercase and low case)

"""
def numbers(you_password):
    z = 0
    for x in you_password:
        if x.isdigit():
            z += 1
    return z

def upper_case(you_password):
    z = 0
    for x in you_password:
        if x.isupper():
            z += 1
    return z

def lower_case(you_password):
    z = 0
    for x in you_password:
        if x.islower():
            z += 1
    return z

def other_symbols(you_password):
    count_numbers = numbers(you_password)
    count_upper = upper_case(you_password)
    count_lower = lower_case(you_password)
    new_len = count_numbers + count_upper + count_lower
    return new_len

def validator(you_password):
    you_password = str(you_password)

    if len(you_password) < 8:
        return "Your password must be at least 8 characters long."

    if numbers(you_password) <= 0:
        return "Your password must contain numbers."
    if upper_case(you_password) <= 0:
        return "Your password must contain capital letters."
    
    if lower_case(you_password) <= 0:
        return "Your password must contain lowercase letters."

    if other_symbols(you_password) == len(you_password):
        return "Your password must contain other characters."

    return you_password

def test():
    a = validator("Sword")
    b = validator(12345678)
    c = validator("Eskaliburus")
    d = validator("123DKLSDFGS")
    e = validator("123Eskaliburus")
    f = validator("123@Eskaliburus")

    print("Test word - Sword. Out - ", a)
    print("Test word - 12345678. Out -", b)
    print("Test word - Eskaliburus. Out -", c)
    print("Test word - 123DKLSDFGS. Out -", d)
    print("Test word - 123Eskaliburus. Out -", e)
    print("Test word - 123@Eskaliburus. Out -", f)

if __name__ == "__main__":
    test()        