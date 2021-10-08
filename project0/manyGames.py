li = ['monopoly', 'risk', 'uno']
print("I like the following games: monopoly, risk, uno")
game = input('What is a game you like you: ')
li.append(game)
while(game != "no"):
    game = input('What is a game you like (type no to stop): ')
    li.append(game)
for item in li:
    print(item)
