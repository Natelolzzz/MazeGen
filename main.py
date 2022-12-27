import random

def generate_maze(width, height):
  # Create a grid of tiles, where each tile is represented by a tuple (x, y)
  tiles = [(x, y) for x in range(width) for y in range(height)]

  # Initialize the maze with all walls present
  maze = {tile: {'north': True, 'south': True, 'east': True, 'west': True} for tile in tiles}

  # Select a starting tile
  current_tile = random.choice(tiles)

  # Perform a depth-first search to generate the maze
  stack = []
  visited_tiles = set()
  while len(visited_tiles) < len(tiles):
    visited_tiles.add(current_tile)
    neighbors = [(current_tile[0] + dx, current_tile[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
    neighbors = [n for n in neighbors if n in tiles and n not in visited_tiles]
    if neighbors:
      stack.append(current_tile)
      next_tile = random.choice(neighbors)
      # Remove the wall between the current tile and the next tile
      maze[current_tile]['east' if next_tile[0] > current_tile[0] else 'west'] = False
      maze[next_tile]['west' if next_tile[0] > current_tile[0] else 'east'] = False
      maze[current_tile]['south' if next_tile[1] > current_tile[1] else 'north'] = False
      maze[next_tile]['north' if next_tile[1] > current_tile[1] else 'south'] = False
      current_tile = next_tile
    else:
      current_tile = stack.pop()

  return maze

# Generate a 10x10 maze
maze = generate_maze(10, 10)

# Print the maze
for y in range(10):
  for x in range(10):
    print('+---' if maze[(x, y)]['east'] else '+   ', end='')
  print('+')
  for x in range(10):
    print('|   ' if maze[(x, y)]['south'] else '    ', end='')
  print('|')
print('+' + '---+' * 10)
