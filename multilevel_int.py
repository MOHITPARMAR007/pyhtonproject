class Eleactronic_device:
    motherbord=1
    circuit=3
class Poket_gadget(Eleactronic_device) :
    gps=1
    circut=8
    time="yes"

class smartphone(Poket_gadget) :
    screentouch="yes"
    games="yes"
    circut = 12
    cpu=1

tv=Eleactronic_device
ipod=Poket_gadget
apple=smartphone
print(apple.games)



