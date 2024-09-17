def calculate_tax(taxable_income, brackets):
    totalTax=0
    for lower,upper,rate in brackets:
        if taxable_income<lower:
            break
        if taxable_income>lower:
            finding_Tax_Rate=min(taxable_income,upper)-lower
            totalTax+=finding_Tax_Rate*rate
    return totalTax
brackets = [(0, 10000, 0.10), (10000, 30000, 0.15), (30000, 60000, 0.25), (60000, float('inf'), 0.35)]
taxable_income = 80000
print(calculate_tax(taxable_income, brackets))         