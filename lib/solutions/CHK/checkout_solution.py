

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, unicode):
        return -1
    print(skus)
    skus_list = skus.split(',')
    #raise NotImplementedError()

checkout('C,D')



