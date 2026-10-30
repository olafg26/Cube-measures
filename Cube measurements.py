#IMPORT
import time

#VARIABLES AND PROCESSES
sideLength = float(input("Enter your cube's side length in centimetres: "))
time.sleep(1)
area = sideLength ** 2
surfaceArea = area * 6
volume = sideLength ** 3
SA_V = round((surfaceArea / volume), 2)

#OUTPUTS
print(f"The area for a surface of your cube is {area:.2f}cm².")
time.sleep(1)
print(f"The surface area for your cube is {surfaceArea:.2f}cm².")
time.sleep(1)
print(f"The volume for your cube is {volume:.2f}cm³.")
time.sleep(1)
print(f"The surface area to volume ratio for your cube is {SA_V:.2f}:1.")
time.sleep
