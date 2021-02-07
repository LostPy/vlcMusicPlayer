"""Class Queue"""


class Queue:
	"""A class which represent a queue object."""

	def __init__(self, list_: list = []):
		self.list_ = list(list_)
		
	def __len__(self):
		return len(self.list_)
	
	def pop(self):
		return self.list_.pop(0)
	
	def add_item(self, item):
		self.list_.append(item)
	
	def add_items(self, items: list):
		self.list_ += list(items)

	@property
	def is_empty(self):
		return len(self) == 0