customers=[]
n=int(input("Enter number of customers:"))

revenue = 0

for i in range(1,n+1):
    print(f"\nCustomer {i}")
    name=input("enter customer name:")
    units = float(input("enter no of units consumed:"))

    if units <=100:
        bill = units*2.5
    elif units <=200:
        bill = (100*2.5) + (units-100) *3.4
    else:
        bill= (100*2.5) +(100*3.4) +(units-200) *5.0
    
    revenue+=bill

    customer_info={
        "Name":name,
        "Units":units,
        "Bill":bill
    }
    customers.append(customer_info)
for customer in customers :
    
    print(f"{customer['Name']:<20}{customer['Units']:<20}{customer['Bill']:10.2f}")
print(f"Total Revenue:{revenue}rs")