import pandas as pd

faculty = pd.read_csv('faculty.csv')
faculty.rename(columns = {' degree':'degree', ' title':'title', ' email':'email'},inplace=True)
faculty['first name'] = faculty['name'].apply(func = lambda x : x.split(' ')[0])
faculty['last name'] = faculty['name'].apply(func = lambda x : x.split(' ')[-1])
faculty = faculty.drop('name',axis=1)
faculty = faculty[['first name','last name','degree','title','email']]




#Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
deg_map = {
    'phd':'PhD',
    'scd' : 'ScD', 
    'md' : 'MD', 
    'ma' : 'MA',
    'mph' : 'MPH', 
    'bsed' : 'BSEd', 
    'ms' : 'MS', 
    'jd' : 'JD',
    '0' : 'No Degree'
    }
    
faculty['degree'] = faculty['degree']
faculty['degree'] = faculty['degree'].apply(lambda x :x.strip(' ').replace('.','').lower())

deg_list = faculty['degree'].tolist()
deg_list = [i for sub in deg_list for i in sub.split(' ')]
unique_deg = {}
for i in set(deg_list):
    formal = deg_map[i]
    unique_deg[formal] = deg_list.count(i)   
print(sorted(unique_deg.items(),key = lambda x : x[1],reverse=True))
    
#Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

faculty['title'].replace(to_replace='Assistant Professor is Biostatistics',value = 'Assistant Professor of Biostatistics',inplace = True)

print(faculty['title'].value_counts())

#Search for email addresses and put them in a list.  Print the list of email addresses.
email_list = faculty['email'].tolist()
print(email_list)

#Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.
domains = [i.rpartition('@')[-1] for i in email_list]
unique_domains = {}

for i in set(domains):
    unique_domains[i] = domains.count(i)
print(sorted(unique_domains.items(),key = lambda x:x[1],reverse=True))

