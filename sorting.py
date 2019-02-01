def insertion_sort(arr,debug = False):
    position = 1
    count = 0
    if debug:
        print(f"Starting list {arr}")
        while position < len(arr):
            pos = position
            while pos > 0 and arr[pos] < arr[pos-1]:
                arr[pos],arr[pos-1] = arr[pos-1], arr[pos]
                print(arr)
                pos -= 1
                count += 1
            if pos > 0:
                count += 1
            
            position += 1
        print(f'Sorted list {arr}')
        print(f'Number of comparisons: {count}')
    if debug != True:
        while position < len(arr):
            pos = position
            while pos > 0 and arr[pos] < arr[pos-1]:
                arr[pos],arr[pos-1] = arr[pos-1], arr[pos]
                count += 1
                pos -= 1
            position += 1
        print(arr)
        print(f'Number of comparisons: {count}')
        
    
def bubble_sort(arr,debug = False):
    count = 0
    var = True
    if debug:
        print(f"Starting list {arr}")
        while var:
            po = 0
            pos = 1
            var = False
            while pos < len(arr):
                if arr[po] > arr[pos]:
                    print(arr)
                    arr[po] , arr[pos] = arr[pos], arr[po]
                    var = True
                count += 1
                po += 1
                pos += 1
    if debug != True:
        while var:
            po = 0
            pos = 1
            var = False
            while pos < len(arr):
                if arr[po] > arr[pos]:
                    arr[po] , arr[pos] = arr[pos], arr[po]
                    var = True
                count += 1
                po += 1
                pos += 1
        
                
    print(f'Sorted list {arr}')
    print(f'Number of comparisons: {count}')
def selection_sort(arr,debug = False):
    loc = 0
    look = 1
    smol = 0
    count = 0
    if debug:
        print(f"Starting list {arr}")
    while loc != len(arr)-1:
        while look < len(arr):
            if arr[look] < arr[smol]:
                smol = look
                if debug:
                    print(arr)
            look += 1
            count += 1
        arr[loc] ,arr[smol] = arr[smol], arr[loc]
        loc += 1
        smol = loc
        look = loc + 1
    print(f'Sorted list {arr}')
    print(f'Number of comparisons: {count}')
if __name__ == '__main__':
    a = [17,8,12,2,9,6,5]
    l = [2,1,3,4,1,2,3]
    selection_sort(a,True)
    selection_sort(l,True)