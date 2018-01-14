import glob

with open('C:\\Users\\svdbergh\\Repositories\\language_of_taste\\cats.txt', 'a', encoding='iso-8859-1') as out:
    for file in glob.iglob('*.txt'):
        out.write(file + ' ' + 'c8090\n')
