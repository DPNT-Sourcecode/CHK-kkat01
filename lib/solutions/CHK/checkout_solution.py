

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    validate_input = ['A','B','C','D']
    validate_data = [{'item': 'A', 'price': 50, 'special_offer': '3A', 'special_price': 130},
                     {'item': 'B', 'price': 30, 'special_offer': '2B', 'special_price': 45},
                     {'item': 'C', 'price': 20, 'special_offer': '', 'special_price': 0},
                     {'item': 'D', 'price': 15, 'special_offer': '', 'special_price': 0}]

    if not isinstance(skus, str):
        return -1

    skus_list = list(skus)

    tmp_price = 0
    A_counter = 0
    B_counter = 0

    for SKU in skus_list:
        if SKU not in validate_input:
            return -1

        for entry in validate_data:
            if SKU == 'A':
                if skus_list.count('A') < 3:
                    tmp_price += entry['price']
                else:
                    if A_counter < 3:
                        A_counter += 1
                    else:
                        # add special offer value and reset counter
                        tmp_price += entry['special_price']
                        A_counter = 0
            elif SKU == 'B':
                if skus_list.count('B') < 2:
                    tmp_price += entry['price']
                else:
                    if B_counter < 2:
                        B_counter += 1
                    else:
                        # add special offer value and reset counter
                        tmp_price += entry['special_price']
                        B_counter = 0
            else:
                tmp_price += entry['price']

    return tmp_price




