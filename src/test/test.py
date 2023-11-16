from category import Category

boodschappen = Category('Boodschappen')#
vaste_lasten = Category('Vaste lasten')#
eten = Category('Eten', boodschappen)#
drinken = Category('Drinken', boodschappen)#
alcohol = Category('Alcohol', drinken)
sap = Category('Sap', drinken)#
brood = Category('Brood', eten)#
groenten = Category('Groenten', eten)#
fruit = Category('Fruit', eten)#
frisdrank = Category('Frisdrank', drinken)#
appel = Category('Appel', fruit)#
cola = Category('Cola', frisdrank)#
volkoren = Category('Volkoren brood', brood)#
alcohol.delete()
    
#Category.exp_categories('testfile')

data = Category.imp_categories("testfile")
Category.load_categories(data)
Category.print_tree()

# my_account = Account()

# my_account.add_transaction('Boodschappen bij Albert Heijn', 20.0, Category('Boodschappen'))
# for transaction in my_account._Account__transactions:
#     print(transaction)