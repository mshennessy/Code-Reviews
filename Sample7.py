

#Initialise Lists
peopleList=[]
heightsList=[]

#defines function
def findtallest():
    for i in range(len(heightsList)-1):
        howTall = heightsList.pop((heightsList)-1)
        newheight = heightsList.pop((heightsList)-1)
        if newHeight > howTall:
            howTall = newHeight
    print(HowTall, "is the tallest")




# Boolean finished controls while loop
finished = False
while not finished:
    #asks user for name
    person=input("Enter a name: ").capitalize()
    if person == "":
        finished = True
    else:
        height=input("Enter their height (eg: 1.73): ")

    #adds name to the 'peopleList' and height to 'heightsList'
    peopleList.append(person)
    heightsList.append(height)
    #ends loop if the user inputs nothing or presses enter



#creates spacing for output
indent = ("       ")

#removes '' from output
del peopleList[len(peopleList)-1]

#prints chart
print("Name", indent, "Height")
for i in range(len(peopleList)):
    print(peopleList.pop(len(peopleList)-1), indent, heightsList.pop(len(heightsList)))
findTallest(heightsList)


    

        
   