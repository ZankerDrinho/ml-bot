from config import MIN_DISCOUNT, MAX_PRICE, CATEGORY

# Calcular desconto:
def check_offer(product):
    return (product["old_price"] - product["price"]) / product["old_price"] * 100

# Verificar se é uma boa oferta:
def is_good_offer(product, discount):
    return (
        discount >= MIN_DISCOUNT and
        product["category"] == CATEGORY and
        product["price"] <= MAX_PRICE
    )
    
def analyze_offer(products):
    for product in products:
        discount = round(check_offer(product), 2)

        if is_good_offer(product,discount):
            message = f"""
        OFERTA ENCONTRADA!

        {product["name"]}
        De: R${product["old_price"]}
        Por: R${product["price"]}
        Desconto: {discount}%
        
        Confira a oferta:
        {product["link"]}
        """
            print(message)
