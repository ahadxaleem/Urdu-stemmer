def stemmer(temp1):
    eff = 0
    idx = -2
    stem = open("output.txt", 'w', encoding='utf-8')
    for str1 in temp1[::2]:
        idx = idx + 2
        if len(str1) < 4:
            continue
        if str1.endswith(("اں", "ات", "ین", "یں", "وں", "نا")):
            stem.write(str1[:len(str1) - 2] + "\t\t" + str1[len(str1) - 2:]+"\n")
            if str1[:len(str1) - 2] == temp1[idx+1]:
                eff = eff+1
            continue
        elif str1.endswith(("ؤں", "ئیں", "وائے")):
            stem.write(str1[:len(str1) - 3] + "\t\t" + str1[len(str1) - 3:]+"\n")
            if str1[:len(str1) - 3] == temp1[idx+1]:
                eff = eff+1
            continue
        elif str1.endswith(("بندی", "گردی")):
            stem.write(str1[:len(str1) - 4] + "\t\t" + str1[len(str1) - 4:]+"\n")
            if str1[:len(str1) - 4] == temp1[idx+1]:
                eff = eff+1
            continue
        elif str1.startswith(("نو", "بے", "با", "نا", "لا", "پس", "صد", "من")):
            stem.write(str1[2:] + "\t\t" + str1[:2]+"\n")
            if str1[2:] == temp1[idx+1]:
                eff = eff+1
            continue
        elif str1.startswith("غیر"):
            stem.write(str1[3:] + "\t\t" + str1[:3]+"\n")
            if str1[3:] == temp1[idx+1]:
                eff = eff+2
        eff = eff/(len(temp1)/2)*100
        print("Efficiency of stemmer is "+str(eff)+"%")


f = open("urdu.txt", 'r', encoding='utf-8')
x = (f.read()).split()
stemmer(x)
print(x)

