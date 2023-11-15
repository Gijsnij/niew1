riching = randint(1, 3)
maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 100)
basic.show_string("" + str(riching))

def on_forever():
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) < 15:
        maqueen.motor_stop(maqueen.Motors.ALL)
    else:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 100)
basic.forever(on_forever)
