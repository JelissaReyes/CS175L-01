#CS175L-01
#Jelissa Reyes
#Stocks

print ("Amount paid for the stock: $80,000.00")
print ("Commission paid on the purchase: $2,400.00")
print ("Amount the stock sold for: $85,500.00")
print ("Commission paid on the sale: $2,565.00")
print ("Profit (or loss if negative): $535.00")
COMMISSION_RATE = float(input("What was the commission rate?" ))
NUM_SHARES = float(input("How many shares did you purchase?"))
PURCHASE_PRICE = float(input("What was the purchasing price?"))
SELLING_PRICE = float(input("What was the selling price?"))
amountPaidForStock = NUM_SHARES * PURCHASE_PRICE
print(f"Amount Paid for Stock $ {amountPaidForStock}")
purchaseCommission = amountPaidForStock * COMMISSION_RATE
print(f"Comission paid on the purchase $ {purchaseCommission}")
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor= NUM_SHARES * SELLING_PRICE
print(f"Amount the Stock sold for $ {stockSoldFor}")
sellingCommission = stockSoldFor * COMMISSION_RATE
print(f"Comission paid on the purchase: $ {sellingCommission}")
totalReceived = stockSoldFor - sellingCommission
totalCommission = purchaseCommission +  sellingCommission
print (f"Total commission paid: $ {totalCommission}")
profitOrLoss = totalReceived - totalPaid
print (f"Profit (or loss if negative) : $ {profitOrLoss}")
