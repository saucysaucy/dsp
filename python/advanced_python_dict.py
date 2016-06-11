from advanced_python_regex import faculty

print('\n\n\n\n')

faculty_dict = {}
faculty['first name'].astype(str)
for index, [first, last, degree, title, email] in faculty.iterrows():
    if not last in faculty_dict:     
        faculty_dict[last] = [degree,title,email]
    else:
        faculty_dict[last].append([degree,title,email])
    
for i,j in faculty_dict.items():
    print(i,j,sep=' : ',end='\n')


"""

faculty_dict = {
    'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
    'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
    ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]
    }

Print the first 3 key and value pairs of the dictionary:

>> Troxel : ['scd', 'Professor of Biostatistics', 'atroxel@mail.med.upenn.edu']
Landis : ['bsed ms phd', 'Professor of Biostatistics', 'jrlandis@mail.med.upenn.edu']
Hwang : ['phd', 'Associate Professor of Biostatistics', 'whwang@mail.med.upenn.edu']

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],
('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],
('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```
"""

professor_dict = {(first, last) : [degree,title,email] for index, [first, last, degree, title, email] in faculty.iterrows()}

for key, value in professor_dict.items():
    print (key,value,sep=' : ',end='\n')

"""
Print the first 3 key and value pairs of the dictionary:

>> ('Susan', 'Ellenberg') : ['phd', 'Professor of Biostatistics', 'sellenbe@upenn.edu']
('Jinbo', 'Chen') : ['phd', 'Associate Professor of Biostatistics', 'jinboche@upenn.edu']
('A.', 'Localio') : ['jd ma mph ms phd', 'Associate Professor of Biostatistics', 'rlocalio@upenn.edu']
"""

####Q8.  It looks like the current dictionary is printing by first name.
# Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors



for key,value in professor_dict.items():
    print (key[1],value,sep=' : ')


"""
>> Ellenberg : ['phd', 'Professor of Biostatistics', 'sellenbe@upenn.edu']
Chen : ['phd', 'Associate Professor of Biostatistics', 'jinboche@upenn.edu']
Localio : ['jd ma mph ms phd', 'Associate Professor of Biostatistics', 'rlocalio@upenn.edu']

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)
"""
