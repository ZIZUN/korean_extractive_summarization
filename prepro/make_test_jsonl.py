import json
import tqdm
import jsonlines
from kss import split_sentences

with open('test_summary.json', 'r') as data:
    data = json.load(data)

    article_original = []
    abstractive = []
    category = []
    extractive = []

    for example in tqdm.tqdm(data):
        try:
            original = split_sentences(example['original'], num_workers=5)
        except:
            original = [example['original']]

        article_original.append(original)
        abstractive.append('')
        category.append(example['Meta']['category'])  # novel, cul_ass, news_r, briefing

        extractive.append([0,0,0])


with open('test.jsonl', 'w') as file:
    for i in range(len(article_original)):
        dic = {}
        dic['category'] = category[i]
        dic['id'] = i
        dic['article_original'] = article_original[i]
        dic['extractive'] = extractive[i]
        dic['abstractive'] = abstractive[i]

        file.write(json.dumps(dic) + '\n')
        # if i==500:
        #     break
