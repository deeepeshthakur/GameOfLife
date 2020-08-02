from tkinter import Tk, Frame, Canvas, Button, LEFT, RIGHT
from helper import find_coordinates, get_next_generation

root = Tk()
root.title("Game of Life")
frame = Frame(root, width=720, height=720)
frame.pack()
canvas = Canvas(frame, width=720, height=720)
canvas.pack()

begin_id = None
live_cells = {}  # To store live cells
rectangles = {}  # To store reference of gui elements

def create_grid():
    # Create Grid
    global rectangles 
    for (ix,iy) in [(i,j) for i in range(70) for j in range(70)]:
        (x,y) = (10+10*ix,10+10*iy)
        rectangles[(x,y)] = canvas.create_rectangle(x, y, x+10, y+10, fill="",outline="white")

def handle_click_event(event):
    # What to do when user uses mouse click to kill or give life to a cell
    global live_cells
    global begin_id
    if begin_id is not None:
        stop_game()
    x, y = find_coordinates(event.x, event.y)
    if live_cells.get((x,y),None) is None:
        canvas.itemconfig(rectangles[(x,y)], fill="black",outline="black")
        live_cells[(x,y)]=True
    else:
        canvas.itemconfig(rectangles[(x,y)], fill="",outline="white")
        del live_cells[(x,y)]

def paint_grid():
    global live_cells
    global rectangles

    for key, item in rectangles.items():
        if live_cells.get(key,None) is not None:
            canvas.itemconfig(item,fill="black",outline="black")
        else:
            canvas.itemconfig(item,fill="",outline="white")

def next_step():
    global live_cells
    live_cells = get_next_generation(live_cells)
    paint_grid()

def just_next_step():
    global begin_id
    if begin_id is not None:
        stop_game()
    next_step()

def begin_game():
    global begin_id
    next_step()
    begin_id = root.after(200, begin_game)


def stop_game():
    root.after_cancel(begin_id)

create_grid()
start = Button(root, text="Start Game", command = begin_game)
start.pack(side = LEFT)
next_button = Button(root, text="Next Step", command = just_next_step)
next_button.pack(side = LEFT)
stop = Button(root, text="Stop Game", command = stop_game)
stop.pack(side = LEFT)
canvas.bind("<Button-1>", handle_click_event)
root.mainloop()