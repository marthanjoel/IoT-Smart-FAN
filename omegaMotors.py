# omegaMotors.py (SIMULATION VERSION - Python2 compatible)

class OmegaPwm:
    def __init__(self, channel):
        self.channel = channel

    def _setFrequency(self, freq):
        print("[SIM] PWM frequency set to: %s Hz" % freq)

    def setDutyCycle(self, duty):
        print("[SIM] Fan duty cycle set to: %s%%" % duty)

class hBridgeMotor:
    def __init__(self, channel1, channel2):
        self.channel1 = channel1
        self.channel2 = channel2

    def forward(self, duty):
        print("[SIM] Motor forward at duty %s%%" % duty)

    def reverse(self, duty):
        print("[SIM] Motor reverse at duty %s%%" % duty)

    def stop(self):
        print("[SIM] Motor stopped")

