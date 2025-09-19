import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans' 

labels = ["A社", "B社", "C社", "D社"]
sizes = [15, 30, 45, 10]

plt.figure(figsize=(6, 6))
plt.pie(sizes,labels=labels,autopct="%1.1f%%",startangle=90)
plt.title("市場シェア")
plt.show()