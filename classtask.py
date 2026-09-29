

1
# a = input("first: ")
# b = input("Second: ")

# try:
#     a = int(a)
#     b = int(b)
#     print(f"Result: {a/b}")
# except ValueError:
#     print("Enter only numbers")
# except ZeroDivisionError:
#     print("zero division error")
# finally:
#     print("Calculation finished")


2
# Cities = ['Dushanbe', 'Khujand', 'Bokhtar']
# try:
#     a = int(input("Enter index: "))
#     print(f"City: {Cities[a]}")
# except ValueError:
#     print("Enter only numbers!")
# except IndexError:
#     print("Position does not exist")


3
# Prices = {'mouse': 100, 'keyboard': 250, 'monitor': 1200}
# try:
#     key = input("Enter key: ")
#     quant = int(input("Enter quantity for product: "))
#     print(f"Total: {Prices[key] * quant}")
# except ValueError:
#     print("Wrong quantity!")
# except KeyError:
#     print("Product does not exist!")

4
# nums = input().split()
# def calculate_average(values):
#     try:
#         for i in range(len(values)):
#             values[i] = int(values[i])
#         return f"Average: {sum(values) / len(values)}"
#     except ValueError as error:
#         return f"{type(error).__name__}: {error}"
#     except ZeroDivisionError as error:
#         return f"{type(error).__name__}: {error}"
#     except Exception as error:
#         return f"{type(error).__name__}: {error}"

# print(calculate_average(nums))

5
# def register(name, age):
#     if not isinstance(name, str):
#         raise TypeError("name must be a string")
#     if not isinstance(age, int):
#         raise TypeError("age must be an integer")    
#     if name.strip() == "":
#         raise ValueError("name cant be empty")
#     if not 18 <= age <= 100:
#         raise ValueError("age must be from 18 to 100")
#     reg = {
#         "name": name,
#         "age": age
#     }
#     return reg
# try:
#     print(f"Registered: {register("ali", 12)}") 
# except (TypeError, ValueError) as error:
#     print(f"{type(error).__name__}: {error}")



6

# class InsufficientFundsError(Exception):
#     def __init__(self, balance, amount):
#         message = f"requested {amount}, available {balance}."
#         super().__init__(message)


# class BankAccount:

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance

#     def show_balance(self):
#         return f"Balance: {self.__balance}"
    
#     def deposit(self, amount):
#         if amount < 0:
#             raise ValueError("Amount must be positive")
#         self.__balance += amount
#     def withdraw(self,amount):
#         if amount > self.__balance:
#             raise InsufficientFundsError(self.__balance, amount)
#         self.__balance -= amount
#         return "Withdraw completed"

# acc = BankAccount("Ali", 1000)

# try:
#     # acc.withdraw(1100)
#     # acc.deposit(-500)
#     print(acc.withdraw(500))
#     print(acc.show_balance())
# except (ValueError, InsufficientFundsError) as error:
#     print(f"{type(error).__name__}: {error}")




7
# def process_payment(balance, amount):
#     if amount < 0:
#         raise ValueError("Amount must be positive")
#     if amount > balance:
#         raise InsufficientFundsError(balance, amount)

# Balance = 1000
# Payment = 50


# try:
#     process_payment(Balance, Payment)
# except (ValueError, InsufficientFundsError) as error:
#     print(f"{type(error).__name__}: {error}")
# else:
#     print(f"New balance: {Balance - Payment}")
# finally:
#     print("Payment attemp finished")




8
# def price_per_item(total, quantity):
#     try:
#         return total / quantity
#     except ZeroDivisionError as error:
#         return error


# def build_report(order):
#     return price_per_item(order["total"], order["quantity"])


# def main():
#     order = {"total": 600, "quantity": 0}
#     print(build_report(order))


# main()


9
# def line_total(price, quantity):
#     return price * quantity


# def cart_total(items):
#     total = 0
#     for index, item in enumerate(items):
#         price = item["price"]
#         quantity = item["quantity"]
#         total += line_total(price, quantity)
#     return total


# cart = [
#     {"name": "Mouse", "price": 100, "quantity": 2},
#     {"name": "Keyboard", "price": 250, "quantity": 1},
#     {"name": "Cable", "price": 30, "quantity": 3},
# ]
# print(cart_total(cart))

10
from datetime import datetime


def parse_date(text):
    try:
        return datetime.strptime(text, "%d.%m.%Y")
    except ValueError:
        print("Invalid date format!")

text = input()
print(parse_date(text).strftime("%Y-%m-%d"))