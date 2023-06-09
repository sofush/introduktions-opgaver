#!/usr/bin/env python
import pygame as pg
from pygame import Color
from pygame import Surface
import time
import random

pg.init()

cell_size = 50
num_rows =12
num_cols = 6 
pad = 5

def calc_width():
    return num_cols*cell_size + pad

def calc_height():
    return num_rows*cell_size + pad

screen = pg.display.set_mode((calc_width(), calc_height()))

grid = []
for _ in range(num_cols):
    grid.append([None]*num_rows)


running = True

sqr = None


class Square:
    def __init__(self,col,row,color):
        self.col = col
        self.row = row
        self.color = color


clear_color = Color(50,50,50)
colors = [Color(200,0,0), Color(0,200,0), Color(0,0,200)]

def wait_tick():
    time.sleep(0.1)

def is_complete_row(row_index):
    for col in range(num_cols):
        if grid[col][row_index] == None:
            return False
    return True

def clear_row(row_index):
    for col in range(num_cols):
        grid[col][row_index] = None

def remove_complete_rows():
    for row in range(num_rows):
        for col in range(num_cols):
            if is_complete_row(row):
                clear_row(row)


def draw_game():
    ## Draw game
    for col in range(num_cols):

        for row in range(num_rows):

            pg.draw.rect(screen, clear_color, pg.Rect((col*cell_size+pad, row*cell_size+pad), (cell_size-pad,cell_size-pad)))

            if col == sqr.col and row == sqr.row:
                pg.draw.rect(screen, sqr.color, pg.Rect((col*cell_size+pad, row*cell_size+pad), (cell_size-pad,cell_size-pad)))

            elif grid[col][row] is not None:
                pg.draw.rect(screen, grid[col][row].color, pg.Rect((col*cell_size+pad, row*cell_size+pad), (cell_size-pad,cell_size-pad)))

tick = 0
while running:

    # New square
    if not sqr:
        col = random.randint(0,num_cols-1)
        color = random.choice(colors)
        sqr = Square(col,0,color)

    # Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # Close window
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
                pg.quit()
                exit()

            # Pause the game
            elif event.key == pg.K_ESCAPE:
                while True:
                    wait_tick()
                    sub_event = pg.event.wait()

                    if sub_event.type == pg.QUIT:
                        running = False
                        break
                    
                    elif sub_event.type == pg.KEYDOWN:
                        if sub_event.key == pg.K_ESCAPE:
                            break

            elif event.key == pg.K_LEFT:
                sqr.col -= 1

            elif event.key == pg.K_RIGHT:
                sqr.col += 1




    draw_game()


    # Update square
    if tick % 3 == 0:
        if sqr.row + 1 < num_rows:
            if grid[sqr.col][sqr.row+1] is None:
                sqr.row += 1
            else:
                grid[sqr.col][sqr.row] = sqr
                sqr = None
        else:
           grid[sqr.col][sqr.row] = sqr
           sqr = None
        
        remove_complete_rows()


    # Update the screen window with any new drawings
    pg.display.flip()

    # Wait a moment
    wait_tick()
    tick = tick + 1
