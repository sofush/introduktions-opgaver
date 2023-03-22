#!/usr/bin/env python
import pygame as pg
import time
import random

pg.init()

cell_size = 50
num_rows =12
num_cols = 6 
pad = 5

screen = pg.display.set_mode((num_cols*cell_size + pad, num_rows*cell_size+pad))

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


colors = [(200,0,0), (0,200,0), (0,0,200)]


tick = 0
while running:

    # New square
    if not sqr:
        col = random.randint(0,num_cols-1)
        color = random.randint(0,2)
        sqr = Square(col,0,color)

    # Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # Close window
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

            elif event.key == pg.K_LEFT:
                sqr.col -= 1

            elif event.key == pg.K_RIGHT:
                sqr.col += 1





    ## Draw game
    for col in range(num_cols):

        for row in range(num_rows):

            pg.draw.rect(screen, (50,50,50), pg.Rect((col*cell_size+pad, row*cell_size+pad), (cell_size-pad,cell_size-pad)))

            if col == sqr.col and row == sqr.row:
                pg.draw.rect(screen, colors[sqr.color], pg.Rect((col*cell_size+pad, row*cell_size+pad), (cell_size-pad,cell_size-pad)))

            elif grid[col][row] is not None:
                pg.draw.rect(screen, colors[grid[col][row].color] , pg.Rect((col*cell_size+pad, row*cell_size+pad), (cell_size-pad,cell_size-pad)))


    # Update square
    if tick % 10 == 0:
        if sqr.row + 1 < num_rows:
            if grid[sqr.col][sqr.row+1] is None:
                sqr.row += 1
            else:
                grid[sqr.col][sqr.row] = sqr
                sqr = None
        else:
           grid[sqr.col][sqr.row] = sqr
           sqr = None


    # Update the screen window with any new drawings
    pg.display.flip()

    # Wait a moment
    time.sleep(0.1)
    tick = tick + 1
