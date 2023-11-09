class BankAccount:
	def __init__(self, int_rate = 0.02, balance = 0):
		self.int_rate = int_rate
		self.balance = balance

	def deposit(self, amount):
		self.balance+=amount
		return self

	def withdraw(self, amount):
		if (self.balance - amount < 0):
			self.balance-=5
			print("Insufficient funds: Charging a $5 fee")
		else:
			self.balance-=amount
		return self

	def display_account_info(self):
		print(f"Balance: {self.int_rate, self.balance}")
		return self

	def yield_interest(self):
		if(self.balance > 0):
			self.balance+= self.balance*self.int_rate
		else:
			self.balance-= self.balance*self.int_rate
		return self

account1 = BankAccount()
account1.deposit(200).deposit(300).deposit(500).withdraw(450).yield_interest().display_account_info()

account2 = BankAccount(int_rate= 0.05, balance=20)
account2.deposit(600).deposit(700).withdraw(1000).withdraw(700).withdraw(1000).withdraw(2000).yield_interest().display_account_info()