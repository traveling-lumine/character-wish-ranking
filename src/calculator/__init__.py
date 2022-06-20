from collections import defaultdict

from tqdm import trange

from src.locale import Locale, StringId
from src.state import State


class Calculator:
    def __init__(self, initial_pity, initial_guarantee, wishes, cutoff, ignore_loses):
        self.bank = {State(initial_pity, initial_guarantee, 0, 0): 1}
        self.wishes = wishes
        self.cutoff = cutoff
        self.ignore_loses = ignore_loses
        self.new_dict = None

    def __call__(self):
        if self.new_dict is not None:
            raise RuntimeError('Already called')
        for _ in trange(self.wishes, desc=Locale.get_str(StringId.running_process_info)):
            self.propagate()
        return self.bank

    def propagate(self):
        self.new_dict = defaultdict(int)
        for key, value in self.bank.items():
            if self.propagate_cutoff(key, value):
                continue
            self.propagate_pickup(key, value)
            self.propagate_advance(key, value)
        self.bank = self.new_dict

    def propagate_cutoff(self, key, value):
        if 0 < self.cutoff <= key.pickups:
            cutoff_state = State(0, False, key.pickups, key.loses)
            self.new_dict[cutoff_state] += value * 1000
            return True
        return False

    def propagate_pickup(self, key, value):
        pickup_state = State(0, False, key.pickups + 1, key.loses)
        losing_state = State(0, True, key.pickups, key.loses + 1 if not self.ignore_loses else key.loses)
        star_5 = self.get_5star_chance_when(key.pity)
        if key.guarantee:
            self.new_dict[pickup_state] += value * star_5
        else:
            self.new_dict[losing_state] += value * (star_5 // 2)
            self.new_dict[pickup_state] += value * (star_5 // 2)

    def propagate_advance(self, key, value):
        rest = 1000 - self.get_5star_chance_when(key.pity)
        advance_state = State(key.pity + 1, key.guarantee, key.pickups, key.loses)
        if rest > 0:
            self.new_dict[advance_state] += value * rest

    @staticmethod
    def get_5star_chance_when(pity):
        return min(6 + 60 * max(0, pity - 72), 1000)
