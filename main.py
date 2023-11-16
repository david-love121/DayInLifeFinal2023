import turtle
screen = turtle.Screen()
all_turtles = []
def create_prompt(message_text, box_size_x, box_size_y, color, position: list):
    t = turtle.Turtle()
    # Start left corner
    t.penup()
    t.goto(position)
    t.pendown()
    t.setheading(0)
    for _ in range(2):
        t.forward(box_size_y)
        t.right(90)
        t.forward(box_size_x)
        t.right(90)
    all_turtles.append(t)
    return 

def create_menu(size_x, size_y, num_boxes, list_messages, position: list):
    for i in range(num_boxes):
        position = [position[0] + i*size_x, position[1]]
        create_prompt(list_messages[i], size_x / num_boxes, size_y, "red", position)

if __name__ == "__main__":
    screen.setup(width=800, height=600)
    screen.screensize(800, 600)
    screen_size = [800, 600]
    print("Hello world!")
    options = ["Go to class now", "Sleep in"]
    count_msg = len(options)
    create_menu(400, 300, count_msg, options, [-350, -0])

turtle.mainloop()
