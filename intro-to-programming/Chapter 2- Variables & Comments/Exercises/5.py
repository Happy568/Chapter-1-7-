# code to calculate how many USB sticks can be bought and remaining balance

def usb_stick_shopping():
    budget = 50  
    price_per_usb = 6  

    
    usb_sticks = budget // price_per_usb

    
    remaining_balance = budget % price_per_usb

   
    print(f"She can buy {usb_sticks} USB sticks.")
    print(f"She will have £{remaining_balance} left.")

usb_stick_shopping()
