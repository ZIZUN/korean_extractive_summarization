import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-filename", default='result_1209_1236_step_13000.candidate.jsonl', type=str)

with open(filename, 'r') as file:
    json_list = list(file)

sents = []
idxs = []

for li in json_list:
    result =json.loads(li)

    ext_sents = result['extract_sents']
    ext_idx = json.loads(result['ext_idx'])

    print(ext_idx)
    temp = 0
    if len(ext_idx) ==3:
        if ext_idx[0] > ext_idx[1]:
            ext_idx[0], ext_idx[1] = ext_idx[1], ext_idx[0]
            ext_sents[0], ext_sents[1] = ext_sents[1], ext_sents[0]
        if ext_idx[0] > ext_idx[2]:
            ext_idx[0], ext_idx[2] = ext_idx[2], ext_idx[0]
            ext_sents[0], ext_sents[2] = ext_sents[2], ext_sents[0]
        if ext_idx[1] > ext_idx[2]:
            ext_idx[1], ext_idx[2] = ext_idx[2], ext_idx[1]
            ext_sents[1], ext_sents[2] = ext_sents[2], ext_sents[1]
    elif len(ext_idx) ==2:
        if ext_idx[0] > ext_idx[1]:
            ext_idx[0], ext_idx[1] = ext_idx[1], ext_idx[0]
            ext_sents[0], ext_sents[1] = ext_sents[1], ext_sents[0]

    sents.append(ext_sents)
    # idxs.append(ext_idx)

    # print(' '.join(ext_sents))

with open('test_summary.json', 'r') as file:
    li = json.load(file)

    for i in range(len(li)):
        print(sents[i])
        li[i]['summary'] = ' '.join(sents[i])
    # print(li)

with open('submission.json', 'w' ,encoding='UTF-8') as file:
    json.dump(li, file, ensure_ascii=False)