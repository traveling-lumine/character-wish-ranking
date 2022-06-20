from dataclasses import dataclass

from src.locale import Locale, StringId


@dataclass(frozen=True)
class State:
    pity: int
    guarantee: bool
    pickups: int
    loses: int

    def __str__(self):
        return Locale.get_str(StringId.state_desc_format, self.pickups, self.loses, self.guarantee, self.pity)
