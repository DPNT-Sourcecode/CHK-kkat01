

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    validate_input = ['A','B','C','D']
    validate_data = [{'item': 'A', 'price': 50, 'special_offer': '3A', 'special_price': 130},
                     {'item': 'B', 'price': 30, 'special_offer': '2B', 'special_price': 45},
                     {'item': 'C', 'price': 20, 'special_offer': '', 'special_price': 0},
                     {'item': 'D', 'price': 15, 'special_offer': '', 'special_price': 0}]

    tmp_price = 0
    A_counter = 0
    B_counter = 0

    if skus == '':
        return tmp_price

    skus_list = list(skus)


    for SKU in skus_list:
        if SKU not in validate_input:
            continue

        if SKU == 'A':
            if A_counter < 3:
                A_counter += 1
                tmp_price += validate_data[0]['price']
            elif A_counter >= 3:
                A_counter = 0
                tmp_price -= 2*(validate_data[0]['price'])
                tmp_price += validate_data[0]['special_price']
        elif SKU == 'B':
            if B_counter < 2:
                B_counter += 1
                tmp_price += validate_data[1]['price']
            elif B_counter >= 2:
                B_counter = 0
                tmp_price -= validate_data[1]['price']
                tmp_price += validate_data[1]['special_price']
        elif SKU == 'C':
            tmp_price += validate_data[2]['price']
        elif SKU == 'D':
            tmp_price += validate_data[3]['price']

    return tmp_price






