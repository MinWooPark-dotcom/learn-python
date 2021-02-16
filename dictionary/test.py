character = {
    'name': '기사',
    'level': 12,
    'items': {
        'sword': '불꽃의 검',
        'armor': '풀플레이트'
    },
    'skill': ['베기', '세게 베기', '아주 세게 베기']
}

for key in character:
    if type(character[key]) is dict:
        for dict_key in character[key]:
            print(dict_key, ': ', character[key][dict_key])
    elif type(character[key]) is list:
        for list_key in character[key]:
            print(character[key], ': ', list_key)
    else:
        print(key, ': ', character[key])
