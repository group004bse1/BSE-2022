# PROGRAM THAT COMPUTES CHANGE FOR A VENDING MACHINE

# PROGRAM START
print('Welcome to the vending machine change maker program.\nChange maker initialized.')

# INITIAL STOCK
nickel_stock = 25
dime_stock = 25
quarter_stock = 25
ones_stock = 0
fives_stock = 0

# WHILE LOOP TO ALLOW MULTIPLE INPUTS UNTIL USER QUITS BY ENTERING 'q'
while True:

    # PRINTING STOCK
    print('\nStock contains:')

    print(round(nickel_stock), 'Nickels')
    print(round(dime_stock), 'Dimes')
    print(round(quarter_stock), 'Quarters')
    print(round(ones_stock), 'Ones')
    print(round(fives_stock), 'Fives')

    # WHILE LOOP TO ALLOW USER TO ENTER PRICE THAT BREAKS WHEN USER ENTERS THE CORRECT PRICE
    # THE PRICE MUST BE NON-NEGATIVE MULTIPLE OF 5 CENTS
    while True:
        purchase_input = input(
            "\nEnter the purchase price (xx.xx) or 'q' to quit: ")  # 'purchase_input' IS THE USER'S PURCHASE PRICE

        # TRY AND EXCEPT BLOCK TO CAPTURE NON-NUMERIC INPUT
        try:
            purchase_input = float(purchase_input)
            total_cents = round(purchase_input * 100)
            remainder = total_cents % 5
            if purchase_input > 0 and remainder == 0:
                break
            else:
                print('Illegal price: Must be a non-negative multiple of 5 cents.')
        except:
            # IF USER ENTERS 'q' THE PROGRAM PRINTS TOTAL IN STOCK AND QUITS
            if purchase_input == 'q':

                total = nickel_stock * 0.05 + dime_stock * 0.1 + quarter_stock * 0.25 + ones_stock * 1 + fives_stock * 5
                dollars = round(total // 1)
                cents = round((total % 1) * 100)
                print('Total:', dollars, 'dollars and', cents, 'cents')
                quit()
            else:
                print('Invalid input: Please enter numeric non-negative multiple of 5 cents.')

    # DECLARING A NEW VARIABLE 'due' FOR THE AMOUNT DUE WHICH IS EQUAL TO THE USER'S PURCHASE PRICE 'purchase_input'
    due = purchase_input

    print('''\nMenu for deposits:
    'n' - deposit a nickel
    'd' - deposit a dime 
    'q' - deposit a quarter 
    'o' - deposit a one dollar bill 
    'f' - deposit a five dollar bill 
    'c' - cancel the purchase''')

    # WHILE LOOP TO ALLOW USER TO ENTER DEPOSITS ONE AT A TIME UNTIL AMOUNT DUE IS OVER OR IF THE USER CANCELS WITH 'c'
    # IF THE AMOUNT IS OVER OR IF THE USER CANCELS, IT WILL PRINT OUT THE CHANGE OWED TO THE USER
    while True:
        # CONVERTING AMOUNT DUE IN TERMS OF DOLLARS AND CENTS
        dollars = due // 1
        cents = round((due % 1) * 100, 2)
        print('\nPayment due:', round(dollars), 'dollars and', round(cents), 'cents')

        deposit = input('Indicate your deposit: ')

        if deposit == 'n':
            nickel_stock = nickel_stock + 1  # UPDATING AMOUNT IN STOCK
            due = due - 0.05  # DEDUCTING AMOUNT DUE
        elif deposit == 'd':
            dime_stock = dime_stock + 1
            due = due - 0.1
        elif deposit == 'q':
            quarter_stock = quarter_stock + 1
            due = due - 0.25
        elif deposit == 'o':
            ones_stock = ones_stock + 1
            due = due - 1
        elif deposit == 'f':
            fives_stock = fives_stock + 1
            due = due - 5
        elif deposit == 'c':  # IF USER ENTERS 'c' TO CANCEL,
            change = purchase_input - due  # CHANGE = PURCHASE PRICE - REMAINING AMOUNT DUE

            print('\nPlease take the change below.')

            # FOR QUARTERS:
            quarters_change = change // 0.25  # CALCULATING NUMBER OF WHOLE QUARTERS FOR CHANGE
            quarters_remainder = round(change % 0.25, 2)  # CALCULATING REMAINDER FOR THE CHANGE

            # CHECKING IF CHANGE OF QUARTERS IS NOT GREATER THAN WHAT IS IN STOCK
            qqq = quarter_stock - quarters_change  # qqq-QUARTERS THAT WILL REMAIN IN STOCK AFTER CHANGE IS DEDUCTED
            if qqq < 0:
                quarters_change = quarter_stock  # IF CHANGE IS GREATER THAN WHAT IS IN STOCK, GIVE OUT ALL QUARTERS IN STOCK FOR CHANGE
                quarters_remainder = abs(
                    qqq) * 0.25 + quarters_remainder  # UPDATING QUARTERS REMAINDER BY ADDING EXCESS QUARTERS THAT WERE NOT IN STOCK
                quarter_stock = 0  # UPDATING QUARTERS IN STOCK TO 0 SINCE ALL WERE GIVEN OUT AS CHANGE
                pass
            else:
                quarter_stock = qqq  # IF STOCK IS NOT EXCEEDED, STOCK 'quarter_stock' = 'qqq'-QUARTERS THAT WILL REMAIN IN STOCK AFTER CHANGE IS DEDUCTED
                pass

            if quarters_change != 0:
                print(round(quarters_change), 'quarters')
            else:
                pass

            # FOR DIMES:
            dimes_change = quarters_remainder // 0.1
            dimes_remainder = round(quarters_remainder % 0.1, 2)
            ddd = dime_stock - dimes_change
            if ddd < 0:
                dimes_change = dime_stock
                dimes_remainder = abs(ddd) * 0.1 + dimes_remainder
                dime_stock = 0
                pass
            else:
                dime_stock = ddd
                pass

            if dimes_change != 0:
                print(round(dimes_change), 'dimes')
            else:
                pass

            # FOR NICKELS:
            # IF NICKELS IN STOCK GET FINISHED, CHANGE SHOULD BE PRINTED AND REMAINING CHANGE SHOULD BE PICKED FROM STORE MANAGER
            nickels_change = dimes_remainder // 0.05
            nickels_remainder = round(dimes_remainder % 0.05, 2)
            nnn = nickel_stock - nickels_change
            if nnn < 0:
                nickels_change = nickel_stock
                nickels_remainder = abs(nnn) * 0.05 + nickels_remainder
                nickel_stock = 0
            else:
                nickel_stock = nnn
                pass

            if nickels_change != 0:
                print(round(nickels_change), 'nickels')
            else:
                pass

            if nickels_remainder != 0:
                # CONVERTING REMAINING CHANGE IN TERMS OF X DOLLARS AND Y CENTS
                dollars_change = nickels_remainder // 1
                cents_change = round((nickels_remainder % 1) * 100, 2)
                print('Machine is out of change.\nSee store manager for remaining refund.\nAmount due is: ',
                      round(dollars_change), 'dollars and', round(cents_change), 'cents')
                break
            else:
                pass
            break
        else:
            print('Illegal selection:', deposit)

        if due == 0:  # IF THE AMOUNT DUE AFTER USER'S DEPOSIT IS EXACTLY 0, THEN THEY DO NOT REQUIRE ANY CHANGE
            print('\nPlease take the change below.')
            print('\n   No change.')

        elif due < 0:
            change = abs(due)
            print('\nPlease take the change below.')

            # FOR QUARTERS:
            quarters_change = change // 0.25  # CALCULATING NUMBER OF WHOLE QUARTERS FOR CHANGE
            quarters_remainder = round(change % 0.25, 2)  # CALCULATING REMAINDER FOR THE CHANGE

            # CHECKING IF CHANGE OF QUARTERS IS NOT GREATER THAN WHAT IS IN STOCK
            qqq = quarter_stock - quarters_change  # qqq-QUARTERS THAT WILL REMAIN IN STOCK AFTER CHANGE IS DEDUCTED
            if qqq < 0:
                quarters_change = quarter_stock  # IF CHANGE IS GREATER THAN WHAT IS IN STOCK, GIVE OUT ALL QUARTERS IN STOCK FOR CHANGE
                quarters_remainder = abs(
                    qqq) * 0.25 + quarters_remainder  # UPDATING QUARTERS REMAINDER BY ADDING EXCESS QUARTERS THAT WERE NOT IN STOCK
                quarter_stock = 0  # UPDATING QUARTERS IN STOCK TO 0 SINCE ALL WERE GIVEN OUT AS CHANGE
                pass
            else:
                quarter_stock = qqq  # IF STOCK IS NOT EXCEEDED, STOCK 'quarter_stock' = 'qqq'-QUARTERS THAT WILL REMAIN IN STOCK AFTER CHANGE IS DEDUCTED
                pass

            if quarters_change != 0:
                print(round(quarters_change), 'quarters')
            else:
                pass

            # FOR DIMES:
            dimes_change = quarters_remainder // 0.1
            dimes_remainder = round(quarters_remainder % 0.1, 2)
            ddd = dime_stock - dimes_change
            if ddd < 0:
                dimes_change = dime_stock
                dimes_remainder = abs(ddd) * 0.1 + dimes_remainder
                dime_stock = 0
                pass
            else:
                dime_stock = ddd
                pass

            if dimes_change != 0:
                print(round(dimes_change), 'dimes')
            else:
                pass

            # FOR NICKELS:
            # IF NICKELS IN STOCK GET FINISHED, CHANGE SHOULD BE PRINTED AND REMAINING CHANGE SHOULD BE PICKED FROM STORE MANAGER
            nickels_change = dimes_remainder // 0.05
            nickels_remainder = round(dimes_remainder % 0.05, 2)
            nnn = nickel_stock - nickels_change
            if nnn < 0:
                nickels_change = nickel_stock
                nickels_remainder = abs(nnn) * 0.05 + nickels_remainder
                nickel_stock = 0
            else:
                nickel_stock = nnn
                pass

            if nickels_change != 0:
                print(round(nickels_change), 'nickels')
            else:
                pass

            if nickels_remainder != 0:
                # CONVERTING REMAINING CHANGE IN TERMS OF X DOLLARS AND Y CENTS
                dollars_change = nickels_remainder // 1
                cents_change = round((nickels_remainder % 1) * 100, 2)
                print('Machine is out of change.\nSee store manager for remaining refund.\nAmount due is: ',
                      round(dollars_change), 'dollars and', round(cents_change), 'cents')
                break
            else:
                pass
            break
        else:
            pass
