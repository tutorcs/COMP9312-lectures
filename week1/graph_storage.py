https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
n = 8
# streaming graph
edges = [[0,1],[0,2],[1,2],[1,3],[1,4],[4,5],[6,7]]
# assume there is no duplicated edge

# Task: we need a data structure
# 1. get neighbors of each vertex
# 2. check if (u,v) has existed in the graph
# 3. add a new edge, e.g., add (u,v) to the graph

# ========
# naive inefficient data structure
nbr = {}
# O(1)
# iterate i fom 0 to n-1
for i in range(n):
	nbr[i] = []

for edge in edges:
	nbr[edge[0]].append(edge[1])

# get neighbor of #1
# print(nbr[1])

# tips: try to not use hash table
# hash table good theoretical results but bad practical efficiency

# {} Dictionary - hash table
# [] list
# () tuple - list


# ========
# adj matrix

adj_matrix = [[0 for i in range(n)] for j in range(n)]
for edge in edges:
	adj_matrix[edge[0]][edge[1]] = 1
	# for undirected graphs
	adj_matrix[edge[1]][edge[0]] = 1


# print(adj_matrix[1])
# any improvement for the above code?
# g[1,2,3,4] in python
# g[1,2,3,4] in C++/Java
# array vs list in python


# a = g[1]
# b = g[2]
# in C: int a = g[1]
# how many reads from memory to CPU? for Python and C++
# 3 for python and 1 for C++/Java
# tips: use array for high efficiency


# =====
# adj List
adj_list = [[] for j in range(n)]
for edge in edges:
	adj_list[edge[0]].append(edge[1])
	adj_list[edge[1]].append(edge[0])




# === 
# CSR
offset = [0]*(n+1)
csr_edges = []
for i in range(n):
	offset[i] = len(csr_edges)
	csr_edges.extend(adj_list[i])
offset[n] = len(csr_edges)

v = 1
for i in range(offset[v],offset[v+1]):
	print(csr_edges[i])


