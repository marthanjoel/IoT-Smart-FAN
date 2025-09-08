# oneWire.py (SIMULATION VERSION - Python2 compatible)

def setupOneWire(gpio):
    print("[SIM] OneWire setup on GPIO %s" % gpio)
    return True

def scanOneAddress():
    print("[SIM] Scanning for OneWire sensor...")
    return "28-00000fakeaddress"
