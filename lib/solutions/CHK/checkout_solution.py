

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1
    print(skus)
    skus_list = skus.split(',')
    print(skus_list)
    #raise NotImplementedError()

checkout('C,D')




