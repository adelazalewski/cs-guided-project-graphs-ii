graph = {
    'a': set(['b','c','d']),
    'b': set(),
    'c': set('e'),
    'd': set(['e', 'f']),
    'e': set(['a', 'f']),
    'f': set()
}
# def main_function(current_vertex):
#     visited = set()
#     def print_graph(current_vertex):
#         print(current_vertex)
#         #recurse on the children
#         for neighbor in graph[current_vertex]:
#             if neighbor not in visited:
#                 print_graph(neighbor)


#print_graph('a')

def print_graph(current_vertex, visited):
    print(current_vertex)
    visited.add(current_vertex)
    print(visited)
    #recurse on the children
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            print_graph(neighbor, visited)

print_graph('a', set())

def interative_dfs(start_vertex, target_vertex):
    stack = []
    visited = set()
    stack.append((start_vertex, []))

    while len(stack) > 0:
        #process verts on the stack and queue up other ones
        current_vertex, current_path = stack.pop()
        visited.add(current_vertex)

        #update a path/more like the previous path
        current_path.append(current_vertex)
        #print(current_vertex)

        #check if the current ver ios our target:
        if current_vertex == target_vertex:
            print("found!")
            return current_path


        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                stack.append((neighbor, current_path.copy()))


print(interative_dfs('a', 'f'))

def interative_Bfs(start_vertex, target_vertex):
    queue = []
    visited = set()
    queue.append((start_vertex, []))

    while len(queue) > 0:
        #process verts on the stack and queue up other ones
        current_vertex, current_path = queue.pop(0)

        #check if current vertex has been visited:
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        #update a path/more like the previous path
        current_path.append(current_vertex)
        #print(current_vertex)

        #check if the current ver ios our target:
        if current_vertex == target_vertex:
            print("found!")
            return current_path


        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                queue.append((neighbor, current_path.copy()))

print(interative_Bfs('a', 'f'))