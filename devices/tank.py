from .state_device import StateDevice


class TankDevice(StateDevice):
    def __init__(self):
        self._intervalRefresh=20 # interval on seconds to call "refresh" function
        self._activationPin="2" # !!!this must be imported from the configuration file
        self._analogPin="A1"  # !!!this must be imported from the configuration file
        self._data=""


    def refresh(self,currentTime):
        self._controller.sendReceiveData("high"+self._activationPin)
        response = self._controller.sendReceiveData(self._analogPin)
        self._controller.sendReceiveData("low"+self._activationPin)

        if len(response.split())!=2:
            return str(int(self._intervalRefresh)+5)

        if response.split()[1]==self._analogPin:
            adConverter = int(response.split()[0])
        else:
            return str(int(self._intervalRefresh)+5) # decrease the refresh time to retest to get a correct response from the microcontroller

        self._data=str(int(adConverter*(-0.3251)+332.6))
        return str(int(currentTime)+self._intervalRefresh)
