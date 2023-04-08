#definning the fucntion cause to equate the elements from high,low and mod list to factor of risk
def cause(x):
	for i in x:
		if i==0:
			print("EVE TEASING")
		if i==1:
			print("LOW CCTV ")
		if i==2:
			print("LOW STREET LIGHTS")
		if i==3:
			print("LOW SHOP FREQUENCY")
		if i==4:
			print("TASMAC SHOP")




#from our website by the button(select yor location)
a=str("3RDAVENUE,PRIYANAGAR")
#opening the database
f=open("cctv.txt","r+")#database containning info of fircases, no of street lights,cctv.shops and tasmac
count_of=[]
# for example count-of=[no of fir,no of cctv,no of streetlights,no of 24/7shops,no of tasmac]
for i in f:
	x=i.split()
	if x[0]==a:
		count_of.append(x[2])
		count_of.append(x[3])
		count_of.append(x[4])
		count_of.append(x[5])
		count_of.append(x[6])
# three list are created to sort out the level of risk and the factor for risk
high=[]
mod=[]
low=[]
#increasing the count of each risk factor to calculate the safety of the streets
danger=0
less=0
moderate=0
x=int(count_of[0])
y=int(count_of[1])
z=int(count_of[2])
e=int(count_of[3])
f=int(count_of[4])
#sorting and calculating the risk
if x>5:
		danger+=1
		high.append(0)
elif x in range(2,5):
		moderate+=1
		mod.append(0)
elif x in range(0,2):
		less+=1
		low.append(0)
if y>=6:
		less+=1
		low.append(1)
elif y in range(3,6):
		moderate+=1
		mod.append(1)
elif y in range(0,3):
		danger+=1
		high.append(1)
if z>=10:
		less+=1
		low.append(2)
elif z in range(5,10):
		moderate+=1
		mod.append(2)
elif z in range(0,5):
		danger+=1
		high.append(3)
if e>1:
		less+=1
		low.append(3)
elif e<=1:
		danger+=1
		high.append(3)
if f>2:
		danger+=1
		high.append(4)
elif f<=2:
		less+=1
		low.append(4)
#print(high,low,mod)
print("_"*25)
if danger>=3:
	print("THE STREET HIGH RISK FACTOR...BEWARE OF")
	cause(high)
elif moderate>2:
	print("THE STREET HAS MODERATE RISK...BE STEADY")
	print("BEWARE OF")
	cause(mod)
else:
	print("THE STREET HAS LOW RISK FACTOR")
	print("AWARE OF")
	cause(low)
	
		
	
