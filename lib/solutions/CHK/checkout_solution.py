

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
    print(skus)
    skus_list = split(skus)

    tmp_price = 0
    for SKU in skus_list:
        if SKU not in validate_input:
            return -1

        if 'A' in validate_input:
            special_A_counter = skus_list.count('A')
            if special_A_counter % 3 == 0:
                offer_A_multiplier = special_A_counter / 3
                tmp_price += (SKU['special_price'] * offer_A_multiplier)

        if 'B' in validate_input:
            special_B_counter = skus_list.count('B')
            if special_A_counter % 2 == 0:
                offer_B_multiplier = special_B_counter / 2
                tmp_price += (SKU['special_price'] * offer_B_multiplier)

        if not SKU['special_offer']:
            tmp_price += SKU['price']

    return tmp_price
    #raise NotImplementedError()

checkout('C,D')

