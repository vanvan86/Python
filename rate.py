#rate = 10.5
overtime = 1.5
norm = 40

try:
	inp = raw_input("Enter Hours: ")
	h = float(inp)
	inp = raw_input("Enter Rate: ")
	r = float(inp)
except:
	print ("Enter numeric format")
	quit()

    
if h <= 40:
    paym = 40*r
else:
    paym = (h - 40)*r*1.5 + 40*r
    
print paym
