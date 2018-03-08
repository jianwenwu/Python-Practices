#figure out which words appear most often in the headlines
import read

from collections import Counter
df = read.load_data()

headlines_list = ''
for i in df['headline']:
    headlines_list += str(i)

#print top 100 most often headlines words
print(Counter(headlines_list.lower().split()).most_common(100))

    