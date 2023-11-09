class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

user1 = User('user1', 'user1@users.com')
user2 = User('user2', 'user2@users.com')
user3 = User('user3', 'user3@users.com')

user1.make_deposit(20).make_deposit(30).make_deposit(25).make_withdrawal(10).display_user_balance()

user2.make_deposit(50).make_deposit(40).make_withdrawal(20).make_withdrawal(13).display_user_balance()

user3.make_deposit(90).make_withdrawal(20).make_withdrawal(12).make_withdrawal(11).display_user_balance()

user1.transfer_money(user2,20)
user1.display_user_balance()
user2.display_user_balance()