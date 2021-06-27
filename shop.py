from collections import defaultdict


def shop():
    menu = [
        'carne de panela',
        'pizza',
    ]

    rec = {
        'carne de panela':
        [
            ('alcatra', 700),
            ('cebola', 150),
            ('cenoura', 200),
        ],

        'pizza':
        [
            ('farinha', 500),
            ('fermento envelope', 1),
            ('elefante peq', 1),
            ('mussarela', 300),
            ('cebola', 100),
        ],
    }

    shoplist = defaultdict(int)
    for dish in menu:
        for ingr, amt in rec[dish]:
            shoplist[ingr] += amt

    print()
    for ingr in sorted(shoplist):
        print('{:<20}\t{:>6}\n'.format(ingr, shoplist[ingr]))
