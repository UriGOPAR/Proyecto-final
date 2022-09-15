"""Tic Tac Toe code by ©2017-2022, Grant Jenks
This is a modified version with educational purposes
"""

from turtle import *

from freegames import line


def grid():
    # Draw tic-tac-toe grid
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    # Draw X player.
    line(x + 10, y + 10, x + 123, y + 123)
    line(x + 10, y + 123, x + 123, y + 10)


def drawo(x, y):
    # Draw O player
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    # Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()