import machine_data as md

def res_check(a):   #function to check resource availability
    for ing,q in md.coffee[a].items():
        for mat,avail in md.resources.items():
            if mat==ing:
                if q>avail:
                    print(f"Sorry not enough {ing} for {a}")
                    return False
    return True

c_ch=''
commands=['off','report']

while c_ch!='off':
    c_ch=input("What would you like?\n(espresso/latte/cappuccino):\n").lower()
    if c_ch=='report':
        for i,j in md.resources.items():
            print(f"{i}: {j}")

    if c_ch in commands:
        continue
    
    if c_ch not in md.coffee.keys():    #to check for accurate inputs
        print("Please enter correct input")
        continue

    elif c_ch in md.coffee.keys():
        if res_check(c_ch) == True: #to ask for coins
            p=int(input("How many pennies?\n"))
            d=int(input("How many dimes?\n"))
            n=int(input("How many nickels?\n"))
            q=int(input("How many quarters?\n"))
            msum=(p*0.01)+(d*0.10)+(n*0.05)+(q*0.25)

            for cof,pr in md.prices.items():
                if cof==c_ch:
                    if msum>=pr:
                        change=msum-pr
                        print(f"Thank you for ordering!\nYour Change is {change}")
                        md.resources['money']+=pr #add money to machine
                        for cof,ing in md.coffee[c_ch].items():
                            for mat,qua in md.resources.items():
                                if cof==mat:
                                    md.resources[mat]-=ing  #deduct machine resources
                        print(f"Here is your {c_ch}!\nPlease Enjoy")
                        continue
                    else:
                        print("Sorry not enough money!\nMoney refunded!!")
