def computepay(h,r):
    if h <= 40:
        p = r*h        
    else:
        p = r*40 + (r*1.5*( h -40 ))
    return p

try:
	inp = raw_input("Enter Hours: ")
	hrs = float(inp)
	inp = raw_input("Enter rate per hour: ")
	rate = float(inp)
except:
    print("it's not a correct number")
    quit()
    
    
paym = computepay(hrs,rate)
print paym