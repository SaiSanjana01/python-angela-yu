def turn_right():
    turn_left()
    turn_left()
    turn_left()
def maze():
    turn_right()
    move()
while not at_goal():
    if right_is_clear():
        maze()
    elif front_is_clear():
        move()   
    else:
        turn_left()