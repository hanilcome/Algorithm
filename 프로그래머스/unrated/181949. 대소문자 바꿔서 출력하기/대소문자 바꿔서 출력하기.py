str = input()
chg = ""
for a in str:
    chg += (a.upper() if a.islower() else a.lower())
    
print(chg)