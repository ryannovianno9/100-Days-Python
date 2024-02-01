def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while at_goal() != True:
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        while front_is_clear() and not at_goal():
            move()
            while right_is_clear():
                turn_right()
                move()