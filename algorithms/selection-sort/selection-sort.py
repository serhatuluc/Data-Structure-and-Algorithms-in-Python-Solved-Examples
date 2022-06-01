
#def find_min_element(arr):
#    min=1000000000000
#    for i in range(len(arr)):
#        if arr[i]<min:
#            min=arr[i]
#    return min

def selection_sort(elements,key):
    size = len(elements)

    for i in range(size):
        min_index=i
        for j in range(min_index+1,size):
            if elements[j][key]<elements[min_index][key]:
                min_index=j
        if i!=min_index:
            elements[i][key],elements[min_index][key]=elements[min_index][key],elements[i][key]

    for i in elements:
       print(i)



if __name__=='__main__':
    elements=[{'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}]

    selection_sort(elements,key='First Name')
   
    