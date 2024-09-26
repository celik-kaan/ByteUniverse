land = int(input("Enter price of the land: "))
construction = int(input("Enter price of the building: "))

vat = 0.21

total_price_before_vat = land + construction

vat_amount = total_price_before_vat * vat

total_price_with_vat = total_price_before_vat + vat_amount

print(f"The total house price including VAT is: {total_price_with_vat}")
