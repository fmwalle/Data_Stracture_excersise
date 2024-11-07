def calculate_tax(taxable_income: float, brackets: list[tuple[float, float, float]]) -> float:

    if not taxable_income or not brackets:
        return 0
    total=0
    for mini,high,tax in brackets:
        if high<taxable_income:
            val=high-mini
            val=val*tax
            total+=val
        elif taxable_income< high:
            val=taxable_income-mini
            val=val*tax
            total+=val
    return total

taxable_income = 80000
brackets = [(0, 10000, 0.10), (10000, 30000, 0.15), (30000, 60000, 0.25), (60000, float('inf'), 0.35)]
print(calculate_tax(taxable_income, brackets)) 