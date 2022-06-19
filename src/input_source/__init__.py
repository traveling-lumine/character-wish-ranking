from typing import Iterable

from src import Locale, StringId


class InputSource:
    def __init__(self):
        self.placeholder = None

    @staticmethod
    def get_input(prompt: str, choices: Iterable[str], default: str) -> str:
        choices = list(map(lambda x: x.casefold(), choices))
        default = default.casefold()
        assert default in choices
        emphasized_choices = map(lambda x: f'{x}*' if x == default else x, choices)
        options = "/".join(emphasized_choices)
        while True:
            kbd = input(f'{prompt}[{options}]')
            if kbd == '':
                return default
            if kbd.casefold() in choices:
                return kbd
            print(Locale.get_str(StringId.invalid_input))
