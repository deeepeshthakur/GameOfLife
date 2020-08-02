def find_coordinates(x, y):
    # Get coordinates of mouse click
    return (x- x%10, y - y%10)

def get_all_neighbours(cell):
    # get neighbours along with current cell
    (x,y) = cell
    return [(x-i,y-j) for i in range(-10,20,10) for j in range(-10,20,10)]

def get_next_generation(cells):
    # Get next generation
    next_gen = {}
    which_cells_to_check = set()
    for curr_cell,_ in cells.items():
        for xy in get_all_neighbours(curr_cell):
            which_cells_to_check.add(xy)
    for curr_cell in which_cells_to_check:
        curr_live_neighbours = 0
        for xy in get_all_neighbours(curr_cell):
            curr_live_neighbours += 1 if (curr_cell != xy) and (cells.get(xy,None) is not None) else 0
        if cells.get(curr_cell,None) is not None and ((curr_live_neighbours == 2) or (curr_live_neighbours == 3)):
            next_gen[curr_cell]=True
        if cells.get(curr_cell,None) is None and (curr_live_neighbours == 3):
            next_gen[curr_cell]=True
    return next_gen
