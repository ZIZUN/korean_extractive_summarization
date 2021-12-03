import json
import tqdm
import jsonline

with open('news_valid_original.json', 'r') as data:
    data = json.load(data)

    article_original = []
    extractive = []
    for doc in tqdm.tqdm(data['documents']):
        temp_doc = []
        for text in doc['text']:
            for sent in text:
                temp_doc.append(sent['sentence'])
        article_original.append(temp_doc)
        extractive.append(doc['extractive'])

with open('train.jsonl', 'w') as file:
    for i in range(len(article_original)):
        dic = {}
        dic['media'] = 'NULL'
        dic['id'] = i
        dic['article_original'] = article_original[i]
        dic['abstractive'] = 'NULL'
        dic['extractive'] = extractive[i]
        dic['extractive_sent'] = []
        for num in extractive[i]:
            if num==None:
                continue

            dic['extractive_sent'].append(dic['article_original'][int(num)])


        file.write(json.dumps(dic) + '\n')
