from tkinter import *
from cell import Cell
import settings
import utilities

w = 4
h = 4
w1 = w * 120
h1 = h * 120

root = Tk()
root.configure(bg = 'black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('QuadroCount')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg = 'light blue',
    width = settings.WIDTH,
    height = utilities.height_prcnt(100/6)
    )
top_frame.place(x = 0, y = 0)

left_frame = Frame(
    root,
    bg = 'steel blue',
    width = utilities.width_prcnt(20),
    height = utilities.height_prcnt(500/6)
    )
left_frame.place(x = 0, y =utilities.height_prcnt(100/6)
)

center_frame= Frame(
    root,
    bg = 'black',
    width = utilities.width_prcnt(80),
    height = utilities.height_prcnt(500/6)
    )
center_frame.place(x = utilities.width_prcnt(20), y = utilities.height_prcnt(100/6))


for x in range (settings.GRID_SIZE):
    for y in range (settings.GRID_SIZE):
        if (x+y == 1):
            k = 1
            #fg = 'red'
        elif (x + y == 9):
            k = -1
            #fg = 'blue'
        else:
            k = 0
            #fg = 'green'
        c = Cell(x, y, k)
        if ((x + y) % 2 == 0):
            bg = 'white'
        else:
            bg = 'black'
        c.create_btn(center_frame, bg)
        c.cell_btn_object.grid(column = x, row = y)

#print(Cell.get_cell_by_axis(1, 0, 1).is_piece)
root.mainloop()