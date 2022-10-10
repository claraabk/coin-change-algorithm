""" The function bellow will:
 1. Create an Array for the result we want to obtain
 2. Call a function that return all possible combinations
 3. Create an array for the result we are going to return in the end of the function
 4. Iterate through a loop in which we get the amount of times each coin appears in each combination and append to result Array
    4.1. Create an Array([0,0,0,0]) in which we are going to change each index
    4.2. Creates an Array(coinsValues) with unique values that appear in the combination
    4.3. Count how many times this specific coin appears in the combination
    4.4. Change from 0 to how many times it appear in the Array metioned in 4.1
 5. Return the array making sure no combination is repeated """

def makeChange(coins, total):
    combinations = []

    findPossibilities(combinations, coins, [], total) 
                
    result = []

    for combination in combinations:
        x = [0,0,0,0]

        coinsValues = list(set(combination))

        for coin in coinsValues:

            find = combination.count(coin)

            x[coins.index(coin)] = find
            if x not in result:
                result.append(x)

    return sorted(result)

""" The function bellow will:
 1. Check if the total is zero, if so it means the combination is already made
    1.1. Append the combination to Array of all combinations
    1.2. Return Array of combinations
 2. Iterate through a loop using range of Array of coins
    2.1. Get the difference between total and the coin (if it is positive it means we still need to finish the combination because total is not complete)
    2.2. Append the coin we are using to a temporary array that keeps the combination set
    2.3. Use recursion to continue the combination and change total to the difference we found on 2.1 an the index to the iterarion we are on (to understand which coin we are using at the moment)
    2.4. Remove the coins from the temporary array because it needs to be empty for the next combination """

def findPossibilities(combinations, coins, temp, total, counter = 0):
     
    if total == 0 :
         
        combinations.append(list(temp))
        return combinations
       
    for coin in range(counter, len(coins)):
 
        if total - coins[coin] >= 0:
 
            temp.append(coins[coin])
            findPossibilities(combinations, coins, temp, total-coins[coin], coin)

            temp.remove(coins[coin])

coins = [25, 10, 5, 1]
total = int(input())
combinations = makeChange(coins, total)

print(combinations)
