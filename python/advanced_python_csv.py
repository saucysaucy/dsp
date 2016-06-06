#Write email addresses from Part I to csv file
import csv
from advanced_python_regex import email_list
import pandas as pd

with open('emails.csv', 'w') as out:
    write = csv.writer(out)
    for i in email_list:
        out.write(i)
        out.write('\n')
out.close()



'''
with open('a.csv', 'wb') as b:
    writer = csv.writer(b)
    for line, row in enumerate(bottle_list):
         data = line_to_override.get(line, row)
         writer.writerow(data)
'''