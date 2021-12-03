import json
import tqdm
import jsonlines
from kss import split_sentences
print('--train set--')

# print(split_sentences('dfdfdf'))

with open('train_summary.json', 'r') as data:
    data = json.load(data)
    original = []
    summary = []
    category = []

    for example in data:
        original.append(example['original'])
        summary.append(example['summary'])
        category.append(example['Meta']['category'])  # novel, cul_ass, news_r, briefing

    print('data num: '+ str(len(original)))
    maxlen = 0
    for doc in original:
        if len(doc) > maxlen:
            maxlen = len(doc)
    print('maxlen: '+ str(maxlen))

    a = 0
    b = 0
    c = 0
    for doc in original:
        if len(doc) < 500:
            a += 1
        elif len(doc) < 1000:
            b += 1
        elif len(doc) < 1500:
            c += 1
    print('< 500 '+ str(a))
    print('< 1000 '+ str(b))
    print('< 1500 '+ str(c))

print('--test set--')

with open('test_summary.json', 'r') as data:
    data = json.load(data)
    original = []
    summary = []
    category = []

    for example in data:
        original.append(example['original'])
        summary.append(example['summary'])
        category.append(example['Meta']['category'])  # novel, cul_ass, news_r, briefing

    print('data num: '+ str(len(original)))
    maxlen = 0
    for doc in original:
        if len(doc) > maxlen:
            maxlen = len(doc)
    print('maxlen: '+ str(maxlen))

    a = 0
    b = 0
    c = 0
    for doc in original:
        if len(doc) < 500:
            a += 1
        elif len(doc) < 1000:
            b += 1
        elif len(doc) < 1500:
            c += 1

    print('< 500 '+ str(a))
    print('< 1000 '+ str(b))
    print('< 1500 '+ str(c))