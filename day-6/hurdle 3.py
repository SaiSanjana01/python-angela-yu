def turn_right():
    turn_left()
    turn_left()
    turn_left()


def hurdle3():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        hurdle3()