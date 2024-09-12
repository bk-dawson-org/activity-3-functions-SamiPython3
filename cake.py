import math

radius = float(input("Enter a value for the radius"))
height = float(input("Enter a value for the height"))

def getCylinderVolume(radius, height) :
    '''
        This function calculates the volume of a cylinder
        param radius: This is the radius of the cylinder
        param height: This is the height of the cylinder
        return : The function returns the volume of a cylinder
    '''
    volume = (radius ** 2) * math.pi * height
    return volume

# Calculates the volume of a cylinder with values (1, 1) and (2, 6)
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

# Calculating the number of slices
numberOfSlices1 = getNumberOfSlices(2, 4, 5)
#print("Number of slices for the given volume =", int(numberOfSlices1))



