def sum(number1, number2):
    if not isinstance(number1, int):
        return
    if not isinstance(number2, int):
        return

    if number1 < 0 or number1 > 100:
        return
    if number2 < 0 or number2 > 100:
        return

    return(number1+number2)