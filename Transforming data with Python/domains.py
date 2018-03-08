import read

df = read.load_data()

domains = df['url'].value_counts()


#top_100_domains = domains[0:100]
#for name. row in domains.items():
    #print("{0}: {1}".format(name, row))

def stripsub(st): 
    s = str(st).split('.') 
    l = len(s)
    return s[l-2]+'.'+s[l-1]


df['url'] = df["url"].apply(stripsub) 

domains = df["url"].value_counts() 

for name, row in domains.items(): 
    print("{0}: {1}".format(name, row))

        
    
