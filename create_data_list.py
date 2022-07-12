import os
import sys

# 取用的语言目录
data_lang = 'Chinese'

# 数据集目录
datasets = 'ace_2005_td_v7'
data_path = os.path.join(datasets, 'data', data_lang)

files = []
with os.scandir(data_path) as dp:
    for item in dp:
        if item.is_file():
            continue
        
        l = []
        with os.scandir(os.path.join(data_path, item.name, 'adj')) as adj:
            for file in adj:
                if file.name.endswith('tab'):
                    l.append(file.path.rsplit('.', 1)[0][len(data_path) + 2 + len('tab') - len(file.path):])
        
        files.append(l)

train = []
dev = []
test = []
for d in files:
    tr = int(len(d) * 0.8)
    de = int(len(d) * 0.1)
    train.extend(d[:tr])
    dev.extend(d[tr:][:de])
    test.extend(d[tr + de - len(d):])

with open(data_lang + '_list.csv', 'w', encoding='utf-8') as filels:
    filels.write('type,path\n')
    for te in test:
        filels.write('test,' + te + '\n')
    for de in dev:
        filels.write('dev,' + de + '\n')
    for tr in train:
        filels.write('train,' + tr + '\n')
