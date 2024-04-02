## Euclid's Algorithm for GCD of 2 numbers in Python
## Good info: https://www.csuohio.edu/sites/default/files/85-%202015.pdf

#Idea is if u replace larger number by the remainder of larger/smaller, GCD stays the same
#So the algorithm just does this recursively until remainder is 0
#larger = lrg/sml * smaller + remainder

A = abs(int(input("Specify a: ")))
B = abs(int(input('Specify b: ')))

def _Euclid(a,b):
	while b:
		a, b = b, a%b
	return a
	
def EuclidAlgo(a,b):
	print(f' GCD of {A}, {B}: {_Euclid(a,b)}')
    
EuclidAlgo(A,B)
