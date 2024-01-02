
from scipy.interpolate import barycentric_interpolate
from numpy import polyfit


#steps = [104705, 197712, 321009, 472744, 655252, 865795, 1107573, 1377002, 1677916, 2006098, 2366229, 2753224, 3172523, 3618581, 4097188]
#N =     [5,       7,       9,    11,      13,      15,      17,    19,     21,       23,       25,       27,       29, 31, 33]
#spots = [345,     475,    605,     735,   865,    995,     1125,    1255,   1385,   1515,    1645,     1775,     1905, 2035, 2165]

# steps 327 2 5 94056
# steps 458 3 7 184099
# steps 589 4 9 304096
# steps 720 5 11 454047

#steps 720 5 11 454047
#steps 851 6 13 633952

steps = [65, 196, 327, 458, 589, 720]
spots = [3832, 33967, 94056, 184099, 304096, 454047]

# steps 65 0 1 3832
# steps 196 1 3 33967
# steps 327 2 5 94056
# steps 458 3 7 184099
# steps 589 4 9 304096
# steps 720 5 11 454047
# steps 851 6 13 633952

i = 0
x = [steps[i+j] for j in range(3)]
y = [spots[i+j] for j in range(3)]
print(x, y)
a,b,c = polyfit(x, y, deg=2)
n = steps[i+3]
print(int(round(a*n*n + b*n + c)), spots[i+3], a, b , c)

for i in range(1, len(steps)-3):
    x = [steps[i+j] for j in range(3)]
    y = [spots[i+j] for j in range(3)]
    n = steps[i+3]
    print(int(round(a*n*n + b*n + c)), spots[i+3], a, b , c)

n = 26501365
print(int(round(a*n*n + b*n + c)), a, b, c)
