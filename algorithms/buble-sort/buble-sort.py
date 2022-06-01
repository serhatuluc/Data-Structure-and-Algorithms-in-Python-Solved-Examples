def bubble_sort(elements,key):
    size = len(elements)
    list_of_sorting=[]

    for i in range(size):
        list_of_sorting.append(elements[i][key])
    

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if list_of_sorting[j] > list_of_sorting[j+1]:
                tmp = list_of_sorting[j]
                list_of_sorting[j] = list_of_sorting[j+1]
                list_of_sorting[j+1] = tmp
                swapped = True
    
        if not swapped:
            break
    for i in list_of_sorting:
        for j in range(size):
            if i==elements[j][key]:
                print(elements[j])


if __name__ == '__main__':
    elements = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]
   

    bubble_sort(elements, key='device')
    #bubble_sort(elements, key='name')