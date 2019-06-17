class BinarySearch(object):
#Bst algo
# 1define midpoint
# while element not found:
# if element < mid : last= mid -1
# else element > mid : first = mid + 1

    def binarySearch(self,alist,item):
        first = 0
        last = len(alist) - 1
        found = False
        mid = len(alist)/2

        while first < last and not found:
            mid = int((first + last)/2)

            if alist[mid] == item:
                found = True
                return found

            if item < mid:
                last = mid - 1
            else:
                first = mid + 1

        return  found

bst = BinarySearch()
a = [1,2,3,7,22,44,35,77]
print(bst.binarySearch(a,35))
