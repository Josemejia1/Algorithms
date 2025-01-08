def bubble(list_a): #Define the function as  "bubble" 
    indexing_lenght = len(list_a) - 1 #Refers to the lenght of the list -1 because the index starts at 0
    sorted = False #Essentially states that the list is not sorted yet
    
    while not sorted:
        sorted = True
        for i in range(0, indexing_lenght):
            if list_a[i] > list_a[i + 1]:
                sorted = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
            
    return list_a

print(bubble([1,4,3,9,6,5,2]))
            