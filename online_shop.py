def compute_totals(orders):
    result = []
    for order in orders:
        total_price = order['quantity'] * order['price_per_item']
        if total_price < 100:
            total_price += 10
        result.append((order['id'], total_price))
    return result
orders = [
    {
        'id': 'order_001',
        'item': 'Introduction to Python',
        'quantity': 1,
        'price_per_item': 32,
    },
    {
        'id': 'order_002',
        'item': 'Advanced Python',
        'quantity': 3,
        'price_per_item': 40,
    },
    {
        'id': 'order_003',
        'item': 'Python web frameworks',
        'quantity': 2,
        'price_per_item': 51,
    },
]


totals = compute_totals(orders)
print(totals)