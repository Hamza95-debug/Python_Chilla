#while loop
x=0

while(x<5):
    print(x)
    x=x+1

# for loop

for x in range(5,10):
    print(x)

# loop in array
days=["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]

for d in days:
    print(d)

#2 loop in array
days=["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]

for d in days:
    if(d=="Thr"):break #breaks the loop at Thursday
    print(d)

#3 loop in array
days=["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]

for d in days:
    if(d=="Thr"):continue # skip the Thursday and then continue
    print(d)