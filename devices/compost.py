from .data_device import DataDevice


class CompostDevice(DataDevice):
    def __init__(self):
        self._intervalRefresh=20
        self._analogPin="A1"
        self._data=""               #data of device

    def refresh(self,currentTime):
        response = self._controller.sendReceiveData(self._analogPin)
        if len(response.split())!=2:
            return str(int(currentTime)+5)

        if response.split()[1]==self._analogPin:
            adConverter = int(response.split()[0])  #the value of analog-digital-converter.
        else:
            return str(int(currentTime)+5)

        self._data=str(round(-0.000010642376258706167*adConverter**2-0.024692321358088184*adConverter+44.223313392346405))
        return str(int(currentTime)+self._intervalRefresh)
