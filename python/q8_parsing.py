#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

# Team, Games, Wins, Losses, Draws, Goals, Goals Allowed, Points

import csv

f = open('football.csv', 'r')
read = list(csv.reader(f))[1:]
for i in read:
    i[1:] = list(map(lambda x : int(x), i[1:]))
football = {i[0] : i[1:] for i in read}

def get_min_score_difference(football):
    diff = [ [k, abs(v[4]-v[5])] for k,v in list(football.items())]
    return sorted(diff, key = lambda x : x[1])[0]

print(get_min_score_difference(football))