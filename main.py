import turtle
turtle.setup(900,600)
turtle.title("PONG")
turtle.bgcolor("pink")
turtle.hideturtle()


import time

import Ball
import itbivalka
turtle.tracer(0)

levaya=itbivalka.Otbivalka(-400, 0)

pravaya=itbivalka.Otbivalka(400, 0)


turtle.update()
turtle.listen()
turtle.onkey(levaya.move_up, "w")
turtle.onkey(levaya.move_down, "s")
turtle.onkey(pravaya.move_up, "Up")
turtle.onkey(pravaya.move_down, "Down")
gameON=True
scrennball=Ball.ball()



while gameON:
    time.sleep(0.1)
    turtle.update()
    scrennball.move_ball()
    if scrennball.ycor() > 300 or scrennball.ycor() < -300:
        scrennball.boll_tern()
    elif scrennball.xcor() > 400 or scrennball.xcor() < -400:
        pass
    if scrennball.distance(levaya) < 20 or scrennball.distance(pravaya) < 20:
        scrennball.boll_tern()






turtle.exitonclick()