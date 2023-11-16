from category import Category
from transaction import Transaction

class Account():

    def __init__(self, name):
        self.__transactions = []
        self.__name = name

    def add_transaction(self, description, amount, category):
        self.__transactions.append(Transaction(description, amount, category, len(self.__transactions) + 1))

    def delete_transaction(self, expense):
        self.__transactions.remove(expense)

    def get_transaction(self, transaction_id):
        for transaction in self.__transactions:
            if transaction.get_transaction_id() == transaction_id:
                return transaction;
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name


class Customer(Account):
    def __init__(self, customer_id, name):
        super().__init__()
        self.__customer_id = customer_id

    def get_customer_id(self):
        return self.__customer_id


class Supplier(Account):
    def __init__(self, supplier_id, name):
        super().__init__()
        self.__supplier_id = supplier_id

    def get_supplier_id(self):
        return self.__supplier_id