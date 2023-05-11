import common


def main():
    assert common.pgcd(12, 18) == 6
    assert common.pgcd(18, 12) == 6
    assert common.pgcd(12, 0) == 12
    assert common.pgcd(0, 12) == 12
    assert common.pgcd(0, 0) == 0
    assert common.pgcd(1, 12) == 1
    
