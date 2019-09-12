phones = ['AAA', 'BBB']

product = {
    'name': 'Iphone',
    'stock': 24,
    'price': 65432.1,
    'recomend': phones,
}

print(product['recomend'])

print(product['recomend'][1])

product['recomend'].append('Iphon 6')

print(product)

print(type(product))

print(type(phones))

    