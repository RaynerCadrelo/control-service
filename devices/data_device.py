from .base import BaseDevice


class DataDevice(BaseDevice):
    @property
    def data(self):
        return self._data
