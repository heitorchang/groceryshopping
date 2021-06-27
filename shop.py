from collections import defaultdict


menu = ['mac n cheese', 'tofu pad thai', 'beef teriyaki']

rec = {
    'beef stroganoff': [
        ('alcatra', 700),
    ],
    
    'beef teriyaki': [
        ('alcatra', 700),
    ],
    
    'carne de panela': [
        ('alcatra', 700),
    ],
    
    'chicken biryani': [
        ('chicken', 700),
    ],
    
    'chicken cacciatore': [
        ('chicken', 700),
    ],

    'chicken with cabbage': [
        ('chicken', 700),
    ],

    'chicken stroganoff': [
        ('chicken', 700),
    ],

    'coleslaw': [
    ],

    'coq au vin': [
        ('chicken', 700),
    ],

    'couscous salad': [
    ],

    'funghi risotto': [
    ],

    'hijiki gohan': [
    ],

    'kare udon': [
    ],

    'lasagna': [
    ],

    'mac n cheese': [
    ],

    'mapo tofu': [
    ],

    'miso pork': [
    ],

    'miso shiru': [
    ],

    'nitsuke': [
    ],

    'noodle soup': [
    ],

    'pasta bolognese': [
        ('carne moida', 300),
    ],

    'pesto': [
    ],

    'pizza': [
    ],

    'potato salad': [
    ],

    'ratatouille': [
    ],

    'roast chicken': [
        ('chicken', 1000),
    ],

    'shrimp pad thai': [
    ],

    'tofu pad thai': [
    ],

    'tomato honey chicken': [
        ('chicken', 700),
    ],

    'vaca atolada': [
        ('alcatra', 700),
    ],

    'vodka pasta': [
    ],

    'yakisoba': [
        ('alcatra', 500),
    ],
}

    
def shop():
    shoplist = defaultdict(int)
    print(", ".join(menu))
    print()
    
    for dish in menu:
        if len(rec[dish]) < 2:
            print("Warning:", dish, "is incomplete.")
        for ingr, amt in rec[dish]:
            shoplist[ingr] += amt

    print()
    for ingr in sorted(shoplist):
        print('{:<20}\t{:>6}\n'.format(ingr, shoplist[ingr]))


def listmenu():
    for d in sorted(rec):
        print(f"'{d}': [],")


def withingr(ingr):
    matches = []
    for r in rec:
        for i, amt in rec[r]:
            if ingr in i:
                matches.append(r)
    print("\n".join(matches))
