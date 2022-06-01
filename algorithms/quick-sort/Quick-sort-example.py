# implementation of quick sort in python using hoare partition scheme

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = end
    pivot = elements[pivot_index]
    p_index=start
    i=0

    while start < end:
        while start < len(elements) and elements[p_index] <= pivot:
            p_index+=1
        
        p_index=i
        pivot=elements[start]
        while elements[i] < pivot and start < len(elements):
            i+=1
        
        if start < end:
            swap(i, p_index, elements)


    return end


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

 