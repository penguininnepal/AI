graph = {
  'a' : ['b','c'],
  'b' : ['d', 'e'],
  'c' : ['f'],
  'f' : [],
  'd' : [],
  'e' : []
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited, graph, 'a')