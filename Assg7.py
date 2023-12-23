"""
Aim: In a hackathon organised by coding club of SR University total
30 teams (where, each team comprises of exactly 6 students) participated
in grand finale. This event has organised for 3 days and the total
expenditure was Rs. 2, 47, 600.00. As an organizer the event I would
like to know how much amount spent per day, how much amount spent on
each student per day, and how much amount spent one each student for
all the 3 days. Write a python program to calculate above all and
print all the results in the form of integer.
"""
teams = 30
members = 6
tot_exp = 247600
days = 3
print("Amount spent per day : ", int(247600/days))
print("Amount spent on each student per day : ", int((247600/days)/(teams*members)))
print("Amount spent on each student for 3 days : ", int(247600/(teams*members)))
