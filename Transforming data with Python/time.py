# when the most articles are submitted
import read
from dateutil.parser import parse

df = read.load_data()

def extract_hour(cols):
    datetime_obj = parse(cols)
    return datetime_obj.hour

df['submission_time'] = df['submission_time'].apply(extract_hour)

hours = df['submission_time'].value_counts()

for name, row in hours.items(): 
    print("{0}: {1}".format(name, row))
    
    