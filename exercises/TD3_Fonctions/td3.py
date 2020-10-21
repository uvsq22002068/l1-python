
def tempsEnSeconde(temps):
    jts = temps[0]*86400
    hts = temps[1]*3600
    mts = temps[2]*60
    return jts + hts + mts + temps[3]


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))


def secondeEnTemps(seconde):
    sej = seconde // 86400
    seh = seconde // 3600 % 24
    sem = seconde // 60 % 60
    ses = seconde % 60
    return sej, seh, sem, ses


seconde = 100000
print(secondeEnTemps(seconde))


def strJour(temps):
    if temps[0] == 0:
        return " "
    elif temps[0] == 1:
        return "un jour"
    else:
        return str(temps[0]) + " jours"


def strHeure(temps):
    if temps[1] == 0:
        return " "
    elif temps[1] == 1:
        return " , une heure"
    else:
        return ", " + str(temps[1]) + " heures"


def strminute(temps):
    if temps[2] == 0:
        return " "
    elif temps[2] == 1:
        return " , une minute"
    else:
        return ", " + str(temps[2]) + " minutes"


def strseconde(temps):
    if temps[3] == 0:
        return " "
    elif temps[3] == 1:
        return " , une seconde "
    else:
        return ", " + str(temps[3]) + " secondes"


def afficheTemps(temps):
    print(strJour(temps) + strHeure(temps) + strminute(temps) + strseconde(temps))
    

afficheTemps((1, 0, 14, 23))


def demandeTemps():
    jour = int(input("définir un nombre de jours"))
    heure = int(input("définir un nombre  d'heures"))
    minute = int(input("définir un nombre de minutes"))
    seconde = int(input("définir un nombre de secondes"))
    while jour < 0:
        jour = int(input("le nombre de jours est incorrect,redéfinir une valeur"))
    while heure < 0 or heure >= 24:
        heure = int(input("le nombre d'heure est incorrect,redéfinir une valeur"))
    while minute < 0 or minute >= 60:
        minute = int(input("le nombre de minute est incorrect,redéfinir une valeur"))
    while seconde < 0 or seconde >= 60:
        seconde = int(input("le nombre de seconde est incorrect,redéfinir une valeur"))
    return(jour, heure, minute, seconde)


demandeTemps()


def sommeTemps(temps1, temps2):
    Stemps = tempsEnSeconde(temps1) + tempsEnSeconde(temps2)
    return secondeEnTemps(Stemps)


print(afficheTemps(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1))))
