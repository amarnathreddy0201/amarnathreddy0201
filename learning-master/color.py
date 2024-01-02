for i in range(len(image)):
  da = []
  for j in range(len(image[i])):
      da1 = []

      image[i][j][0] = 180 + image[i][j][0]
      image[i][j][1] = 250 + image[i][j][1]
      image[i][j][2] = 250 + image[i][j][2]
