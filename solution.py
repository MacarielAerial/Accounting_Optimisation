'''
The script provides the solution to AM16 SPR20 Financial Reporting Analytics Group Assignment 3
'''

# Import libraries
import numpy as np
import math
import gurobipy as gp
from gurobipy import GRB, quicksum
import matplotlib.pyplot as plt

# Define global parameters
capacity_one = 250000
fixed_cost = 2000000000

# Define search ranges
factory_number = [1, 2, 3]
price_a = list(range(10000, 100000, 5000))
price_b = list(range(10000, 100000, 5000))

class Optimisation:
	'''
	Module to solve the embedded optimisation problem
	'''
	def __init__(self, capacity_one, fixed_cost, price_a, price_b, factory_number):
		self.capacity_one, self.fixed_cost = capacity_one, fixed_cost
		self.price_a, self.price_b, self.factory_number = price_a, price_b, factory_number
		self.best_params = [0, 0, 0, 0, 0]
		self.profit = []
		self.current_profit = 0
		self.best_profit = 0
		self.quantity_a = []
		self.current_quantity_a = 0
		self.quantity_b = []
		self.current_quantity_b = 0

	def grid_search(self):
		'''Calculate all viable solutions given ranges of input'''
		for i_1 in range(len(factory_number)):
			for i_2 in range(len(price_a)):
				for i_3 in range(len(price_b)):
					self.current_quantity_a = (1000000 - 1000000/(1 + math.exp(-(1/15000)*(price_a[i_2]-50000))))
					self.current_quantity_b = (1000000 - 1000000/(1 + math.exp(-(1/15000)*(price_b[i_3]-40000))))
					if self.current_quantity_a + self.current_quantity_b <= factory_number[i_1] * self.capacity_one:
						self.current_profit = self.current_quantity_a*price_a[i_2] + self.current_quantity_b*price_b[i_3] - (56000 - 5600/(1 + math.exp(1-(1/10000)*(self.current_quantity_a - 50000))))*self.current_quantity_a - (35000 - 3500/(1 + math.exp(-(1/20000)*(self.current_quantity_b - 100000))))*self.current_quantity_b - 2000000000*factory_number[i_1]
						self.quantity_a.append(self.current_quantity_a)
						self.quantity_b.append(self.current_quantity_b)
						self.profit.append(self.current_profit)
						if self.current_profit == max(self.profit):
							self.best_params = [factory_number[i_1], price_a[i_2], price_b[i_3], self.current_quantity_a, self.current_quantity_b]
							self.best_profit = self.current_profit
					else:
						self.quantity_a.append(0)
						self.quantity_b.append(0)
						self.profit.append(0)

	def result_display(self):
		print('*'*10 + 'The highest level of profit is:' + '*'*10)
		print(self.best_profit)
		print('The optimal number of factory is:')
		print(self.best_params[0])
		print('The optimal price level for model A is:')
		print(self.best_params[1])
		print('The optimal price level for model B is:')
		print(self.best_params[2])
		print('The corresponding demand level for model A is:')
		print(self.best_params[3])
		print('The corresponding demand level for model B is;')
		print(self.best_params[4])
		print('*'*10 + '*'*len('The highest level of profit is:') + '*'*10)

	def exec(self):
		self.grid_search()
		self.result_display()


if __name__ == '__main__':
	obj = Optimisation(capacity_one, fixed_cost, price_a, price_b, factory_number)
	obj.exec()
