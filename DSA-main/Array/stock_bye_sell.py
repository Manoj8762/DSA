

# bruteforce solution
def stock_bye_sell1(price):
    n=len(price)
    max_profit=float('-inf')
    for i in range(n):
        for j in range(i+1,n):
            if price[i]<price[j]:
                temp=price[j]-price[i]
                max_profit=max(temp,max_profit)
    return max_profit
print(stock_bye_sell1([7,2,1,5,6,4,8])) #time complexity=>O(N**2)

#optimal

def stock_bye_sell2(arr):
    min_price=arr[0]
    max_profit=0
    for price in arr:
        if price < min_price:
            min_price=price
            
        profit=price-min_price
        max_profit=max(max_profit,profit)
        
    return max_profit
print(stock_bye_sell2([7,2,1,5,6,4,8]))
#time complexity=>O(N)
#space complexity=>O(1)


def stock_bye_sell3(arr):
    min_price=float('inf')
    max_profit=0
    for price in arr:
        if price < min_price:
            min_price=price
            
        profit=price-min_price
        max_profit=max(max_profit,profit)
        
    return max_profit
print(stock_bye_sell3([7,2,1,5,6,4,8]))
#time complexity=>O(N)
#space complexity=>O(1)



def stockByeSell(arr):

print(stockByeSell([7,2,1,5,6,4,8]))



