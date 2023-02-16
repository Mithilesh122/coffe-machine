MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
transaction=0
want_more='yes'
while(want_more=='yes'):
        c=input("enter 'espresso','latte' or 'cappuccino'")
        if (c == "report"):
            for key in resources:
                print(f"{key}:{resources[key]}")
            continue

        def check_resource(c,resources):
                if(resources["water"]>=MENU[c]["ingredients"]["water"] and resources["milk"]>=MENU[c]["ingredients"]["milk"] and resources["coffee"]>=MENU[c]["ingredients"]["coffee"]):
                    return(1)
                else:
                    return(0)
        def process_coins(c,resources):
            p=float(input("number of pennie's"))
            d=float(input("number of dime's"))
            n=float(input("number of nickel's"))
            q=float(input("number of quater's"))
            total=p*0.01+d*0.1+n*0.05+q*0.25
            if(total<MENU[c]["cost"]):
                return(0)
            else:
                print(f"here's the change {total-MENU[c]['cost']}")
                return(1)


        if(check_resource(c,resources)==1):
            resources["water"]=resources["water"]-MENU[c]["ingredients"]["water"]
            resources["milk"]=resources["milk"]-MENU[c]["ingredients"]["milk"]
            resources["coffee"]=resources["coffee"]-MENU[c]["ingredients"]["coffee"]
            transaction=1
        else:
            print("no sufficient resources")
            transaction=0
            want_more = (input("enter 'yes' if you want more otherwise 'no'"))
            continue

        if(process_coins(c,resources)==0):
            transaction=0
            print("not enough money")
        else:
            transaction=1
        if(transaction==1):
            print(f"enjoy your {c}")

        want_more=(input("enter 'yes' if you want more otherwise 'no'"))








