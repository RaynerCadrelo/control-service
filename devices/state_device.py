from .base import BaseDevice


class StateDevice(BaseDevice):
    @property
    def state(self):
        return self._state
