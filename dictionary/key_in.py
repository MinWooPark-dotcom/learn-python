dictionary = {
    'name': '망고',
    'type': '당절임',
    'ingredient': ['망고', '설탕'],
    'origin': '필리핀'
}

key = input('접근하고자 하는 키:')

if key in dictionary:
    print(dictionary[key])
else:
    print('존재하지 않는 키')


value = dictionary.get('존재하지 않는 키')
print(value)

if value == None:
    print('존재하지 않는 키에 접근해서 None나옴')
