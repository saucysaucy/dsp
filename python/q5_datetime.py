# Hint:  use Google to find python function
import datetime

format_a = "%m-%d-%Y"
format_b = "%m%d%Y"
format_c = "%d-%b-%Y"

####a)
a_start = datetime.datetime.strptime('01-02-2013', format_a)
a_stop = datetime.datetime.strptime('07-28-2015', format_a)
print((a_start-a_stop))

####b)  
b_start = datetime.datetime.strptime('12312013', format_b)
b_stop = datetime.datetime.strptime('05282015', format_b)
print(b_start-b_stop)

####c)  
c_start = datetime.datetime.strptime('15-Jan-1994',format_c)
c_stop = datetime.datetime.strptime('14-Jul-2015', format_c)
print(c_start-c_stop)