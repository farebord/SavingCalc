import math

BUY_TEXT = "You can buy it already."
SAVE_TEXT = "You need to save for {} month{}."

def get_savings():
    return float(input("How much savings do you have? "))

def get_monthly_savings():
    return float(input("How much can you save every month? "))

def get_product_cost():
    return float(input("How much does the product cost? "))

def get_months(savings, monthly_savings, product_cost):
    return math.ceil((product_cost - savings) / monthly_savings) if product_cost > savings else 0

def main():
    MONTHS = get_months(get_savings(), get_monthly_savings(), get_product_cost())
    print(SAVE_TEXT.format(MONTHS, "s" if MONTHS > 1 else "")) if MONTHS >= 1 else print(BUY_TEXT)

if __name__ == "__main__":
    main()