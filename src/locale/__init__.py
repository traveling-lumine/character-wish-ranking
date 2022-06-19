from enum import IntEnum, auto


# noinspection PyArgumentList
class LocaleEnum(IntEnum):
    en = auto()
    kr = auto()


# noinspection PyArgumentList
class StringId(IntEnum):
    initial_pity_prompt = auto()
    initial_guarantee_prompt = auto()
    init_state_info = auto()
    wishes_prompt = auto()
    cutoff_prompt = auto()
    ignore_loses_prompt = auto()
    running_process_info = auto()
    review_result_info = auto()
    desired_pickups_prompt = auto()
    desired_loses_prompt = auto()
    desired_guarantees_prompt = auto()
    desired_pity_prompt = auto()
    state_ranking = auto()
    not_found = auto()
    enter_integer = auto()
    language_prompt = auto()
    language_not_found = auto()
    state_desc_format = auto()
    invalid_input = auto()


class Locale:
    _cur = LocaleEnum.en
    locale_dict = {
        StringId.invalid_input: {
            LocaleEnum.en: "Invalid input.",
            LocaleEnum.kr: "올바르지 않은 입력입니다."
        },
        StringId.state_desc_format: {
            LocaleEnum.en: "[{0} pickups, {1} loses, isGuaranteed {2}, {3} pity]",
            LocaleEnum.kr: "[픽업 {0}회, 픽뚫 {1}회, 확천 {2}, 스택 {3}]"
        },
        StringId.language_prompt: {
            LocaleEnum.en: "Select language[en/kr]: ",
            LocaleEnum.kr: "언어를 선택하세요[en/kr]: "
        },
        StringId.language_not_found: {
            LocaleEnum.en: "Choose one of [en/kr].",
            LocaleEnum.kr: "[en/kr] 중 하나를 선택하세요."
        },
        StringId.initial_pity_prompt: {
            LocaleEnum.en: "Initial pity: ",
            LocaleEnum.kr: "초기 스택 수: "
        },
        StringId.initial_guarantee_prompt: {
            LocaleEnum.en: "Initial guarantee [1/0]: ",
            LocaleEnum.kr: "초기 확천 여부 [1/0]: "
        },
        StringId.init_state_info: {
            LocaleEnum.en: "Starting from pity {0} and guarantee {1}",
            LocaleEnum.kr: "초기 스택 수 {0} 초기 확천 여부 {1}로 계산 시작"
        },
        StringId.wishes_prompt: {
            LocaleEnum.en: "Wishes: ",
            LocaleEnum.kr: "뽑기 횟수: "
        },
        StringId.cutoff_prompt: {
            LocaleEnum.en: "Max #pickup (stops pulling when #pickup reaches this. "
                           "Use (#of your pickups, including constellations) + 1 most of the time. "
                           "-1 for unlimited run (strongly not recommended)): ",
            LocaleEnum.kr: "픽업 수 상한 (뽑기 과정 중 픽업 수가 이것을 넘으면 뽑기를 중지합니다. "
                           "대체로 (별자리 포함해서 보유중인 픽업 수) + 1을 입력하세요. "
                           "무제한은 -1을 입력하세요.(-1은 매우 권장하지 않음)): "
        },
        StringId.ignore_loses_prompt: {
            LocaleEnum.en: "Ignore #loses [1/0 (0 strongly not recommended)]: ",
            LocaleEnum.kr: "픽뚫 수를 무시할까요? [1/0 (0은 매우 권장하지 않음)]: "
        },
        StringId.running_process_info: {
            LocaleEnum.en: "Running process... ",
            LocaleEnum.kr: "뽑기 진행중... "
        },
        StringId.review_result_info: {
            LocaleEnum.en: '=== Calculation done. Starting review... ===',
            LocaleEnum.kr: '=== 계산 완료. 리뷰 시작... ==='
        },
        StringId.desired_pickups_prompt: {
            LocaleEnum.en: "Desired pickups (-1 for any): ",
            LocaleEnum.kr: "원하는 픽업 횟수 (-1 = 아무거나): "
        },
        StringId.desired_loses_prompt: {
            LocaleEnum.en: "Desired loses (-1 for any): ",
            LocaleEnum.kr: "원하는 픽뚫 횟수 (-1 = 아무거나): "
        },
        StringId.desired_guarantees_prompt: {
            LocaleEnum.en: "Desired guarantee [1/0/-1 for any]: ",
            LocaleEnum.kr: "원하는 확천 상태 [1/0/-1 = 아무거나]: "
        },
        StringId.desired_pity_prompt: {
            LocaleEnum.en: "Desired pity (-1 for any): ",
            LocaleEnum.kr: "원하는 스택 수 (-1 = 아무거나): "
        },
        StringId.state_ranking: {
            LocaleEnum.en: "{0} : You lie between top {1}% ({2} on log10 scale) ~ top {3}% ({4} on log10 scale).\n---",
            LocaleEnum.kr: "{0} : 상위 {1}% ~ 상위 {3}% (log10를 취하면 {2} ~ {4}) 에 속합니다.\n---"
        },
        StringId.not_found: {
            LocaleEnum.en: "Not found.\n---",
            LocaleEnum.kr: "상태를 찾을 수 없습니다.\n---"
        },
        StringId.enter_integer: {
            LocaleEnum.en: "Please enter an integer.",
            LocaleEnum.kr: "정수를 입력하세요."
        }
    }

    @classmethod
    def get_str(cls, item, *format_args):
        return cls.locale_dict[item][cls._cur].format(*format_args)
