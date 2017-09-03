# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    DFS.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/02 11:58:30 by kcheung           #+#    #+#              #
#    Updated: 2017/09/02 19:27:52 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	
	def add_edge(self, u, v):
		self.graph[u].append(v)

	def dfs(self, start, visited=None):
		if visited is None:
			visited = set()
		visited.add(start)
		print start,
		for next in self.graph[start]:
			if next not in visited:
				self.dfs(next, visited)
		return visited

g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)
# g.dfs(2)

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('A', 'D')
g.add_edge('B', 'D')
g.add_edge('Z', 'O')
g.add_edge('B', 'D')
g.dfs('A')
# print g.graph['A']
