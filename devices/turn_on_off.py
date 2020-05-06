from .base import BaseDevice


class TurnOnOfDevise(BaseDevice):
    def __init__(self, state):
        super().__init__()
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self.state = state