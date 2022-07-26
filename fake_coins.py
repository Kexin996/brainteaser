"""
I have to say that it took me two weeks to truly understand each step in this puzzle.

Input:
    coins: a list of number that represents the weight of the coins

Output:
    turns: the maximum number of weighting we gonna take
    fake_coins: return the fake coin
"""

# Note: now it is a simple demo just in order to find the odd in 12 coins
def fake_coins(coins):
    if len(coins) <= 2:
        print("No need to weigh the coins.")
    
    length = (int)(len(coins) / 3)
    # since we split the coins into three piles, we need to do some paritions.
    # we first get our three bags
    bag1 = [3**i for i in range(length) if 3 ** i < length]
    bag2 = [3**i for i in range(length) if 3 ** i < length]
    bag3 = [3**i for i in range(length) if 3 ** i < length]

    # if left < 0, that represents we "borrow" +left coins and put them into bag3
    # if left = 0, that means we don't need to borrow and there is no excess coins either
    # if left > 0, that means we may go back to compare those coins
    left = len(coins) - sum(bag1)*3
    
    # and we keep the signs for genelization
    signs = ['>','<','=']
   
    # we begin our comparison
    
    res1 = 0
    res2 = 0
    index = sum(bag1)

    # we just leave the beginning --- for beginning we need to do two comparisons for the whole three groups
    sum1 = sum(coins[:index])
    sum2 = sum(coins[index:2*index])

    # we need to do recursion for equal situation
    if (sum1 == sum2):
        flag = 3
        # we compare the majority of bag3

        res3 = sum(coins[2*index+1:2*index+bag3[1]+1])-sum(coins[:3])
        if (res3 == 0):
            if (coins[2*index] > coins[0]):
                return ['>',2*index+1]
            else:
                return ['<',2*index+1]
        elif res3 < 0:
            # final internal comparison
            if (coins[2*index+1] == coins[2*index+2]):
                return ['<',2*index+2+1]
            elif (coins[2*index+1] < coins[2*index+2]):
                return ['<',2*index+1+1]
            else:
                return ['<',2*index+1]
        else:
            if (coins[2*index+1] == coins[2*index+2]):
                return ['>',2*index+2+1]
            elif (coins[2*index+1] > coins[2*index+2]):
                return ['>',2*index+1+1]
            else:
                return ['>',2*index+1]

    # if not, we just do cross comparison
    # we leave the lagest element of bag 1
    # and we rotate
    else:
        sign1 = '<' if res1-res2 < 0 else '>'
        res1 = coins[bag1[0]-1]+sum(coins[index+bag2[0]:index+bag2[1]+1])
        res2 = coins[index]+sum(coins[2*index+bag3[0]:2*index+bag3[1]+1])


        if (res1 == res2):
            flag = 1
            res3 = coins[bag1[0]] - coins[bag1[0]+1]
      
            if (res3 == 0):
                return [sign1,bag1[0]+2+1]
            elif (res3 < 0):
                return [sign1,bag1[0]+1+1]
            else:
                return [sign1, bag1[0]+1]


        sign2 = '<' if res1-res2 < 0 else '>'
        if (sign1 == sign2):
            # the candidate becomes the first element in bag1 and bag2
            # we compare them with bag3
            flag = [1,2]
            if coins[bag1[0]-1] == coins[2*index]:
                if sign1 == '>':
                    return ['<',index+bag2[0]]
                else:
                    return ['>',index+bag2[0]]
            else:
                return [sign1,bag1[0]]
        else:
            # that means the only probability is in group 2
            # and we return sign2

            p1 = coins[index+bag2[0]]
            p2 = coins[index+bag2[0]+1]
         
            if (p1 == p2):
                return [sign2,index+bag2[0]+2+1]
            elif (p1 < p2):
                if (sign2 == '>'):
                    return [sign2,index+bag2[0]+1+1]
                else:
                    return [sign2,index+bag2[0]+1]
            else:
                if (sign2 == '>'):
                    return [sign2,index+bag2[0]+1]
                else:
                    return [sign2,index+bag2[0]+1+1]

    return "All coins are the same."
      
# this function return the minimum number of comparisons
import math
def minimum_turns(coins):
    turns = math.log(2*len(coins)+3,3)

    if turns%1 == 0:
        return int(turns)
    else:
        return int(turns)+1



            
        



    
    
        

# testcase
print(fake_coins([1,1,1,1,1,1,1,1,1,1,1,33]))
print(fake_coins([4,1,1,1,1,1,1,1,1,1,1,1]))
print(fake_coins([1,1,1,1,-5,1,1,1,1,1,1,1]))
print(fake_coins([1,1,1,1,1,-6,1,1,1,1,1,1]))

print(minimum_turns([1,1,1,1,1,-6,1,1,1,1,1,1]))

