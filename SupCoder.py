#!/bin/python3
import random
import datetime
import time

class Monolith:
	def __init__(self, keys, values=None):
		if type(keys) != str:
			raise TypeError("Please Provide String.")
		self.chars = {}
		self.reverseChars = {}
		
		if values == None:
			for item in keys:
				self.chars[item] = item
			
			for i in range(int(len(keys) ** 1.5)):
				x = random.choice(list(self.chars.keys()))
				y = random.choice(list(self.chars.keys()))
				self.chars[x], self.chars[y] = self.chars[y], self.chars[x]
		else:
			if len(keys) != len(values):
				raise NameError("Key And Values, Size Inconistency")
				
			for item in [keys, values]:
				for i in range(0, len(item)-1):
					for j in range(i+1, len(item)):
						if item[i] == item[j]:
							raise NameError("Repeating Char")
							
			for item in keys:
				if item not in values:
					raise NameError("Asynchrone Encoding, Not Possible Decoding")
			
			for i in range(len(keys)):
				self.chars[keys[i]] = values[i]
		pass
			
		for thing in self.chars:
			self.reverseChars[self.chars[thing]] = thing
	
	def __getitem__(self, x):
		try:
			return self.chars[x]
		except:
			return x
	
	def __call__(self, x):
		try:
			return self.reverseChars[x]
		except:
			return x
	
	def __repr__(self):
		return "Monolith " + repr(self.chars)
		
	def __str__(self):
		return "Monolith " + str(self.chars)

class Multilith:
	def __init__(self, monolist):
		for monolith in monolist:
			if type(monolith) != Monolith:
				raise TypeError("Please provide List of Monolith")
		self.monolist = monolist
	
	def __getitem__(self, x):
		return self.monolist[x]
	
	def __repr__(self):
		return "Multilith " + repr(self.monolist)
		
	def __str__(self):
		return "Multilith " + str(self.monolist)
	
	def decode(self, string):
		listlen = len(self.monolist)
		curr = 0
		x = ""
		for i in range(len(string)):
			x += self.monolist[curr][string[i]]
			curr += 1
			if curr >= len(self.monolist):
				curr = 0
		return x
	
	def encode(self, string):
		listlen = len(self.monolist)
		curr = 0
		x = ""
		for i in range(len(string)):
			x += self.monolist[curr](string[i])
			curr += 1
			if curr >= len(self.monolist):
				curr = 0
		return x


if __name__ == "__main__":
	multilith = Multilith(
		[
			Monolith("0123456789-+*×÷/|\\.,;:!?`~¡¿()[]{}<>《》▪︎¤ #ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz°•○●□■♤♡◇♧") for i in range(3)
		]
	)
	
	while True:
		msg = multilith.decode(f"{datetime.datetime.now().astimezone().isoformat()}")
		print(end = "\u001Bc")
		print(msg)
		print(multilith.encode(msg))
		
		time.sleep(1)
		
