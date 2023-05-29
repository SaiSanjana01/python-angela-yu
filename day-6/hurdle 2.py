def turn_right():
    turn_left()
    turn_left()
    turn_left()


def hurdle1():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
while not at_goal():
    move()
    hurdle1()