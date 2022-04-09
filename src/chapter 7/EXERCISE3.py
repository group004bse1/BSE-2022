file = input('Enter the file name: ')
file = (file + "-short.txt")
try:
    if file == 'na na boo boo':
        print('NA NA BOO BOO TO YOU- You have been punk\'d!')
        exit()
    open_file = open(file,"r")
except FileNotFoundError:
    print(f'File cannot be opened:{file}')
    exit()
count = 0
for line in open_file:
    if line.startswith('X'):
        count += 1
print(f'There were {count} subject lines in {file}')
