from collections import deque

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
    finish_x = len(maze) - 1
    finish_y = len(maze[finish_x]) - 1
    queue = deque()
    queue.append((0,0))
    visited_nodes = set()
    while len(queue) > 0:
        node = queue.popleft()
        if neighbor(maze, node, 'e') == '.':
            next_node = (node[0],node[1]+1)
            if next_node not in visited_nodes:
                if next_node[0] == finish_x and next_node[1] == finish_y:
                    return True
                queue.append(next_node)
                visited_nodes.add(next_node)
        if neighbor(maze, node, 's') == '.':
            next_node = (node[0]+1,node[1])
            if next_node not in visited_nodes:
                if next_node[0] == finish_x and next_node[1] == finish_y:
                    return True
                queue.append(next_node)
                visited_nodes.add(next_node)
        if neighbor(maze, node, 'w') == '.':
            next_node = (node[0],node[1]-1)
            if next_node not in visited_nodes:
                if next_node[0] == finish_x and next_node[1] == finish_y:
                    return True
                queue.append(next_node)
                visited_nodes.add(next_node)
        if neighbor(maze, node, 'n') == '.':
            next_node = (node[0]-1,node[1])
            if next_node not in visited_nodes:
                if next_node[0] == finish_x and next_node[1] == finish_y:
                    return True
                queue.append(next_node)
                visited_nodes.add(next_node)
    return False

def main():
    a = "\n".join([
      ".W.",
      ".W.",
      "..."
    ])

    b = "\n".join([
      ".W.",
      ".W.",
      "W.."
    ])

    c = "\n".join([
      "......",
      "......",
      "......",
      "......",
      "......",
      "......"
    ])

    d = "\n".join([
      "......",
      "......",
      "......",
      "......",
      ".....W",
      "....W."
    ])
    print(path_finder(a))
    print(path_finder(b))
    print(path_finder(c))
    print(path_finder(d))

main()
