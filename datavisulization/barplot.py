import numpy as np
import matplotlib.pyplot as plt

candidates = ["java", "c++","c#", "python", "go"]
votes = [1040,133,150,123,155]
plt.bar(candidates,votes, color ="red", align = "edge", width = 0.5, edgecolor ="green", lw = 6)
plt.show()
