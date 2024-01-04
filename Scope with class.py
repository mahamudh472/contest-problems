class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None
    def computeDifference(self):
        self.__elements.sort()
        result = self.__elements[-1] - self.__elements[0]
        self.maximumDifference = result
        return result
	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)