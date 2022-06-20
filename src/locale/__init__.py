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

    thoma = auto()
    diona = auto()
    rosaria = auto()
    beidou = auto()
    sangonomiya_kokomi = auto()
    bennett = auto()
    qiqi = auto()
    shenhe = auto()
    jean = auto()
    noelle = auto()
    kamisato_ayato = auto()
    aloy = auto()
    xiao = auto()
    yelan = auto()
    diluc = auto()
    gorou = auto()
    yun_jin = auto()
    fischl = auto()
    arataki_itto = auto()
    paimon = auto()
    lisa = auto()
    venti = auto()
    naganohara_yoimiya = auto()
    raiden_shogun = auto()
    yae_miko = auto()
    barbara = auto()
    kujou_sara = auto()
    hu_tao = auto()
    tartaglia = auto()
    klee = auto()
    yanfei = auto()
    amber = auto()
    ningguang = auto()
    mona = auto()
    chongyun = auto()
    razor = auto()
    albedo = auto()
    kamisato_ayaka = auto()
    xingqiu = auto()
    xinyan = auto()
    sayu = auto()
    eula = auto()
    kaedehara_kazuha = auto()
    xiangling = auto()
    keqing = auto()
    sucrose = auto()
    kaeya = auto()
    ganyu = auto()
    zhongli = auto()
    happy_birthday = auto()


class Locale:
    _cur = LocaleEnum.en
    locale_dict = {
        StringId.happy_birthday: {
            LocaleEnum.en: "Happy birthday, {0}!",
            LocaleEnum.kr: "{0}, 생일 축하해!"
        },
        StringId.thoma: {
            LocaleEnum.en: "Thoma",
            LocaleEnum.kr: "토마"
        },
        StringId.diona: {
            LocaleEnum.en: "Diona",
            LocaleEnum.kr: "디오나"
        },
        StringId.rosaria: {
            LocaleEnum.en: "Rosaria",
            LocaleEnum.kr: "로자리아"
        },
        StringId.beidou: {
            LocaleEnum.en: "Beidou",
            LocaleEnum.kr: "북두"
        },
        StringId.sangonomiya_kokomi: {
            LocaleEnum.en: "Sangonomiya Kokomi",
            LocaleEnum.kr: "산고노미야 코코미"
        },
        StringId.bennett: {
            LocaleEnum.en: "Bennett",
            LocaleEnum.kr: "베넷"
        },
        StringId.qiqi: {
            LocaleEnum.en: "Qiqi",
            LocaleEnum.kr: "치치"
        },
        StringId.shenhe: {
            LocaleEnum.en: "Shenhe",
            LocaleEnum.kr: "신학"
        },
        StringId.jean: {
            LocaleEnum.en: "Jean",
            LocaleEnum.kr: "진"
        },
        StringId.noelle: {
            LocaleEnum.en: "Noelle",
            LocaleEnum.kr: "노엘"
        },
        StringId.kamisato_ayato: {
            LocaleEnum.en: "Kamisato Ayato",
            LocaleEnum.kr: "카미사토 아야토"
        },
        StringId.aloy: {
            LocaleEnum.en: "Aloy",
            LocaleEnum.kr: "에일로이"
        },
        StringId.xiao: {
            LocaleEnum.en: "Xiao",
            LocaleEnum.kr: "소"
        },
        StringId.yelan: {
            LocaleEnum.en: "Yelan",
            LocaleEnum.kr: "야란"
        },
        StringId.diluc: {
            LocaleEnum.en: "Diluc",
            LocaleEnum.kr: "다이루크"
        },
        StringId.gorou: {
            LocaleEnum.en: "Gorou",
            LocaleEnum.kr: "고로"
        },
        StringId.yun_jin: {
            LocaleEnum.en: "Yun Jin",
            LocaleEnum.kr: "운근"
        },
        StringId.fischl: {
            LocaleEnum.en: "Fischl",
            LocaleEnum.kr: "피슬"
        },
        StringId.arataki_itto: {
            LocaleEnum.en: "Arataki Itto",
            LocaleEnum.kr: "아라타키 이토"
        },
        StringId.paimon: {
            LocaleEnum.en: "Paimon",
            LocaleEnum.kr: "페이몬"
        },
        StringId.lisa: {
            LocaleEnum.en: "Lisa",
            LocaleEnum.kr: "리사"
        },
        StringId.venti: {
            LocaleEnum.en: "Venti",
            LocaleEnum.kr: "벤티"
        },
        StringId.naganohara_yoimiya: {
            LocaleEnum.en: "Naganohara Yoimiya",
            LocaleEnum.kr: "나가노하라 요이미야"
        },
        StringId.raiden_shogun: {
            LocaleEnum.en: "Raiden Shogun",
            LocaleEnum.kr: "라이덴 쇼군"
        },
        StringId.yae_miko: {
            LocaleEnum.en: "Yae Miko",
            LocaleEnum.kr: "야에 미코"
        },
        StringId.barbara: {
            LocaleEnum.en: "Barbara",
            LocaleEnum.kr: "바바라"
        },
        StringId.kujou_sara: {
            LocaleEnum.en: "Kujou Sara",
            LocaleEnum.kr: "쿠죠 사라"
        },
        StringId.hu_tao: {
            LocaleEnum.en: "Hu Tao",
            LocaleEnum.kr: "호두"
        },
        StringId.tartaglia: {
            LocaleEnum.en: "Tartaglia",
            LocaleEnum.kr: "타르탈리아"
        },
        StringId.klee: {
            LocaleEnum.en: "Klee",
            LocaleEnum.kr: "클레"
        },
        StringId.yanfei: {
            LocaleEnum.en: "Yanfei",
            LocaleEnum.kr: "연비"
        },
        StringId.amber: {
            LocaleEnum.en: "Amber",
            LocaleEnum.kr: "엠버"
        },
        StringId.ningguang: {
            LocaleEnum.en: "Ningguang",
            LocaleEnum.kr: "응광"
        },
        StringId.mona: {
            LocaleEnum.en: "Mona",
            LocaleEnum.kr: "모나"
        },
        StringId.chongyun: {
            LocaleEnum.en: "Chongyun",
            LocaleEnum.kr: "중운"
        },
        StringId.razor: {
            LocaleEnum.en: "Razor",
            LocaleEnum.kr: "레이저"
        },
        StringId.albedo: {
            LocaleEnum.en: "Albedo",
            LocaleEnum.kr: "알베도"
        },
        StringId.kamisato_ayaka: {
            LocaleEnum.en: "Kamisato Ayaka",
            LocaleEnum.kr: "카미사토 아야카"
        },
        StringId.xingqiu: {
            LocaleEnum.en: "Xingqiu",
            LocaleEnum.kr: "행추"
        },
        StringId.xinyan: {
            LocaleEnum.en: "Xinyan",
            LocaleEnum.kr: "신염"
        },
        StringId.sayu: {
            LocaleEnum.en: "Sayu",
            LocaleEnum.kr: "사유"
        },
        StringId.eula: {
            LocaleEnum.en: "Eula",
            LocaleEnum.kr: "유라"
        },
        StringId.kaedehara_kazuha: {
            LocaleEnum.en: "Kaedehara Kazuha",
            LocaleEnum.kr: "카에데하라 카즈하"
        },
        StringId.xiangling: {
            LocaleEnum.en: "Xiangling",
            LocaleEnum.kr: "향릉"
        },
        StringId.keqing: {
            LocaleEnum.en: "Keqing",
            LocaleEnum.kr: "각청"
        },
        StringId.sucrose: {
            LocaleEnum.en: "Sucrose",
            LocaleEnum.kr: "설탕"
        },
        StringId.kaeya: {
            LocaleEnum.en: "Kaeya",
            LocaleEnum.kr: "케이아"
        },
        StringId.ganyu: {
            LocaleEnum.en: "Ganyu",
            LocaleEnum.kr: "감우" 
        },
        StringId.zhongli: {
            LocaleEnum.en: "Zhongli",
            LocaleEnum.kr: "종려"
        },
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
