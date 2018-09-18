import time
loadout = {
    'primary_weapon' : "Assult Rifles",
    'seconday_weapon' : "Pistols", 
    'perks' : "Quick revive, Scavenger",
    'medkit' : "1",
    }
exp_information = {
    'current_exp' : 5000,
    'exp_needed' : 200000,
    'current_level' : 23,
    }
info = input("press (f) to get loadout informatioin: "
             "press (e) to get exp information"
             "or press (h) for controls")
if info == "f":
    print("loading...")
    time.sleep(.5)
    print(loadout)
elif info == "e":
    print("loading...")
    time.sleep(.5)
    print(exp_information)    

    
    
    




    
    
    
        
    
