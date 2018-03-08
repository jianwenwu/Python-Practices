import pandas as pd

def load_data():
    data = pd.read_csv('hn_stories.csv')
    data.columns = ['submission_time', 'upvotes', 'url', 'headline']
    return data


print(load_data().head(2))
print(load_data().columns)