#partition is done in another function
def partition(elements,key,descending):
    size = len(elements)
    list_of_sorting=[]
    
    for i in range(size):
        list_of_sorting.append(elements[i][key])
    merge_sort(list_of_sorting,elements,key,descending)

def merge_sort(arr,elements,key,descending):
    if len(arr) <= 1:
        return 

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left,elements,key,descending)
    merge_sort(right,elements,key,descending)

    merge_two_sorted_lists(left, right, arr)

    #print elements as it is ordered
    #ascending
    if len(arr)==len(elements) and not descending:
        for i in arr:
            for j in range(len(arr)):
                if i==elements[j][key]:
                    print(elements[j])
    #descending
    if len(arr)==len(elements) and descending:
        for i in reversed(arr):
            for j in range(len(arr)):
                if i==elements[j][key]:
                    print(elements[j])
    



def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0
  

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
            
        else:
            arr[k] = b[j]
            j+=1
        k+=1
        

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1
        

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1
    
    



if __name__ == '__main__':
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    partition(elements, key='age',descending=True)
   