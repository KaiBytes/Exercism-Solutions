def convert(number):
    factor3 = Pling
    factor5 = Plang
    factor7 = Plong
    if number % 3 == 0:
        return factor3
    elif number % 5 == 0:
        return factor5
    elif number % 7 == 0:
        return factor7
    else:
        return number
