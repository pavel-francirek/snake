direction = 0 # 0: N, 1: E, 2: S, 3: W
food = (0,0)
direction_change = (
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
)

# init
snake = [(2,2)]
led.plot(2,2)

def set_food():
    # create new "food"
    global food
    food = (randint(0, 4), randint(0, 4))
    led.plot_brightness(food[0], food[1], 27)

def snake_run():
    global snake
    while True:
        # main loop
        basic.pause(1000)
        new_point = (
            snake[0][0] + direction_change[direction][0],
            snake[0][1] + direction_change[direction][1]
        )
        # check if new point (new part of snake) hits existing body of snake
        in_snake = False
        for s in snake:
            if s[0] == new_point[0] and s[1] == new_point[1]:
                in_snake = True

        # end game condition
        if new_point[0] < 0 or new_point[0] > 4 or new_point[1] < 0 or new_point[1] > 4 or in_snake:
            music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM), music.PlaybackMode.IN_BACKGROUND)
            basic.show_icon(IconNames.ANGRY)
            basic.clear_screen()
            basic.show_number(len(snake))
            return
        if new_point[0] == food[0] and new_point[1] == food[1]:
            # food is eaten
            set_food()
        else:
            if snake[len(snake)-1][0] != food[0] or snake[len(snake)-1][1] != food[1]:
                # if there is no new created food "inside" snake
                led.unplot(snake[len(snake)-1][0], snake[len(snake)-1][1])
            snake.remove_at(len(snake)-1)
        led.plot(new_point[0], new_point[1])
        snake.unshift(new_point)
        music.play(music.tone_playable(Note.C5, music.beat(BeatFraction.SIXTEENTH)), music.PlaybackMode.UNTIL_DONE)

def on_logo_event_pressed():
    global snake
    global direction
    basic.clear_screen()
    snake = [(2,2)]
    direction = randint(0, 3)
    led.plot(2,2)
    set_food()
    snake_run()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

def on_button_pressed_a():
    global direction
    direction = direction - 1
    if direction < 0:
        direction = 3
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global direction
    direction = direction + 1
    if direction > 3:
        direction = 0
input.on_button_pressed(Button.B, on_button_pressed_b)
