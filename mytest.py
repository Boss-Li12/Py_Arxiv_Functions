from typing import Dict, List, TextIO

data = open("example_data.txt", 'r')



def read_arxiv_file(f: TextIO):
    print(f.readlines())

read_arxiv_file(data)