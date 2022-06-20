import time

from src.locale import StringId, Locale


def generate_happy_birthday():
    str_list = get_str()
    str_list = ', '.join(map(lambda x: Locale.get_str(x), str_list))
    if str_list:
        print(Locale.get_str(StringId.happy_birthday, str_list))


def get_str():
    date_str = time.strftime('%m-%d')
    if date_str == '01-09':
        return [StringId.thoma]
    elif date_str == '01-18':
        return [StringId.diona]
    elif date_str == '01-24':
        return [StringId.rosaria]
    elif date_str == '02-14':
        return [StringId.beidou]
    elif date_str == '02-22':
        return [StringId.sangonomiya_kokomi]
    elif date_str == '02-29':
        return [StringId.bennett]
    elif date_str == '03-03':
        return [StringId.qiqi]
    elif date_str == '03-10':
        return [StringId.shenhe]
    elif date_str == '03-14':
        return [StringId.jean]
    elif date_str == '03-21':
        return [StringId.noelle]
    elif date_str == '03-26':
        return [StringId.kamisato_ayato]
    elif date_str == '04-04':
        return [StringId.aloy]
    elif date_str == '04-17':
        return [StringId.xiao]
    elif date_str == '04-20':
        return [StringId.yelan]
    elif date_str == '04-30':
        return [StringId.diluc]
    elif date_str == '05-18':
        return [StringId.gorou]
    elif date_str == '05-21':
        return [StringId.yun_jin]
    elif date_str == '05-27':
        return [StringId.fischl]
    elif date_str == '06-01':
        return [StringId.arataki_itto, StringId.paimon]
    elif date_str == '06-09':
        return [StringId.lisa]
    elif date_str == '06-16':
        return [StringId.venti]
    elif date_str == '06-21':
        return [StringId.naganohara_yoimiya]
    elif date_str == '06-26':
        return [StringId.raiden_shogun]
    elif date_str == '06-27':
        return [StringId.yae_miko]
    elif date_str == '07-05':
        return [StringId.barbara]
    elif date_str == '07-14':
        return [StringId.kujou_sara]
    elif date_str == '07-15':
        return [StringId.hu_tao]
    elif date_str == '07-20':
        return [StringId.tartaglia]
    elif date_str == '07-27':
        return [StringId.klee]
    elif date_str == '07-28':
        return [StringId.yanfei]
    elif date_str == '08-10':
        return [StringId.amber]
    elif date_str == '08-26':
        return [StringId.ningguang]
    elif date_str == '08-31':
        return [StringId.mona]
    elif date_str == '09-07':
        return [StringId.chongyun]
    elif date_str == '09-09':
        return [StringId.razor]
    elif date_str == '09-13':
        return [StringId.albedo]
    elif date_str == '09-28':
        return [StringId.kamisato_ayaka]
    elif date_str == '10-09':
        return [StringId.xingqiu]
    elif date_str == '10-16':
        return [StringId.xinyan]
    elif date_str == '10-19':
        return [StringId.sayu]
    elif date_str == '10-25':
        return [StringId.eula]
    elif date_str == '10-29':
        return [StringId.kaedehara_kazuha]
    elif date_str == '11-02':
        return [StringId.xiangling]
    elif date_str == '11-20':
        return [StringId.keqing]
    elif date_str == '11-26':
        return [StringId.sucrose]
    elif date_str == '11-30':
        return [StringId.kaeya]
    elif date_str == '12-02':
        return [StringId.ganyu]
    elif date_str == '12-31':
        return [StringId.zhongli]
    else:
        return []
