
def printTopTenEven():
    for i in range(1,11):
        if i%2 == 0 :
            print(i)
            
def printTopTenOdd():
    for i in range(1,11):
        if i % 2 == 1:
            print(i)
            
if __name__ == "__main__":
    print("I am running directly I will shout on Someone")
else:
    print("I am running in-directly I will shout on You all")
