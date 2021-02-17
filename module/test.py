import os

output = os.listdir('.')
print('os.listdir():', output)
# file test.py
# file module_urllib.py
# file module.random.py
# file module_os.py
# file module_time.py
# file module_sys.py

print()

for path in output:
    if os.path.isdir(path):
        print('dir', path)
    else:
        print('file', path)
