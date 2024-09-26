trousers = int(input("How many trousers have been bought?: "))
tshirt = int(input("How many T-shirts have been bought?:  "))
vests = int(input("How many vests have been bought?: "))

trousers_calculate = trousers * 70.5
tshirt_calculate = tshirt * 20.89
vest_calculate = vests * 100.3

total = trousers_calculate + tshirt_calculate + vest_calculate

print(f"Total amount to pay: {total}")