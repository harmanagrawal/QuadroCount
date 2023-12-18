from tkinter import Button
import utilities
import settings
#import random

class Cell:
    all = []
    counter = 0
    alternate = 1
    current_player = 0
    area_blue = 4
    area_red = 4
    move_history = []
    def __init__(self, x, y, is_piece):
        self.is_piece = is_piece
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)       
        
    def create_btn(self, location, color):
        btn_text = f'{self.is_piece}' if self.is_piece != 0 else ""
        btn_fg = 'red' if self.is_piece == 1 else 'blue'
        btn = Button(
            location,
            text = btn_text,
            #image = settings.red_circle_image,
            #compound = 'center',
            fg = btn_fg,
            #text = f'{self.x}, {self.y}',
            bg = color,
            width = 10,
            height = 4
            )
        btn.bind('<Button-1>', self.left_click_actions) # Left Click
        btn.bind('<Button-3>', self.right_click_actions) # Right Click
        location.bind('<Control-z>', lambda event: self.undo_last_move())
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(event)
        #print("I am left clicked!")
        if (self.is_piece == 1):
            print('red piece')
        elif (self.is_piece == -1):
            print('blue piece')
        else:
            print('no piece present')

    def right_click_actions(self, event):
        grid_info = event.widget.grid_info()
        x1 = grid_info['row']
        y1 = grid_info['column']
        print(event)
        #print("I am right clicked!")
        if (self.is_piece == Cell.alternate):
            if (self.is_piece != 0 and Cell.counter % 2 == 0):
                Cell.counter += 1
                Cell.alternate = -self.is_piece
                Cell.current_player = self.is_piece
                self.is_piece = 0
                # Update the text of the button to reflect the change
                self.cell_btn_object.config(text='', fg = 'yellow')
                print(Cell.current_player)
        elif (self.is_piece == 0 and Cell.counter % 2 == 1):
            Cell.counter += 1
            self.is_piece = Cell.current_player
            print(Cell.current_player)
            #current_player = 0
            btn_fg = 'red' if self.is_piece == 1 else 'blue'
            self.cell_btn_object.config(text = Cell.current_player, fg = btn_fg)
        move = {'x': self.x, 'y': self.y, 'is_piece': self.is_piece}
        print(move)
        Cell.move_history.append(move)
        
    @classmethod
    def undo_last_move(cls):
        if Cell.move_history:
            last_move = Cell.move_history.pop()
            cell = cls.get_cell_by_axis(last_move['x'], last_move['y'])
            cell.is_piece = last_move['is_piece']
            btn_text = f'{cell.is_piece}' if cell.is_piece != 0 else ""
            btn_fg = 'red' if cell.is_piece == 1 else 'blue'
            cell.cell_btn_object.config(text=btn_text, fg=btn_fg)
        
    @classmethod
    def get_cell_by_axis(cls, x,y):
        # Return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def __repr__(self):
       return f"Cell({self.x}, {self.y})"