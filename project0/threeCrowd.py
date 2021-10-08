li = ['alex', 'ben', 'sam', 'catherine']
def crowd_test(li):
    if(len(li) > 3):
        print('the room is crowded')
    else:
        print('not crowded')
crowd_test(li)
li.pop()
li.pop()
crowd_test(li)

