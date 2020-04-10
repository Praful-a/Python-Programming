import numpy as np
import pandas as pd
import csv
from matplotlib import pyplot as plt
from collections import Counter
import os
os.chdir('/Users/praful/desktop/python/Matplotlib/BarCharts/ ')
plt.style.use("fivethirtyeight")


# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

# for row in csv_reader:
#     language_counter.update(row['LanguagesWorkedWith'].split(';'))
for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
# print(languages)
# print(popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use.")

plt.tight_layout()

plt.show()
