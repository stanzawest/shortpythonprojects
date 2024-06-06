
perc = mark/total*100
roundperc = round(perc, 2) # DO THIS INSTEAD OF WRITING "round(perc,2)" IN EVERY SINGLE print IT IS SOOO MUCH MORE CLEAN
markneed = round(100 - roundperc,2)  #Turns out you can just round here inside of an equasion, nice!

if (roundperc >= 80):
    print("You got", roundperc,"%" " Which is an 'A'","Good job!")
    print("But..")
    print("You would need an extra ", markneed," % to get a 100%")
elif(roundperc >= 70):
    print("You got", roundperc,"%" " Which is an B")
    print("You would need an extra ", markneed," % to get a 100%")
elif(roundperc >= 60):
    print("You got", roundperc,"%" " Which is an C")
    print("You would need an extra ", markneed," % to get a 100%")
elif(roundperc >= 50):
    print("You got", roundperc,"%" " Which is an D")
    print("You would need an extra ", markneed," % to get a 100%")
else:
    print("You got", roundperc,"%" " Which means you did not pass")
    print("You would need an extra ", markneed," % to get a 100%")
    print("(Ｔ▽Ｔ)")
if(markneed == 0.0 or 0):
    print("YOU PERFECTED THAT!! (〜^∇^)〜")
print("-------ALL RESULTS ARE ROUNDED TO 2 DECIMAL PLACES-------")
