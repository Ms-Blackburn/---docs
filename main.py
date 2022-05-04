def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.pause(20)
    basic.show_icon(IconNames.SMALL_HEART)
basic.forever(on_forever)
