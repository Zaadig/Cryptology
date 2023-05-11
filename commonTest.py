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
    assert common.expo_modulaire(5, 3, 7) == 5
    assert common.expo_modulaire(3, 5, 7) == common.expo_modulaire_fast(3, 5, 7)
    assert common.expo_modulaire(3, 4, 7) == common.expo_modulaire_fast(3, 4, 7)
    assert common.expo_modulaire(3, 3, 7) == common.expo_modulaire_fast(3, 3, 7)
    assert common.expo_modulaire(3, 2, 7) == common.expo_modulaire_fast(3, 2, 7)
    assert common.expo_modulaire(3, 1, 7) == common.expo_modulaire_fast(3, 1, 7)


def crible_erasTest():

    primes = common.crible_eras(30)
    for p in primes:
        assert all(p % i != 0 for i in range(2, p))

    assert len(common.crible_eras(10)) == 4
    assert len(common.crible_eras(20)) == 8
    assert len(common.crible_eras(50)) == 15


    assert common.crible_eras(1) == []
    assert common.crible_eras(0) == []
    assert common.crible_eras(-10) == []


def fermatTest():

    assert common.test_fermat(15, 3) == False
    assert common.test_fermat(17, 3) == True
    assert common.test_fermat(18, 3) == False
    assert common.test_fermat(19, 3) == True
    assert common.test_fermat(20, 3) == False
    assert common.test_fermat(21, 3) == False


def find_ruTest():

    assert common.find_ru(15) == (0, 15)
    assert common.find_ru(16) == (4, 1)
    assert common.find_ru(17) == (0, 17)
    assert common.find_ru(18) == (1, 9)
    assert common.find_ru(19) == (0, 19)


def temoin_rabinTest():

    assert common.temoin_rabin(2, 15) == True
    assert common.temoin_rabin(3, 15) == True
    assert common.temoin_rabin(5, 15) == True
    assert common.temoin_rabin(7, 15) == True

def gen_primeTest():

    assert common.test_rabin(common.gen_prime(10), 5) == True
    assert common.test_rabin(common.gen_prime(100), 5) == True
    assert common.test_rabin(common.gen_prime(2), 5) == True
    assert common.test_rabin(common.gen_prime(1000), 5) == True

    

if __name__ == "__main__":
    print("Start Tests \n")
    pgcdTest()
    euclide_extTest()
    inverse_modulaireTest()
    expo_modulaireTest()
    crible_erasTest()
    fermatTest()
    find_ruTest()
    temoin_rabinTest()
    gen_primeTest()
    print("Ends Tests \n")

