"""
This file contains a syimple python code for generalizing the gold_chain cuts problem

Input:
    N: the total number of chains, integer

Output:
    cuts: a list containing each cut point, list

Formula:
    if the length of cuts = current N-1:
        return
    else:
        1. if the number of cuts is even:
            we cut at N/2
        2. if the number of cuts is odd:
            we cut at (N-1)/2-1
## the order of cuts is from left to right

"""

def cut(N):
    # invalid case
    if N <= 1:
        return "We cannot cut. Try again."
    
    cuts = []
    while (N != len(cuts)+1):
        if (N % 2 == 0):
            N = N / 2-1
            cuts.append(N+1)
        else:
            N = (N-1)/2 - 1
            cuts.append(N+1)
    cuts.reverse()
    return cuts

# testcase
print(cut(21))
print(cut(123))


