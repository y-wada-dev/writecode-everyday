import random
import matplotlib.pyplot as plt

in_pi = 0

n = 1000000  # `試行回数

X_inside = []
Y_inside = []
X_outside = []
Y_outside = []

for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    z = x**2 + y**2
    
    if z <= 1:
        in_pi += 1
        X_inside.append(x)
        Y_inside.append(y)
    else:
        X_outside.append(x)
        Y_outside.append(y)

pi = 4 * in_pi / n

print(f"推定されたπの値: {pi}")

plt.figure(figsize=(6, 6))
plt.scatter(X_inside, Y_inside, color='blue', s=1, label='Inside Circle')
plt.scatter(X_outside, Y_outside, color='red', s=1, label='Outside Circle')
plt.gca().set_aspect('equal', adjustable='box')
plt.title('monte Carlo Simulation for π')
plt.legend()
plt.show()

print("円の内側の点の数:", in_pi)
print("試行回数:", n)
print("円の外側の点の数:", n - in_pi)
print("πの推定値:", pi)