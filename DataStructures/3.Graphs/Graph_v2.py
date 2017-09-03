# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Graph_v2.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/01 16:30:16 by kcheung           #+#    #+#              #
#    Updated: 2017/09/02 19:19:49 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This is a basic implementation of a Graph Datastructure (without using dicts)
class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	vertices = {}
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False

	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
		else:
			self.add_vertex(Vertex(u))
			self.add_vertex(Vertex(v))
			self.add_edge(u, v)

g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)

for i in range(ord('A'),ord('Z'),2):
	g.add_vertex(Vertex(chr(i)))

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('A', 'D')
g.add_edge('B', 'D')
g.add_edge('Z', 'O')
g.add_edge('B', 'D')
print g.vertices
# g.dfs('A')

g.print_graph()
