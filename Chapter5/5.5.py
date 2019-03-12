#5.5
#Debugger : Explain what the following code does?
(n&(n-1)) == 0

n-1 will look like n, except that n's initial 0s will be 1s in n-1 and n's least significant 1 will be 0 in n-1

ex:
n =  abcde1000
n-1= abcde0111

The value n is therefore a power of two.

So, (n&(n-1)) == 0 checks if n is a power of 2(or if n is 0)
