import turtle
screen = turtle.Screen()

def create_prompt(message_text, box_size, color, position: list):
    t = turtle.Turtle()
    # Start left corner
    t.penup()
    t.goto(position)
    t.pendown()
    t.setheading(0)
    for _ in range(2):
        t.forward(box_size)
        t.right(90)
        t.forward(box_size / 2)
        t.right(90)
    
    return 

def create_menu(size, num_boxes, list_messages, position: list):
    for i in range(num_boxes):
        position = [position[0] + i*((size + 50) / 2), position[1]]
        create_prompt(list_messages[i], size / num_boxes, "red", position)

if __name__ == "__main__":
    screen.setup(width=800, height=600)
    screen_size = [800, 600]
    print("Hello world!")
    options = ["Go to class now", "Sleep in"]
    count_msg = len(options)
    create_menu(500, count_msg, options, [-350, -0])

turtle.mainloop()
