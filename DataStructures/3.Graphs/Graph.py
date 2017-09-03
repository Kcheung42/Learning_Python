# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Graph.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/01 13:27:53 by kcheung           #+#    #+#              #
#    Updated: 2017/09/02 11:56:07 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This is a basic implementation of an undirected graph
# Adjacency List structure

class Node:
	def __init__(self, dest=None, nextNode=None):
		self.dest = dest
		self.next = nextNode

class NodeList:
	def __init__(self, head=None):
		self.head = head
		
class Graph:
	def __init__(self, count):
		self.count = count
		self.graph = [NodeList()] * self.count

	def addEdge(self, src, dest):
		self.new_Node = Node()
		if not self.graph[src].head:
			self.graph[src].head = Node(dest)
			self.graph[dest].head = Node(src)
		else:
			self.graph[src] = Node(dest, self.graph[src].head)
			self.graph[dest].head = Node(src, self.graph[dest].head)
	
	def printGraph(self):
		for index, node in enumerate(self.graph):
			print (index),
			self.printEdges(node.head)

	def printEdges(self, head):
		cur = head
		if cur is None:
			return "list is empty"
		while cur:
			print("%d ->" % cur.dest)
			cur = cur.next

g = Graph(10)

g.addEdge(0,1)
g.addEdge(0,2)
g.printGraph()

