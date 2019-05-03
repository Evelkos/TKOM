# node.py
from abc import ABC, abstractmethod


class Node(ABC):
	def __init__(self, node_name, node_type):
		self.children = []
		self.name = node_name
		self.type = node_type


	@abstractmethod
	def visit(self):
		pass