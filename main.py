import turtle
screen = turtle.Screen()
#list of all turtles on screen. 
all_turtles = []
#current prompts is a list of all prompts on screen. It needs to be emptied when a screen is changed. Do not append directly.
current_prompts = []
#Creates a singular prompt box. Takes arguments based on the text to be added, position, size and color.
def create_prompt(message_text, box_size_x, box_size_y, color, position: list):
    #Todo: add code for color.
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

#Adds prompts to the current_prompts list. This list should only be appended to through this method. 
def add_event_handler(message_triggered, size_x: int, size_y: int, position:list):
    current_prompts.append([message_triggered, size_x, size_y, position])

#size of box x, size of box y, number of boxes, list of text to go in the options, position of the menu, optional padding
def create_menu(box_size_x, box_size_y, num_boxes, list_messages, position: list, padding=0):
    for i in range(num_boxes):
        position = [position[0] + i*box_size_x + padding, position[1]]
        add_event_handler(list_messages[i], box_size_x, box_size_y, position)
        create_prompt(list_messages[i], box_size_x, box_size_y, "red", position)
        
#On click function that's ran every time the user clicks. It checks what prompts are on screen from current_prompts
#then calculates what the user click.
def on_click(x, y):
    print(x, y)
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
            #Todo: introduce progression based on what the user clicks
            print(prompt[0])

#function takes information about the next screen and displays it. Returns the changes based on the user's choices.
def load_screen(position_menu: list, box_size: int, options: list, background_path="", padding=0):
    #Todo: implement stats about mental health, physical health, etc
    #Todo: implement background images
    create_menu(box_size, 200, len(options), options, position_menu, padding=50)
    value_change = []
    return value_change

if __name__ == "__main__":
    #Initalization code
    menu_size = [1000, 800]
    screen.setup(width=1200, height=800)
    turtle.tracer(False)
    #Bind the onclick method
    turtle.onscreenclick(on_click)
    options = ["Go to class now", "Sleep in"]
    #Load the first screen
    load_screen([-600, 0], menu_size[0] / len(options), options, padding=50)
    
turtle.tracer(True)
turtle.mainloop()
