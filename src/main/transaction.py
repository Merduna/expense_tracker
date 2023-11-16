import datetime

class Transaction():

    def __init__(self, description, amount, category, transaction_id):
        try:
            assert isinstance(category, Category)
            self.__transaction_id = transaction_id
            self.__date = datetime.datetime.now()
            self.__description = description
            self.__amount = amount
            self.__category = category
        except AssertionError:
            print('Invalid input')
   
    def __str__(self):
        return "transaction_id: " + str(self.__transaction_id) + "\ndate: " + str(self.__date) + "\ndescription: " + str(self.__description) + "\namount: " + str(self.__amount) + "\ncategory: " + self.__category.get_name() + " " + str(self.__category.get_category_id())

    def get_transaction_id(self):
        return self.__transaction_id

    def get_date(self):
        return self.__date
    
    def get_description(self):
        return self.__description
    
    def get_amount(self):
        return self.__amount
    
    def get_category(self):
        return self.__category