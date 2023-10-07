flashes = 50
flashDelay = 25
led = Pin("LED", Pin.OUT)

while flashes > 0:
    flashes-=1
    time.sleep_ms(flashDelay)
    led.toggle()
