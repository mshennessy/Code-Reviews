


# function to find the tallest person in the list.
# it does this by getting index of the biggest height,
# then matching it to the person with that same index
def findTallest(inList):                              #Q.g
    biggestH=heightsList.index(max(inList))
    tallestPerson= peopleList[biggestH]
    return tallestPerson




#Initialise Lists
peopleList=[]
heightsList=[]

# Boolean finished controls while loop
finished = False
while not finished:
    person=input("Enter a name")
    #ending the loop if nothing is entered
    if person=='':                                     #Q.a
        finished = True
    #stops the same name from being entered twice
    elif person in peopleList:                         #Q.f
        print('already in the list!')
    else:
        #capatilising the name
        CapPerson=person.capitalize()
        peopleList.append(CapPerson)                   #Q.b    Q.d
        #getting the height of the person and defining it as a
        #float so it can be used in the function
        height=float(input("Enter their height:"))
        heightsList.append(height)                     #Q.c

#printing the titles of the list with a tab between
print('Name'  '\tHeight')

#printing a list of the people's names followed by their height 
for i in range(len(peopleList)):                       #Q.e
    print(peopleList[i] , '\t ' ,heightsList[i],'meters')


#printing the name of the tallest person by calling the function
print('The talllestt person is' , findTallest(heightsList))