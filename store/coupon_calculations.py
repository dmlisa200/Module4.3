def calculate_price(price, cash_coupon, percent_coupon):

    pretax = (price - cash_coupon) - (int(price) * int(percent_coupon)/100)
    tax = pretax * .06
    post_tax = pretax + tax
    if price < 10:
        total_price = post_tax + 5.95

    elif price >= 10 and price < 30:
        total_price = post_tax + 7.95

    elif price >= 30 and price < 50:
        total_price = post_tax + 11.95
    else:
        total_price = post_tax
    return total_price


if __name__ == '__main__':
    customer_name = input("Enter first name: ")
    calculated_total = calculate_price()

    print(customer_name, + " your total is $", + calculated_total)
