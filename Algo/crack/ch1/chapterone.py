class Chapter:
    def __init__(self):
        print("chapter")


### Question 1.1  Check whether the string is unoque with/without using any data structures

    def checkUnique(self,elem):
        temp = set()
        for s in elem:
            if s not in temp:
                 temp.add(s)
            else:
                return False

        return True

## checck without algo
## check the ascii value of the element in an array and check if it exists
## Solution time complexity : O(N)  space complexity : O(N) or O(126)
    def isUniq(self,elem):
        temp = [False] * 126

        for s in elem:
            if temp[ord(s)]:
                return False
            else:
                temp[ord(s)] = True
        return True


## 1.2 Check if one string is permutation of other string such as GOD = DOG but "DOG   " != GOD

    def isPermutation(self, s1, s2):
        temp = [False] * 128

        s1 = s1.lower()
        s2 = s2.lower()

        for s in s1:
            temp[ord(s)] = True

        for x in s2:
            if not temp[ord(x)]:
                return False
        return True


ch = Chapter()
s1 = "abxd"
print(ch.checkUnique(s1))
print(ch.isUniq(s1))
print("### 1.2 #####")
s1 = "dog"
s2 = "goD "
print(ch.isPermutation(s1,s2))