def Mean(X, Y):
    AMean = (X + Y) / 2
    GMean = (X * Y) ** 0.5
    return AMean, GMean

print(Mean(4, 8))
print(Mean(4, 10))
print(Mean(6, 6))