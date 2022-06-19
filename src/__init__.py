from collections import defaultdict
from itertools import accumulate
from math import log10, floor

from tqdm import trange

from src.locale import Locale, StringId, LocaleEnum
from src.state import State


class Calculator:
    def __init__(self):
        self.prob_sum = None
        self.acc_prob = None
        self.bank = None
        self.cutoff = None
        self.wishes = None
        self.ignore_loses = None
        self.new_dict = None
        self.desired_pickups = None
        self.desired_loses = None
        self.desired_guarantees = None
        self.desired_pity = None

    @staticmethod
    def set_lang():
        while True:
            input_str = input(Locale.get_str(StringId.language_prompt))
            if input_str == 'en':
                Locale._cur = LocaleEnum.en
                break
            elif input_str == 'kr':
                Locale._cur = LocaleEnum.kr
                break
            print(Locale.get_str(StringId.language_not_found))

    def run(self):
        self.set_lang()
        self.init_values()
        self.run_process()
        self.review_result()

    def init_values(self):
        self.init_bank()
        self.init_run_config()

    def init_bank(self):
        initial_pity = self.int_input(Locale.get_str(StringId.initial_pity_prompt))
        initial_guarantee = bool(self.int_input(Locale.get_str(StringId.initial_guarantee_prompt)))
        print(Locale.get_str(StringId.init_state_info, initial_pity, initial_guarantee))
        self.bank = {State(initial_pity, initial_guarantee, 0, 0): 1}

    def init_run_config(self):
        self.wishes = self.int_input(Locale.get_str(StringId.wishes_prompt))
        self.cutoff = self.int_input(Locale.get_str(StringId.cutoff_prompt))
        self.ignore_loses = bool(self.int_input(Locale.get_str(StringId.ignore_loses_prompt)))

    def run_process(self):
        for _ in trange(self.wishes, desc=Locale.get_str(StringId.running_process_info)):
            self.propagate()

    def propagate(self):
        self.new_dict = defaultdict(int)
        for key, value in self.bank.items():
            if self.propagate_cutoff(key, value):
                continue
            self.propagate_pickup(key, value)
            self.propagate_advance(key, value)
        self.bank = self.new_dict
        self.new_dict = None

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

    def review_result(self):
        self.sort_states()
        states, probability = zip(*self.bank)
        self.prob_sum = sum(probability)
        self.acc_prob = list(accumulate(probability))
        print(Locale.get_str(StringId.review_result_info))
        while True:
            self.review_states(states)

    def review_states(self, states):
        self.input_target_state_condition()
        for i, a_state in enumerate(states):
            if self.wrong_state(a_state):
                continue
            self.print_portion(a_state, i)
            break
        else:
            print(Locale.get_str(StringId.not_found))

    def print_portion(self, a_state, i):
        start_info = ('0', '-inf') if i == 0 else self.calc_end(self.acc_prob[i - 1])
        end_info = self.calc_end(self.acc_prob[i])
        print(Locale.get_str(StringId.state_ranking, a_state, *start_info, *end_info))

    def calc_end(self, accumulation):
        log_prob = log10(accumulation) - log10(self.prob_sum)
        prob_string = f'{accumulation * 100 / self.prob_sum:.4f}' if log_prob > -4 \
            else f'{pow(10, log_prob - floor(log_prob)):.4f}e{floor(log_prob) + 2}'
        return prob_string, log_prob

    def sort_states(self):
        self.bank = list(self.bank.items())

        def criteria(x):
            st = x[0]
            return st.pickups, st.loses, 62.5 * st.guarantee + st.pity

        self.bank.sort(key=criteria, reverse=True)

    def input_target_state_condition(self):
        self.desired_pickups = self.si_int(StringId.desired_pickups_prompt)
        if self.ignore_loses:
            self.desired_loses = -1
        else:
            self.desired_loses = self.si_int(StringId.desired_loses_prompt)
        self.desired_guarantees = self.sii_bool(StringId.desired_guarantees_prompt)
        self.desired_pity = self.si_int(StringId.desired_pity_prompt)

    def wrong_state(self, a_state):
        return 0 <= self.desired_pickups != a_state.pickups \
               or 0 <= self.desired_guarantees != a_state.guarantee \
               or 0 <= self.desired_pity != a_state.pity \
               or 0 <= self.desired_loses != a_state.loses

    def sii_bool(self, str_id):
        v = self.si_int(str_id)
        upper = 1 if v > 1 else v
        clamped = -1 if v < -1 else upper
        return clamped

    def si_int(self, str_id):
        return self.int_input(Locale.get_str(str_id))

    @staticmethod
    def int_input(message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print(Locale.get_str(StringId.enter_integer))
