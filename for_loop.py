#Starting with basic example of For LOOP:
#break
clients = ['ab', 'bc' 'cd', 'ef', 'hg']
for client in clients:
    if client == 'ef':
        break
    print(client)
#continue
for client in clients:
    if client == 'ef':
        continue
    print(client)
#Loop In Loop
nums = [1,2]
for client in clients:
    for num in nums: 
        print(client, num)
