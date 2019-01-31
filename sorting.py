

def insertion_sort(arr,debug=False):
    comparisonCounter = 0
    for sortedPos in range(1,len(arr)):
        a = arr[sortedPos-1]
        b = arr[sortedPos]
        if a > b:
            comparisonCounter += 1
            arr[sortedPos-1] = b
            arr[sortedPos] = a
            for backtrackPos in range(sortedPos-1,0,-1):
                a = arr[backtrackPos-1]
                b = arr[backtrackPos]
                if a > b:
                    comparisonCounter += 1
                    arr[backtrackPos] = a
                    arr[backtrackPos-1] = b
                    if debug:
                        print(arr)
                else:
                    comparisonCounter += 1
        else:
            comparisonCounter += 1
    return comparisonCounter


def bubble_sort(arr,debug=False):
    comparisonCounter = 0
    whole_row = False
    while not whole_row:
        whole_row_counter = 0
        for i in range(0,len(arr)-1):
            a = arr[i]
            b = arr[i+1]
            if a > b:
                comparisonCounter += 1
                arr[i] = b
                arr[i+1] = a
                if debug:
                    print(arr)
            else:
                comparisonCounter += 1
                whole_row_counter += 1
                if (whole_row_counter == len(arr) - 1):
                    return comparisonCounter
                    
                
    
    
def selection_sort(arr,debug=False):
    comparisonCounter = 0
    for originPos in range(0,len(arr)):
        searcher = 0
        a = arr[originPos]
        smallest = a
        for searchingPos in range((originPos + 1), len(arr)):
            b = arr[searchingPos]
            if b < smallest:
                smallest = b
                searcher = searchingPos
            comparisonCounter += 1
        if smallest != a:
            arr[originPos] = smallest
            arr[searcher] = a
    return comparisonCounter
            
            

if __name__ == "__main__":
    listBoi = [17,8,12,2,9,6,5]
    print(bubble_sort(listBoi))
    print(listBoi)
    listBoi = [17,8,12,2,9]
    print(insertion_sort(listBoi))
    print(listBoi)
    listBoi = [17,8,12,2,9,6,5]
    print(selection_sort(listBoi))
    print(listBoi)
    
