import matplotlib.pyplot as plt
x = [7, 12, 3303, 3844, 11383,155462, 1078176]
y = [0.005859, 0.010010, 2.839111, 3.369141, 10.299805,	136.911865,	1083.556396 ]

plt.plot(x,y,marker = 'o')
plt.xlabel('Input Size')
plt.ylabel('Construction Time')
plt.title('Progression of Construction Time wrt Input Size')
plt.savefig("CT_CG.PNG")
plt.close()

m = ['S1', 'S2', 'Human_Opsin', 'Mouse_Opsin', 'Human_BRCA2', 'Tomato','Yeast']
n = [950, 512, 24, 24, 23, 22, 23]
plt.xticks(rotation = 45)
plt.figure(figsize=(10,7))
plt.plot(m,n,marker = 'o')
plt.xlabel('Input Size')
plt.ylabel('Implementation Constant')
plt.title('Progression of Implementation Constant wrt Input Size')

for i,txt in enumerate (n):
    plt.annotate(txt, (m[i], n[i])) 

plt.savefig("IC_CG.PNG")
plt.close()
