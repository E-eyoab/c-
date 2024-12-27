import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black
screen.title("Colorful Animated Object")  # Set title of the window

# Create a turtle object
t = turtle.Turtle()
t.shape("circle")  # Set the shape of the turtle
t.speed(0)  # Fastest animation speed
t.width(3)  # Set width of the turtle's pen

# Function to change color randomly
def change_color():
    colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "white"]
    return random.choice(colors)

# Create a function for animation
def animate_object():
    for _ in range(100):  # Repeat the animation 100 times
        t.color(change_color())  # Change the color randomly
        t.forward(50)  # Move the turtle forward
        t.right(30)  # Turn the turtle by 30 degrees
        t.penup()
        t.goto(random.randint(-300, 300), random.randint(-300, 300))  # Move to a random position
        t.pendown()

# Run the animation
animate_object()

# Close the turtle graphics window on click
screen.exitonclick()
