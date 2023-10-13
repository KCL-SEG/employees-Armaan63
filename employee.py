"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from enum import Enum

class Commission(Enum):
    BONUS = 1
    CONTRACT = 2
    NONE = 3

class Contract(Enum):
    HOURLY = 1
    SALARY = 2

class Employee:
    def __init__(self, name, contract, commission, num_contracts, commission_rate, hours, rate, salary):
        self.name = name
        self.contract = contract
        self.commission = commission
        self.num_contracts = num_contracts
        self.commission_rate = commission_rate
        self.hours = hours
        self.rate = rate
        self.salary = salary

    def get_pay(self):
        pay = 0

        if(self.contract == Contract.HOURLY):
            pay = self.hours * self.rate
            pay = pay + self.get_commission()
        else:
            pay = self.salary
            pay = pay + self.get_commission()

        return pay
    
    def get_commission(self):
        commission = 0

        if self.commission == Commission.CONTRACT:
            commission = self.num_contracts * self.commission_rate
        elif self.commission == Commission.BONUS:
            commission = self.commission_rate
        
        return commission
    
    def __str__(self):
        statement = ''

        if(self.contract == Contract.HOURLY and self.commission == Commission.NONE):
            statement = statement + f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour.'
        elif(self.contract == Contract.SALARY and self.commission == Commission.NONE):
            statement = statement + f'{self.name} works on a monthly salary of {self.salary}.'
        elif(self.contract == Contract.HOURLY and self.commission == Commission.BONUS):
            statement = statement + f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour '
            statement = statement + f'and receives a bonus commission of {self.commission_rate}.'
        elif(self.contract == Contract.SALARY and self.commission == Commission.BONUS):
            statement = statement + f'{self.name} works on a monthly salary of {self.salary} '
            statement = statement + f'and receives a bonus commission of {self.commission_rate}.'
        elif(self.contract == Contract.HOURLY and self.commission == Commission.CONTRACT):
            statement = statement + f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour '
            statement = statement + f'and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract.'
        elif(self.contract == Contract.SALARY and self.commission == Commission.CONTRACT):
            statement = statement + f'{self.name} works on a monthly salary of {self.salary} '
            statement = statement + f'and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract.'

        statement = statement + f' Their total pay is {self.get_pay()}.'

        return statement


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Contract.SALARY, Commission.NONE, 0, 0, 0, 0, 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Contract.HOURLY, Commission.NONE, 0, 0, 100, 25, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Contract.SALARY, Commission.CONTRACT, 4, 200, 0, 0, 3000)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Contract.HOURLY, Commission.CONTRACT, 3, 220, 150, 25, 0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Contract.SALARY, Commission.BONUS, 0, 1500, 0, 0, 2000)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Contract.HOURLY, Commission.BONUS, 0, 600, 120, 30, 0)
