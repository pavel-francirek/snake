let direction = 0
let food = [0, 0]
let direction_change = [[0, -1], [1, 0], [0, 1], [-1, 0]]
let snake = [[2, 2]]
led.plot(2, 2)
function set_food() {
    
    food = [randint(0, 4), randint(0, 4)]
    led.plotBrightness(food[0], food[1], 27)
}

function snake_run() {
    let new_point: number[];
    let in_snake: boolean;
    
    while (true) {
        basic.pause(1000)
        new_point = [snake[0][0] + direction_change[direction][0], snake[0][1] + direction_change[direction][1]]
        in_snake = false
        for (let s of snake) {
            if (s[0] == new_point[0] && s[1] == new_point[1]) {
                in_snake = true
            }
            
        }
        if (new_point[0] < 0 || new_point[0] > 4 || new_point[1] < 0 || new_point[1] > 4 || in_snake) {
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Dadadadum), music.PlaybackMode.InBackground)
            basic.showIcon(IconNames.Angry)
            basic.showNumber(snake.length)
            return
        }
        
        if (new_point[0] == food[0] && new_point[1] == food[1]) {
            set_food()
        } else {
            if (snake[snake.length - 1][0] != food[0] || snake[snake.length - 1][1] != food[1]) {
                led.unplot(snake[snake.length - 1][0], snake[snake.length - 1][1])
            }
            
            snake.removeAt(snake.length - 1)
        }
        
        led.plot(new_point[0], new_point[1])
        snake.unshift(new_point)
        music.play(music.tonePlayable(Note.C5, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.UntilDone)
    }
}

input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    
    
    basic.clearScreen()
    snake = [[2, 2]]
    direction = randint(0, 3)
    led.plot(2, 2)
    set_food()
    snake_run()
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    direction = direction - 1
    if (direction < 0) {
        direction = 3
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    direction = direction + 1
    if (direction > 3) {
        direction = 0
    }
    
})
