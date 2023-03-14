def is_leap(year):
    leap = False
    
    # Write your logic here
    if year>=1900 and year<=100000:
        if year%100==0 and year%400==0:
            leap=True
        elif year%100==0 and year%400!=0:
            leap=False
        elif year%4==0:
            leap=True
        else:
            leap=False
    else:
        print("please enter 1900<=year<=100000")
    
    return leap

