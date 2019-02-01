# Worst Case Test Runs (in Comparisons), Given A Randomized List of n Integers From 1-1000 (15 Trial Runs Each)
#
#
#
#          n    Bubble            Insertion        Selection
#       ------------------------------------------------------
#       |10^1 |     81     |         33         |      45     |
#       |     |            |                    |             |
#       |10^2 |    9900    |        2746        |     4950    |
#       |     |            |                    |             |
#       |10^3 |   984015   |       259089       |    499500   |
#       |     |            |                    |             |
#       |     |            |                    |             |
#       |-----------------------------------------------------|





from random import randint

def insertion_sort(arr,debug=False):
    comparisonCounter = 0
    for sortedPos in range(1,len(arr)):
        a = arr[sortedPos-1]
        b = arr[sortedPos]
        if a > b:
            comparisonCounter += 1
            arr[sortedPos-1] = b
            arr[sortedPos] = a
            if debug:
                print(arr)
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
                    break
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
            if debug:
                print(arr)
    return comparisonCounter

def test_sorts(n,num_lists):
    bubbleSum = 0
    bubbleAvg = 0
    insertionSum = 0
    insertionAvg = 0
    selectionSum = 0
    selectionAvg = 0
    listBoi = []
    for i in range(n):
        listBoi.append(randint(1,1000))
    bubbleCopy = listBoi[:]
    insertionCopy = listBoi[:]
    selectionCopy = listBoi[:]
    for i in range(num_lists):
        bubbleSum += bubble_sort(bubbleCopy)
        bubbleCopy = listBoi[:]
    bubbleAvg = bubbleSum // n
    for i in range(num_lists):
        insertionSum += insertion_sort(insertionCopy)
        insertionCopy = listBoi[:]
    insertionAvg = insertionSum // n
    for i in range(num_lists):
        selectionSum += selection_sort(selectionCopy)
        selectionCopy = listBoi[:]
    selectionAvg = selectionSum // n
    return ("Bubble Sort: " + str(bubbleAvg) + "\n" +  "Insertion Sort: " +  str(insertionAvg) + "\n" +  "Selection Sort: " +  str(selectionAvg))
    
    
            
            

if __name__ == "__main__":
    print(test_sorts(1000,5))
    
