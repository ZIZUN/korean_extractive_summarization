import json
import tqdm
import jsonlines
from kss import split_sentences

with open('train_summary.json', 'r') as data:
    data = json.load(data)

    article_original = []
    abstractive = []
    category = []
    extractive = []

    for example in tqdm.tqdm(data):
        try:
            original = split_sentences(example['original'], num_workers=5)
            summary = split_sentences(example['summary'], num_workers=5)

            temp = 1
            for sent in summary:
                if not (sent in original):
                    temp = 0
                    break
            if temp==0 or len(summary) != 3 or len(original)==0 or len(summary) == 0:
                continue
        except:
            continue

        article_original.append(original)
        abstractive.append(example['summary'])
        category.append(example['Meta']['category'])  # novel, cul_ass, news_r, briefing
        li = []
        for i in range(3):
            li.append(original.index(summary[i]))
        extractive.append(li)


with open('train.jsonl', 'w') as file:
    for i in range(len(article_original)):
        dic = {}
        dic['category'] = category[i]
        dic['id'] = i
        dic['article_original'] = article_original[i]
        dic['extractive'] = extractive[i]
        dic['abstractive'] = abstractive[i]
        dic['extractive_sents'] = []
        for num in extractive[i]:
            if num==None:
                continue

            dic['extractive_sents'].append(dic['article_original'][int(num)])


        file.write(json.dumps(dic) + '\n')
        # if i==500:
        #     break
