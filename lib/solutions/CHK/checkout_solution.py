

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1
    print(skus)
    skus_list = split(skus)
    for SKU in skus_list:
        if SKU not in ['A','B','C','D']:
            return -1
    print(skus_list)
    #raise NotImplementedError()

checkout('C,D')
