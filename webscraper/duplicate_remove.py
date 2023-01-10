# loop all files in ../global/data and remove duplicate lines from each
import os

files = os.listdir('../global/data')
for file in files:
    if file.endswith('.txt'):
        print('---- Checking {}'.format(file))
        with open('../global/data/{}'.format(file), 'r') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
            lines = list(set(lines))
            lines = [line + '\n' for line in lines]
            with open('../global/data/{}'.format(file), 'w') as f:
                f.writelines(lines)
        print('------')
