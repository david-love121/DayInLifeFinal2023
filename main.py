import turtle
screen = turtle.Screen()
all_turtles = []
#current prompts is a list of all prompts on screen
current_prompts = []
def create_prompt(message_text, box_size_x, box_size_y, color, position: list):
    t = turtle.Turtle()
    all_turtles.append(t)
    # Start left corner
    t.penup()
    t.goto(position)
    t.pendown()
    t.setheading(0)
    for _ in range(2):
        t.forward(box_size_x)
        t.right(90)
        t.forward(box_size_y)
        t.right(90)
    # Turtle is top left facing right 
    text_turtle = turtle.Turtle()
    all_turtles.append(text_turtle)
    text_turtle.penup()
    text_turtle.hideturtle()
    text_turtle.goto([position[0] + (box_size_x / 2), position[1] - (box_size_y / 2)])
    text_turtle.pendown()
    text_turtle.write(message_text, align="center", font=("Arial", 12, "normal"))
    return 

def add_event_handler(message_triggered, size_x: int, size_y: int, position:list):
    current_prompts.append([message_triggered, size_x, size_y, position])

def create_menu(size_x, size_y, num_boxes, list_messages, position: list):
    for i in range(num_boxes):
        position = [position[0] + i*size_x + 50, position[1]]
        add_event_handler(list_messages[i], size_x, size_y, position)
        create_prompt(list_messages[i], size_x, size_y, "red", position)

def on_click(x, y):
    for i in range(len(current_prompts)):
        # format [message_triggered, size_x, size_y, position]
        prompt = current_prompts[i]
        position = prompt[3]
        bounds_x = position[0] + prompt[1]
        bounds_y = position[1] - prompt[2] 
        lower_x_bound = min(position[0], bounds_x)
        higher_x_bound = max(position[0], bounds_x)
        lower_y_bound = min(position[1], bounds_y)
        higher_y_bound = max(position[1], bounds_y)
        if lower_x_bound < x < higher_x_bound and lower_y_bound < y < higher_y_bound:
            print(prompt[0])

if __name__ == "__main__":
    screen.setup(width=800, height=600)
    screen.screensize(800, 600)
    screen_size = [800, 600]
    turtle.tracer(False)
    print("Hello world!")
    options = ["Go to class now", "Sleep in"]
    count_msg = len(options)
    create_menu(300, 200, count_msg, options, [-350, -0])
    turtle.onscreenclick(on_click)

turtle.tracer(True)
turtle.mainloop()
