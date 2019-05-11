class BinarySearch(object):

    def binarySearch(self,alist,item):
        first = 0
        last = len(alist) - 1
        middle = len(alist)/2
        found = False

        while first < last and not found:
            if alist[middle] == item:
                found = True
            else:
                if item < middle:
                    last = middle - 1
                else:
                    first = middle + 1
        return  found

