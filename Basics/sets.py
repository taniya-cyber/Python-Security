#Creation of Set
firewalls_used = {'A', 'B', 'C'}
#Order does NOT matter in sets as they are meant for checking if the value is present in a set or not, and also to check if duplicate values are not there means removing them.
print(firewalls_used) 
print('A' in firewalls_used) #gives True or False. This is known as MEMBERSHIP TEST. And sets are more efficient in this than tuple and list.
#Set operations:
risky_firewalls = {'D', 'A', 'D', 'W'} #if no, output will be set() which means an empty set.
# 1. Intersection method
print(firewalls_used.intersection(risky_firewalls))
# 2. Union and Difference
print(firewalls_used.union(risky_firewalls))
print(firewalls_used.difference(risky_firewalls))