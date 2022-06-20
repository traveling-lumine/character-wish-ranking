from calculator import Calculator
from revier import Reviewer
from src.locale import Locale, StringId, LocaleEnum


class Main:
    def __init__(self):
        self.ignore_loses = None

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
        bank = self.run_process()
        rev = Reviewer(bank, self.ignore_loses)
        rev.review_result()

    def run_process(self):
        initial_pity = self.int_input(Locale.get_str(StringId.initial_pity_prompt))
        initial_guarantee = bool(self.int_input(Locale.get_str(StringId.initial_guarantee_prompt)))
        print(Locale.get_str(StringId.init_state_info, initial_pity, initial_guarantee))
        wishes = self.int_input(Locale.get_str(StringId.wishes_prompt))
        cutoff = self.int_input(Locale.get_str(StringId.cutoff_prompt))
        self.ignore_loses = bool(self.int_input(Locale.get_str(StringId.ignore_loses_prompt)))
        calc = Calculator(initial_pity, initial_guarantee, wishes, cutoff, self.ignore_loses)
        return calc()

    @staticmethod
    def int_input(message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print(Locale.get_str(StringId.enter_integer))
