import turtle
turtle.setup(800,600)
window=turtle.Screen()
window.title("My dragon")
t=turtle.getturtle()
turtle.register_shape('mypolygon',((0,0),(100,0),(140,40)))
t.shape('mypolygon')
t.fillcolor('pink')
for angle in range(0,360,5):
    t.setheading(angle)
    t.stamp()
turtle.exitonclick()
                                  
