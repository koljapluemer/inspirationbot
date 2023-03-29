# Purpose: checks whether all versions have the same links

import sys
import os
import re


def main():
    # get all *.html files in the /versions directory (recursive)
    files = []
    for (dirpath, dirnames, filenames) in os.walk('versions'):
        # only add .html files
        files.extend([os.path.join(dirpath, f)
                     for f in filenames if f.endswith('main.html')])

    print(f'Found {len(files)} files in /versions directory')

    for file in files:
        # get all links from the current file
        with open(file, 'r') as f:
            links = re.findall(r'href=\"(.*?)\"', f.read())

  # print file name, including parent dir
  # print bold
        print(f'\033[1m{file}\033[0m')
        for link in links:
            print(link)

if __name__ == '__main__':
    main()
