https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
n = 8
edges = [[0,1],[0,2],[0,4],[1,2],[1,3],[1,4],[2,4],[3,4],[4,5],[6,7]]

# add [0,4], [2,4], [3,4]

# adjacency list
adj_list = [[] for _ in range(n)]
for edge in edges:
	adj_list[edge[0]].append(edge[1])
	adj_list[edge[1]].append(edge[0])


def core_decomposition():
	# core decomposition
	deg_vertices = []
	deg = []

# initialize arrays
# ==================

	for u in range(n):
		deg.append(len(adj_list[u]))
		while deg[u] > len(deg_vertices)-1:
			deg_vertices.append([])
		deg_vertices[deg[u]].append(u)

	max_deg = len(deg_vertices)


	deg_position = [0 for _ in range(max_deg+1)]
	vertex_position = [0 for I in range(n)]
	vertex_order = []

	for d in range(1,max_deg):
		deg_position[d] = len(vertex_order)
		for u in deg_vertices[d]:
			vertex_position[u] = len(vertex_order)
			vertex_order.append(u)

# =====================

	for i in range(n):
		v = vertex_order[i]
		for u in adj_list[v]:
			if deg[v] >= deg[u]: continue
			old_deg_of_u = deg[u]
			old_position_of_u = vertex_position[u]
			start_position_of_u_deg = deg_position[old_deg_of_u]
			start_vertex_of_deg = vertex_order[start_position_of_u_deg]
			if u != start_vertex_of_deg:
				vertex_order[old_position_of_u] = start_vertex_of_deg
				vertex_order[start_position_of_u_deg] = u
				vertex_position[u] = start_vertex_of_deg
				vertex_position[start_vertex_of_deg] = old_position_of_u
			deg_position[old_deg_of_u] = deg_position[old_deg_of_u]+1
			deg[u] = deg[u]-1

	print(deg)




# triangle counting
# naive
def naive_triangle_counting():
	triangles = 0
	for u in range(n):
		for v in adj_list[u]:
			triangles = triangles + len(set(adj_list[u]).intersection(set(adj_list[v])))
	print(int(triangles/6))




def improved_triangle_counting():

	# build directed graphs
	directed_adj_list = [[] for _ in range(n)]
	for u in range(n):
		for v in adj_list[u]:
			if len(adj_list[v]) < len(adj_list[u]) or (len(adj_list[v]) == len(adj_list[u]) and v < u):
				directed_adj_list[u].append(v)


	triangles = 0
	for u in range(n):
		# build hash table for u's out-going neighbors
		nbr_set_of_u = set(directed_adj_list[u])
		for v in directed_adj_list[u]:
				for w in directed_adj_list[v]:
					if(w in nbr_set_of_u):
						triangles += 1
						print("<"+str(u)+","+str(v)+","+str(w)+">")

	print(triangles)

improved_triangle_counting()
core_decomposition()
		

