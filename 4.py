#7#
def delivery(amount):
    if amount == 1:
        return (one_product)
    else:
        return (round(one_product + other_products * (amount - 1), 2))


one_product = 10.95
other_products = 2.95
amount = int(input("Введите количество товара: "))
print('Стоимость доставки: ', delivery(amount))