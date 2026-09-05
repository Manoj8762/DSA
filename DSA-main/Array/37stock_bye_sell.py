

# bruteforce solution
def stock_bye_sell1(price):
    maxi=float('-inf')
    profit=0
    n=len(price)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if price[i]<price[j]:
                profit=price[j]-price[i]
                maxi=max(maxi,profit)
    return maxi

print(stock_bye_sell1([7,2,1,5,6,4,8])) #time complexity=>O(N**2)




#optimal solution
def stock_bye_sell2(arr):
    minimum_price=float('inf')
    max_profit=float('-inf')
    for i in range(0,len(arr)):
        if arr[i]<minimum_price:
            minimum_price=arr[i]
        profit=arr[i]-minimum_price
        max_profit=max(max_profit,profit)
        
    return max_profit
print(stock_bye_sell2([7,2,1,5,6,4,8]))
#time complexity=>O(N)
#space complexity=>O(1)

#optimal solution
def stock_bye_sell3(arr):
    minimum_price=float('inf')
    max_profit=float('-inf')
    for i in range(0,len(arr)):
        minimum_price=min(minimum_price,arr[i])
        max_profit=max(max_profit,arr[i]-minimum_price)
    return max_profit
print(stock_bye_sell3([7,2,1,5,6,4,8]))