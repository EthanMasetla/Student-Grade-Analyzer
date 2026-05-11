#create a function which will recieve data from the main filecalled reciever
def reciever(student_name, storage):
    
    print("____________________________________________________________________________________________________ ")
    #we wanna calculate the average of each mark using for loops
    for subjects, marks in storage.items():
           print(f'Average in {subjects}:{round((marks["test 1"]+marks["test 2"]+marks["Assignment"])/3, 1)}%')
    
    print(" ")

    #find the overrall Average
    total=0
    for subject, marks in storage.items():
           average=(marks["test 1"] + marks["test 2"] + marks["Assignment"]) / 3
           total= average+total

    print(f'Overall Average:{round(total/len(storage), 1)}%')
    
    print("____________________________________________________________________________________________________  ")
    print(" ")
    #find the subjects which are below 50% as they need Attention
    for subject, marks in storage.items():
            average= ((marks["test 1"] + marks["test 2"] + marks["Assignment"]) / 3)
            
            if average<50 :
                    print(f'{subject}:{round(average,1)}% (This subject needs your attention!!)')