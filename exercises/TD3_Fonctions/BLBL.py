def tempsEnSeconde(temps):
    jts = temps[0]*86400
    hts = temps[1]*3600
    mts = temps[2]*60
    return jts + hts + mts + temps[3]


def secondeEnTemps(seconde):
    sej = seconde // 86400
    seh = seconde // 3600 % 24
    sem = seconde // 60 % 60
    ses = seconde % 60
    return sej, seh, sem, ses


def sommeTemps(temps1, temps2):
    Stemps = tempsEnSeconde(temps1) + tempsEnSeconde(temps2)
    return secondeEnTemps(Stemps)


print(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))
