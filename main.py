# import colorgram
# rgb_colors=[]
# colors=colorgram.extract("C:\python\Angelia\cologram_project\image.jpg",12)

# for i in colors:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim=turtle_module.Turtle()

color_list=[(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73)]

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed(0)
num_of_dots=100

for dot_count in range(1, num_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen=turtle_module.Screen()
screen.exitonclick()