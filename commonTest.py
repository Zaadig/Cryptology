import common


def pgcdTest():
    assert common.pgcd(12, 18) == 6
    assert common.pgcd(18, 12) == 6
    assert common.pgcd(12, 0) == 12
    assert common.pgcd(0, 12) == 12
    assert common.pgcd(0, 0) == 0
    assert common.pgcd(1, 12) == 1
    
def euclide_extTest():
    assert common.euclide_ext(35, 12) == (1, -1, 3)
    assert common.euclide_ext(12, 35) == (1, 3, -1)
    assert common.euclide_ext(12, 0) == (12, 1, 0)
    assert common.euclide_ext(0, 12) == (12, 0, 1)
    assert common.euclide_ext(0, 0) == (0, 1, 0)


def inverse_modulaireTest():

    assert common.inverse_modulaire(12, 35) == 3
    assert common.inverse_modulaire(12, 0) == None
    assert common.inverse_modulaire(0, 12) == None
    assert common.inverse_modulaire(0, 0) == None



def expo_modulaireTest():
    assert common.expo_modulaire(3, 5, 7) == 3**5%7
    assert common.expo_modulaire(7, 2, 11) == 7**2%11
    assert common.expo_modulaire(13, 17, 23) == 13**17%23
    assert common.expo_modulaire(1, 1, 1) == 1
    assert common.expo_modulaire(1, 1, 2) == 1



def expo_modulaire_fastTest():

    assert common.expo_modulaire_fast(3, 5, 7) == 3**5%7
    assert common.expo_modulaire_fast(7, 2, 11) == 7**2%11
    assert common.expo_modulaire_fast(13, 17, 23) == 13**17%23
    assert common.expo_modulaire_fast(1, 1, 1) == 1
    assert common.expo_modulaire_fast(1, 1, 2) == 1
    assert common.expo_modulaire_fast(1, 1, 3) == 1
    assert common.expo_modulaire_fast(7, 1, 7) == 0





pgcdTest()
euclide_extTest()
inverse_modulaireTest()
expo_modulaireTest()
# expo_modulaire_fastTest()