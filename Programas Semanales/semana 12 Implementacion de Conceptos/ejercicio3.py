def Breadth_First_Search(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print (s, end = " ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

def UNIFORM_COST_SEARCH(problem):
    return  BEST_FIRST_SEARCH()