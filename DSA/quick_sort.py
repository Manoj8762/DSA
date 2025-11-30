

def partition(ar,low,high):
    pivot=ar[low]
    i=low+1
    j=high
    while True: ##
        while  i<=high and ar[i]<=pivot:
            i+=1
            
        while j>=low and ar[j]>pivot:
            j-=1
        if i<j:
            ar[i],ar[j]=ar[j],ar[i]
        else:
            break
    ar[low],ar[j]=ar[j],ar[low]
    return j
def quick_sort(ar,low,high):
    if low<high:
        pivot_index=partition(ar,low,high)
        quick_sort(ar,low,pivot_index-1)
        quick_sort(ar,pivot_index+1,high)
    return ar
a=[1, 2, 4, 5, 7, 8, 9, 31, 68]
print(quick_sort(a,0,len(a)-1))



def partition(ar, low, high):
    pivot = ar[low]
    i = low + 1
    j = high
    while True:
        while i <= high and ar[i] <= pivot:
            i += 1
        while j >= low and ar[j] > pivot:
            j -= 1
        if i < j:
            ar[i], ar[j] = ar[j], ar[i]
        else:
            break
    ar[low], ar[j] = ar[j], ar[low]
    return j

def quick_sort(ar, low, high):
    if low < high:
        pivot_index = partition(ar, low, high)
        quick_sort(ar, low, pivot_index - 1)
        quick_sort(ar, pivot_index + 1, high)
    return ar

a = [1, 2, 4, 5, 7, 8, 9, 31, 68]
print(quick_sort(a, 0, len(a) - 1))


