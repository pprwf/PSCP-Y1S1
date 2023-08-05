"""EuclideanDistance2D"""
 
def euclid(valq1, valq2, valp1, valp2):
    """EuclideanDistance2D"""
    print(((valq1 - valp1) ** 2 + (valq2 - valp2) ** 2) ** 0.5)
euclid(float(input()), float(input()), float(input()), float(input()))
