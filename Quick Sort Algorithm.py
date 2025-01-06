def quick_sort(sequence):
    lenght = len(sequence)
    if lenght <= 1:
        return sequence
    
    pivot = sequence.pop()
    
    items_greater = []
    items_lower = []
    
    for item in sequence:
        if pivot > item:
            items_lower.append(item)
        else: 
            items_greater.append(item)
            
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([6, 46, 59, 46, 70, 56, 60, 60, 57, 79, 63, 41, 30, 17, 61, 39, 45, 89, 51, 74]))