import math

radius = float(input("Enter a value for the radius"))
height = float(input("Enter a value for the height"))

def getCylinderVolume(radius, height) :
    volume = (radius ** 2) * math.pi * height
    return volume

volume1 = getCylinderVolume(1, 1)
volume2 = getCylinderVolume(2, 6)
print("Volume 1 =", round(volume1, 3))
print("Volume 2 =", int(volume2))

volume3 = getCylinderVolume(radius, height)
print("Volume 3 =", round(volume3, 2))

def getNumberOfSlices(radius, height, volumeOfSlice) : 
    volume = getCylinderVolume(radius, height)
    numberOfSlices = volume / volumeOfSlice
    return numberOfSlices

numberOfSlices1 = getNumberOfSlices(10, 10, 100)
print("Number of slices for the given volume =", int(numberOfSlices1))



