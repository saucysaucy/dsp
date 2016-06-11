# Write email addresses from Part I to csv file
import csv
from advanced_python_regex import email_list

with open('emails.csv', 'w') as out:
    write = csv.writer(out)
    for i in email_list:
        out.write(i)
        out.write('\n')
out.close()
