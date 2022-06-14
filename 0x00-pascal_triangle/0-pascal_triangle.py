def pascal_triangle(n):
  triangle = []

  for i in range(n):
    if i == 0:
      triangle.append([1])
      continue
    if i == 1:
      triangle.append([1, 1])
      continue

    triangle.append([1])
    for j in range(len(triangle[i - 1]) - 1):
      triangle[-1].append(triangle[i - 1][j] + triangle[i - 1][j + 1])
    triangle[-1].append(1)
  
  return triangle
