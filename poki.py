
# this is a poki game in this game you will find a minimum and maximum number without using a sorting a element 
p = [3,2,7,8]

print("your entered value is ",p)

mini,maxi = 0,0
for num in p:
    if mini == 0 and maxi == 0:
        mini, maxi = p[0],p[0]
        print(mini,maxi)
    else:
        mini = min(mini,num)
        maxi = max(maxi,num)
        print(mini,maxi)
        
        
