let riching = randint(1, 3)
maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 100)
basic.showString("" + ("" + riching))
basic.forever(function on_forever() {
    if (maqueen.Ultrasonic(PingUnit.Centimeters) < 15) {
        maqueen.motorStop(maqueen.Motors.All)
    } else {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 100)
    }
    
})
