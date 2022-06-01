def insertion_sort(elements):
    median=[elements[0]]
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
            elements[j+1] = anchor
        if i%2==1:
            median.append((elements[(i//2)+1]+elements[(i//2)])/2)
        elif i%2==0:
            median.append(elements[(i//2)])
    print(median)
        

if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5]
    insertion_sort(elements)
    
    