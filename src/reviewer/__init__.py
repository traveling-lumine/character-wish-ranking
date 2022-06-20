from itertools import accumulate
from math import log10, floor

from src.locale import Locale, StringId


class Reviewer:
    def __init__(self, bank, ignore_loses):
        self.desired_pickups = None
        self.desired_loses = None
        self.desired_guarantees = None
        self.desired_pity = None
        self.ignore_loses = ignore_loses
        self.acc_prob = None
        self.prob_sum = None
        self.bank = bank

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
