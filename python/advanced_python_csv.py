#Write email addresses from Part I to csv file
import csv
from advanced_python_regex import email_list
import pandas


out = open('emails.csv', 'w', newline='')
write = csv.writer(out).
for i in email_list:
    write.(i)
out.close()

l = pd.read_csv('emails.csv')

print(l)

i

'''
Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```
'''