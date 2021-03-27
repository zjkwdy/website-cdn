import os
import pypinyin
from zhon.hanzi import punctuation

files=os.listdir()

for file in files:
    fileName=''.join(file.split('.')[:-1])
    tuozhanming=''.join(file.split('.')[-1])
    punctuation_str = punctuation
    for punctuation_str in fileName:
        fileName=fileName.replace(punctuation,'')
    pinyined=''.join(pypinyin.lazy_pinyin(fileName))
    print(f'input: {fileName}, fileName: {fileName}, tuozhanName:{tuozhanming}')
    os.rename(file,f"{pinyined}.{tuozhanming}")
    print(f'output: FileName:{pinyined}.{tuozhanming}')
