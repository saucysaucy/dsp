#Write email addresses from Part I to csv file
import csv
from advanced_python_regex import email_list
import pandas as pd

out = open('emails.csv', 'w', newline='')
write = csv.writer(out)
for i in email_list:
    out.write(i)
out.close()