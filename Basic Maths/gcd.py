'''Calculate and return GCD(Greatest Common Divisor) of two given numbers x and y.

Note :
Numbers should be in range of Integer.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
20 
5
Sample Output 1:
5'''

############### ------BRUTE FORCE APPROACH -------####################
def gcd(n,m):
    for i in range(1,min(n,m)+1):              # Time Complexity: O(N)
        if n%i==0 and m%i==0:                  # Space Complexity: O(1).
            res=i
    print(res)
a=int(input())
b=int(input())
gcd(a,b)

############# ------OPTIMAL APPROACH --------#################
#######################
# EUCLIDEAN ALGORITHM #
#######################
def gcd(n,m):
    while n>0 and m>0:
        if n>m:
            n%=m                           # Time Complexity: O(logɸmin(a,b)), where ɸ is 1.61.                                 .
        else:                              # Space Complexity: O(1)
            m%=n                      
    if n==0:
        print(m)
    else:
        print(n)
a=int(input())
b=int(input())
gcd(a,b)




