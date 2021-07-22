i = 0

while i <= 3:
    print(i)
    i+=1
    
    if i == 3:
        i+=1
        print(f'i is {i} now')
        print('This group of statements is printed because',
              ' the while loop condition is fulfilled at start',
              ' of loop, and even if the condition is violated',
              ' mid loop, the iteration does not break.')
        