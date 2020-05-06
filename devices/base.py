from abc import ABC


class BaseDevice(ABC):

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        
    @abstractmethod
    def refresh(self):
        pass