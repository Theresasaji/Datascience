import matplotlib.pyplot as  plt
import numpy as np
x  =np.array(['anu','binu','cinu','denu','ernu','feba','ginu','henu','illy','jenu','kaira'])
y1 = np.array([38,62,18,75,38,59,66,92,52,75,48])
y2 = np.array([74,44,85,19,88,69,50,33,29,32,56])

plt.title("STUDENT'S SCORE")
plt.xlabel("names of student")
plt.ylabel("marks")
plt.scatter(x,y1,marker='^' , color='hotpink')
plt.scatter(x,y2,marker='*' , color='blue')


