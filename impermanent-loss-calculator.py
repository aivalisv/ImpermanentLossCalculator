def calculate():
    print("Impermanent Loss Calculator")
    print("---------------------------")
    current_price = 14.5
    min_price = 14
    max_price = 15
    token_1_in_pool = 100

    print("Current Price: {:.4f}".format(current_price))
    print("Min Price: {:.4f}".format(min_price))
    print("Max Price: {:.4f}".format(max_price))

    sp = current_price ** 0.5
    sa = min_price ** 0.5
    sb = max_price ** 0.5

    L = get_liquidity(token_1_in_pool, sp, sa, sb)
    #print("L: {:.4f}".format(L))


    x_calcualted=calculate_x(L, sp, sa, sb)
    print("Token0 in Pool: {:.4f}".format(x_calcualted))
    print("Token1 in Pool: {:.4f}".format(token_1_in_pool))

    future_price = 14.8
    sp_f = future_price ** 0.5

    x1 = calculate_x(L, sp_f, sa, sb)
    y1 = calculate_y(L, sp_f, sa, sb)

    print("\r\nIf in pool")
    print("--------------")
    print("Token0: {:.4f}".format(x1))
    print("Token1: {:.4f}".format(y1))
    print("Token0 Value: {:.4f}".format(x1*future_price))
    print("All Value: {:.4f}".format(x1*future_price + y1))

    print("\r\nIf not in pool")
    print("------------------")
    print("Token0 Value: {:.4f}".format(x_calcualted*future_price))
    print("All Value: {:.4f}".format(x_calcualted*future_price+token_1_in_pool))
    print("\r\n Loss: {:.4f}".format((x_calcualted*future_price+token_1_in_pool)-(x1*future_price + y1)))



def get_liquidity(y, sp, sa, sb):
    if sp <= sa:
        print("FAILED to calculate")
    elif sp < sb:
        liquidity = get_liquidity_1(y, sa, sp)
    else:
        liquidity = get_liquidity_1(y, sa, sb)
    return liquidity

def get_liquidity_1(y, sa, sb):
    return y / (sb - sa)

def calculate_x(L, sp, sa, sb):
    sp = max(min(sp, sb), sa)     # if the price is outside the range, use the range endpoints instead
    return L * (sb - sp) / (sp * sb)

def calculate_y(L, sp, sa, sb):
    sp = max(min(sp, sb), sa)  
    return L * (sp - sa)   

def main():
    calculate()

if __name__ == "__main__":
    main()

