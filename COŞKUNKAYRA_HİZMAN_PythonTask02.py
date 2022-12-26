print( "Welcome, please enter the weight values of the items you want to buy")

appl = float(input( "Apple:"))
banan = float(input( "Banana:"))
stbery = float(input( "Strawberry:"))
orang = float(input( "Orange:"))

if appl<= 10:
    appl1 = (appl * 14 )

elif appl> 10:
     appl1 = (appl * 10 )

if banan<= 5:
    banan1 = (banan * 44)

elif banan> 5:
    banan1 = (banan * 42)

if stbery<= 5:
    stbery1 = (stbery * 60)

elif stbery> 5:
    stbery1 = (stbery * 50)


if orang<= 10:
    orang1 = (orang * 20)

elif orang> 10:
    orang1 = (orang * 15)

toplam = (appl1 + banan1 + stbery1 + orang1)
print("Your total is:", toplam)
#----------------

print("Please enter your information below")

name = (input( "Name:"))
finalg = float(input( "Final Grade:"))
midg = float(input( "Midterm Grade:"))
labg = float(input( "Lab Grade:"))

totalgrade = (finalg * 0.4 + midg * 0.3 + labg * 0.3)

if totalgrade<= 50:
    lettergrade = ("F")

elif totalgrade<= 60:
    lettergrade = ("DD")

elif totalgrade<= 70:
    lettergrade = ("DC")

elif totalgrade<= 75:
    lettergrade = ("CC") 


elif totalgrade<= 80:
    lettergrade = ("CB")

elif totalgrade<= 85:
    lettergrade = ("BB")
    
elif totalgrade<= 90:
    lettergrade = ("BA")

elif totalgrade<= 100:
    lettergrade = ("AA")

print(name, "Your total grade is:", totalgrade, "and your letter grade is:", lettergrade )