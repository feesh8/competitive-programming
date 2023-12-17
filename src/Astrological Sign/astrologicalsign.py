import sys
ent = sys.stdin.read()
liste = ent.splitlines()
for i in range(1, len(liste)):
    d, m = liste[i].split()
    d = int(d)
    if m == "Sep":
        if d >= 22:
            print("Libra")
        else:
            print("Virgo")
    elif m == "Oct":
        if d >= 23:
            print("Scorpio")
        else:
            print("Libra")
    elif m == "Nov":
        if d >= 23:
            print("Sagittarius")
        else:
            print("Scorpio")
    elif m == "Dec":
        if d >= 22:
            print("Capricorn")
        else:
            print("Sagittarius")
    elif m == "Jan":
        if d >= 21:
            print("Aquarius")
        else:
            print("Capricorn")
    elif m == "Feb":
        if d >= 20:
            print("Pisces")
        else:
            print("Aquarius")
    elif m == "Mar":
        if d >= 21:
            print("Aries")
        else:
            print("Pisces")
    elif m == "Apr":
        if d >= 21:
            print("Taurus")
        else:
            print("Aries")
    elif m == "May":
        if d >= 21:
            print("Gemini")
        else:
            print("Taurus")
    elif m == 'Jun':
        if d >= 22:
            print("Cancer")
        else:
            print("Gemini")
    elif m == "Jul":
        if d >= 23:
            print("Leo")
        else:
            print("Cancer")
    elif m == "Aug":
        if d >= 23:
            print("Virgo")
        else:
            print("Leo")