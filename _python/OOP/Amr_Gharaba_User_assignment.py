class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.name, self.account_balance)
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

user1 = User('user1', 'user1@users.com')
user2 = User('user2', 'user2@users.com')
user3 = User('user3', 'user3@users.com')

user1.make_deposit(20)
user1.make_deposit(30)
user1.make_deposit(25)
user1.make_withdrawal(10)
user1.display_user_balance()

user2.make_deposit(50)
user2.make_deposit(40)
user2.make_withdrawal(20)
user2.make_withdrawal(13)
user2.display_user_balance()


user3.make_deposit(90)
user3.make_withdrawal(20)
user3.make_withdrawal(12)
user3.make_withdrawal(11)
user3.display_user_balance()

user1.transfer_money(user2,20)
user1.display_user_balance()
user2.display_user_balance()