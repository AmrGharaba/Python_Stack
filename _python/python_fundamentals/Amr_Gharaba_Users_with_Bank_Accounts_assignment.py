class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.account = BankAccount( int_rate = 0.02, balance = 0)
	def deposit(self, amount):
		self.account.balance+=amount
		return self
	def withdraw(self, amount):
		if (self.account.balance - amount < 0):
			self.account.balance-=5
			print("Insufficient funds: Charging a $5 fee")
		else:
			self.account.balance-=amount
		return self
	def display_account_info(self):
		print(f"Balance: {self.account.int_rate, self.account.balance}")
		return self

class BankAccount:

	def __init__(self, int_rate, balance):
		self.int_rate = int_rate
		self.balance = balance
	def yield_interest(self):
		if(self.balance > 0):
			self.balance+= self.balance*self.int_rate
		else:
			self.balance-= self.balance*self.int_rate
		return self

user1 = User('micheal','miacheal@account.com')
user1.deposit(50).display_account_info()