list_input_a = ['1', '2', '3', '4', 'spy']

list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass

print('{}내부에 있는 숫자는'.format(list_input_a))
# ['1', '2', '3', '4', 'spy']내부에 있는 숫자는
print('{}입니다.'.format(list_number))
# ['1', '2', '3', '4']입니다.
