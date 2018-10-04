def neighbor(maze, node, direction):
    if direction == 'n':
        if node[0] - 1 < 0:
            return 'W'
        else:
            return maze[node[0]-1][node[1]]
    if direction == 's':
        if node[0] + 1 == len(maze):
            return 'W'
        else:
            return maze[node[0]+1][node[1]]
    if direction == 'w':
        if node[1] - 1 == -1:
            return 'W'
        else:
            return maze[node[0]][node[1]-1]
    if direction == 'e':
        if node[1] + 1 == len(maze[0]):
            return 'W'
        else:
            return maze[node[0]][node[1]+1]

def path_finder(maze):
    maze = maze.split()
    start_x = 0
    start_y = 0
    finish_x = len(maze) - 1
    finish_y = len(maze[finish_x]) - 1
    queue = [(start_x, start_y)]
    visited_nodes = []
    while len(queue) > 0:
        node = queue.pop(0)
        print(node)
        if neighbor(maze, node, 'e') == '.':
            next_node = (node[0],node[1]+1)
            if next_node not in visited_nodes:
                if next_node[0] == finish_x and next_node[1] == finish_y:
                    return True
                queue.append(next_node)
                visited_nodes.append(next_node)
        if neighbor(maze, node, 's') == '.':
            next_node = (node[0]+1,node[1])
            if next_node not in visited_nodes:
                if next_node[0] == finish_x and next_node[1] == finish_y:
                    return True
                queue.append(next_node)
                visited_nodes.append(next_node)
        if neighbor(maze, node, 'w') == '.':
            next_node = (node[0],node[1]-1)
            if next_node not in visited_nodes:
                if next_node[0] == finish_x and next_node[1] == finish_y:
                    return True
                queue.append(next_node)
                visited_nodes.append(next_node)
        if neighbor(maze, node, 'n') == '.':
            next_node = (node[0]-1,node[1])
            if next_node not in visited_nodes:
                if next_node[0] == finish_x and next_node[1] == finish_y:
                    return True
                queue.append(next_node)
                visited_nodes.append(next_node)
    return False
