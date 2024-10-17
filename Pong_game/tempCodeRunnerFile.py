 ball.move()
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()
    if ball.distance(r_paddle) <50:
        print("done")
