class Fibbonaci(object):


# with recursion
    def fib(self, n):

        if n == 0 or n == 1:
            return n
        else:
            return  self.fib(n-1) + self.fib(n-2)


# with memoization:


    def fibM(self, n, memo):

        if n == 0 or n == 1:
            return n

        if memo[n] == 0:
            memo[n] = self.fibM(n-1,memo)  + self.fibM(n-2, memo)

        return memo[n]

# with bottom up approach:
    def fibB(self,n):
        if n == 0: return

        a = 0
        b = 1

        for x in range(n):
            c = a+b
            a = b
            b = c

        return a+b




f = Fibbonaci()
print(f.fibB(3))
