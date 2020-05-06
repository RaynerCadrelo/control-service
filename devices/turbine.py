from .turn_on_off import TurnOnOfDevise


class TurbineDevise(TurnOnOfDevise):
    ON = "ON"
    OFF = "OFF"

    def __init__(self):
        super().__init__(self.OFF)

    def refresh(self):
        # Implement this method.
        pass
