import glob


def inplace_change(filename, old_string, new_string):
    with open(filename, encoding="latin-1") as f:
        s = f.read()
        if old_string not in s:
            print(f'"{old_string}" not found in {filename}')
            return

    with open(filename, 'w', encoding="latin-1") as f:
        print(f'Changing "{old_string}" to "{new_string}" in {filename}')
        s = s.replace(old_string, new_string)
        f.write(s)


for file in glob.iglob('testcorpus/8090/*.txt'):
    inplace_change(f'{file}', '\x92', "'")
