def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_icon(IconNames.HEART)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.pause(1000)
    basic.clear_screen()
    basic.pause(1000)
basic.forever(on_forever)
