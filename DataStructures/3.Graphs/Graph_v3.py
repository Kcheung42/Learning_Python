# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Graph_v3.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/01 16:14:36 by kcheung           #+#    #+#              #
#    Updated: 2017/09/02 18:55:36 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This is a basic implementation of a Graph Datastructure (using Dict)

from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	
	def addEdge(self, u, v):
		self.graph[u].append(v)

g = Graph()
g.addEdge('A','B')
g.addEdge('A','B')
g.addEdge('A','B')
g.addEdge('B','B')
g.addEdge('C','D')
g.addEdge('A','B')
g.addEdge('C','A')

for keys, values in sorted(g.graph.items()):
	print (keys + str(values))


