import json
import pypinyin
from zhon.hanzi import punctuation

with open('owo.json','rb+') as jsonfp:
    owos=json.load(jsonfp)
    to_owos=['小黄脸','热词系列一','tv_小电视','良辰美景·不问天','喵','2020拜年祭']
    for owo in to_owos:
        group=owos[owo]
        for content in range(len(group['content'])):
            icon=group['content'][content]['icon']
            img=group['content'][content]['img']
            punctuation_str = punctuation
            for punctuation_str in icon:
                fileName=icon.replace(punctuation,'')
            for punctuation_str in img:
                fileName=img.replace(punctuation,'')
            
            pinyined_icon=''.join(pypinyin.lazy_pinyin(icon))
            pinyined_img=''.join(pypinyin.lazy_pinyin(img))
            print(pinyined_icon,pinyined_img)
            owos[owo]['content'][content]['icon']=pinyined_icon
            owos[owo]['content'][content]['img']=pinyined_img

with open('owo.json','w') as jsonfp:
    json.dump(owos,jsonfp)