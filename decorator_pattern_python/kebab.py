from collections import namedtuple

PRIX_BASE = 3.0
PRIX_MOUTON = 0.8
PRIX_POULET = 1.0
PRIX_SALADE = 0.2
PRIX_TOMATES = 0.2
PRIX_OIGNONS = 0.3
PRIX_FRITES = 0.5

Ingredient = namedtuple('Ingredient', 'prix quantite')

class Kebab:
    def __init__(self, sauce):
        self.type_sauce = sauce
        self.type_viande = 'mouton'
        self.base = PRIX_BASE

        self._ing = dict()


        self._ing['viande'] = Ingredient(PRIX_MOUTON, 1)
        self._ing['tomates'] = Ingredient(PRIX_TOMATES, 1)
        self._ing['salade'] = Ingredient(PRIX_SALADE, 1)
        self._ing['oignions'] = Ingredient(PRIX_OIGNONS, 1)
        self._ing['frites'] = Ingredient(PRIX_FRITES, 1)
        self._ing['fromage'] = Ingredient(PRIX_FROMAGE, 1)


    @property
    def prix(self):
        return (self.base + sum(i.prix*i.quantite for i in self._ing.values()))

    def __str__(self):
        s = "Kebab ({0: .2f} sauce {1})".format(self.prix, self.type_sauce)
        if self.type_viande !="mouton":
            s += ', au {0}) '.format(self.type_viande)
        for elt in self._ing:
            qte = self._ing[elt].quantite
            if qte > 0:
                s += ', {0}x{1}'.format(qte, elt)
            else:
                s += ', sans {0}'.format(elt)
        return s

    def sans(self, ingredient):
        if ingredient in self._ing:
            prix, _ =self._ing[ingredient]
            self._ing[ingredient] = Ingredient(prix, 0)

    def supp(self, ingredient):
        if ingredient in self._ing:
            prix, _ =self._ing[ingredient]
            self._ing[ingredient] = Ingredient(prix, qte+1)

    def poulet(self):
        self.type_viande ='poulet'
        _, qte = self._ing['viande']
        self._ing['viande'] = Ingredient(PRIX_POULET, qte)


