from .turn_on_off import TurnOnOfDevise


class TurbineDevise(TurnOnOfDevise):
    on = "ON"
    off = "OFF"

    def __init__(self):
        super().__init__(self.off)
        self._intervalRefresh=20
        self._activationPin="3"
        self._analogPin="A1"

    def powerOff(self):
        pass            #to implement, turn off state

    def refresh(self,currentTime):
        if self._state==on:
            self._controller.sendReceiveData("high"+self._activationPin)
            response = self._controller.sendReceiveData(self._analogPin)
            self._controller.sendReceiveData("low"+self._activationPin)

            if response.split()[1]==self._analogPin:
                if int(response.split()[0]) <= 695:
                    self.powerOff()
            else:
                return str(int(currentTime)+5)

        return str(int(currentTime)+self._intervalRefresh)
