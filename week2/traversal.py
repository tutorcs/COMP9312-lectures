https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from collections import deque
# use deque instead of [] in python to implement queue

n = 8
edges = [[0,1],[0,2],[1,2],[1,3],[1,4],[4,5],[6,7]]

# create adjacency list
adj_list = [[] for j in range(n)]
for edge in edges:
	adj_list[edge[0]].append(edge[1])
	adj_list[edge[1]].append(edge[0])

# create CSR
offset = [0]*(n+1);
csr_edges = [];
for i in range(n):
	offset[i] = len(csr_edges)
	csr_edges.extend(adj_list[i])
offset[n] = len(csr_edges)


# BFS
def BFS(u):
	visited = [False] * n
	# initialize an boolean array / bitmap
	queue = deque()
	queue.append(u)
	# O(1)
	visited[u] = True

	while queue:
		s = queue.popleft()
		# time complexity is expected to be O(1), [].pop(0) takes O(n) in the worst case
		# 99% scenarios, never user [].pop(0)
		print(s)
		for i in range(offset[s],offset[s+1]):
			nbr_of_s = csr_edges[i]
			if visited[nbr_of_s]: continue
			queue.append(nbr_of_s)
			visited[nbr_of_s] = True 



# DFS recursive
visited = [False] * n
def DFS_recursive(u):
	print(u)
	visited[u] = True
	for i in range(offset[u],offset[u+1]):
		nbr_of_u = csr_edges[i]
		if visited[nbr_of_u]: continue
		DFS_recursive(nbr_of_u)

# DFS_recursive(0)


# DFS iterative / stack-based
def DFS_iterative(u):
	visited = [False] * n
	# initialize an boolean array / bitmap
	stack = []
	stack.append(u)
	# O(1)
	visited[u] = True

	while stack:
		s = stack.pop()
		# O(1)
		print(s)
		for i in range(offset[s],offset[s+1]):
			nbr_of_s = csr_edges[i]
			if visited[nbr_of_s]: continue
			stack.append(nbr_of_s)
			visited[nbr_of_s] = True 


# DFS_iterative(0)


# naive method to compute all connected components
def naive_cc():
	unvisited = [i for i in range(n)]
	# id form 0 to n-1
	result = []

	while unvisited:
		u = unvisited.pop()
		current_cc = []
		queue = deque()
		queue.append(u)
		while queue:
			s = queue.popleft()
			current_cc.append(s)
			for i in range(offset[s],offset[s+1]):
				nbr_of_s = csr_edges[i]
				if nbr_of_s in unvisited:
				# scan the whole list to find the item: O(n)
					queue.append(nbr_of_s)
					unvisited.remove(nbr_of_s)
					# O(n) like pop(0)
		result.append(current_cc)
	return result

# print(naive_cc())

# an improved algorithm to computed connected components, time complexity: O(m)
def cc():
	result = []
	visited = [False]*n

	for i in range(n):
		if visited[i]: continue
		current_cc = []
		queue = deque()
		queue.append(i)
		visited[i] = True
		current_cc.append(i)

		while queue:
			s = queue.popleft()
			for j in range(offset[s],offset[s+1]):
				nbr_of_s = csr_edges[j]
				if visited[nbr_of_s]: continue
				queue.append(nbr_of_s)
				visited[nbr_of_s] = True
				current_cc.append(nbr_of_s)

		result.append(current_cc)

	return result



# print(cc())



### disjoint set data structure for n items

parent = [i for i in range(n)]
size   = [1 for i in range(n)]

def find(x):
	# path compression
	if parent[x] != x:
		parent[x] = find(parent[x])
	return parent[x]

def union(x,y):
	x = find(x)
	y = find(y)
	# union by tree size
	if size[x] < size[y]:
		size[y] += size[x]
		parent[x] = y
	else:
		size[x] += size[y]
		parent[y] = x

### using disjoint set to compute all connected components
def ds_cc():
	for edge in edges:
		union(edge[0],edge[1])

# ds_cc()
# print(find(1) == find(2))





