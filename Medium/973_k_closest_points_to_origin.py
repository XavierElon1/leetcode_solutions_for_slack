import math
points = [[3,3],[5,-1],[-2,4]]
K = 2
lst = []
for point in points:
   z = math.sqrt((point[0] ** 2) + (point[1] ** 2))
   lst.append((point, z))
z = sorted(lst, key= lambda t:t[0])
print("The closest set of points are: ", [z[i][0] for i in range(0,K)])
