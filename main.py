class Customer:
    def __init__(self, name, date_of_birth, balance):
        self.name = name
        self.date_of_birth = date_of_birth  
        self._balance = balance

    @property
    def age(self):
        today = (2024, 10, 18) 
        year, month, day = self.date_of_birth
        age = today[0] - year - ((today[1], today[2]) < (month, day))
        return age

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []  

    @property
    def budget(self):
        return sum(customer.balance for customer in self.customers)

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer):
        if customer in self.customers:
            self.customers.remove(customer)

    def can_get_loan(self, customer, amount):
        return customer.balance >= (amount * 0.5)


customer1 = Customer("Niko", (2001, 6, 5), 1000.0)
customer2 = Customer("Gioegi", (1990, 4, 18), 500.0)

bank = Bank("Saq.Banki")
bank.add_customer(customer1)
bank.add_customer(customer2)

sawyisi = bank.budget

loan = bank.can_get_loan(customer1, 1500)

customer1.withdraw(200)
customer2.deposit(300)

finalbudg = bank.budget

print("saywisi biudjeti:", sawyisi)
print("Loani (1500):", loan)
print("Final Budget :", finalbudg)
