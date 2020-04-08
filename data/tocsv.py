import pandas as pd
import json, os
from bz2 import BZ2File

def read_jsonlines(bz2_file):
    text = bz2_file.read().decode('utf-8')
    for line in text.split('\n'):
        if line != '':
            yield line

# Transform to pandas DataFrame
journal = []
date = []
title = []
fulltext = []

input_dir = 'reduced'

for archive in os.listdir(input_dir):
    f = BZ2File(os.path.join(input_dir, archive), 'r')
    articles = list(read_jsonlines(f))

    for art in articles:
        article_dict = json.loads(art)
        # Ignore articles with empty text or title (not for NZZ)
        if (article_dict['title'] or (article_dict['id'][:3] == 'NZZ')) and article_dict['fulltext']:
            journal.append(article_dict['id'][:3])
            date.append(article_dict['date'])
            title.append(article_dict['title'])
            fulltext.append(article_dict['fulltext'])

df = pd.DataFrame.from_dict(
{
    'journal': journal,
    'date': date,
    'title': title,
    'fulltext':fulltext,
})

# Save results to .csv file
df.to_csv('data.csv', index=False)
