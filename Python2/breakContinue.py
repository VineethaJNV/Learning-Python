i = 1

while(i<=10):
    if(i %3==0):
        i+=1
        continue

    if(i==6):
        break
    print(i*5)
    
    i+=1