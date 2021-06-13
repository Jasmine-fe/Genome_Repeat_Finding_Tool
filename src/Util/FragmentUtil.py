# In[ ]:
import matplotlib.pyplot as plt
from collections import Counter

# In[ ]:
# sortedLenList = [(lengthValue: count), ... ]
def fragmentLenPlot(sortedLenList):
    x, y = [], []
    for len, count in sortedLenList:
        x.append(len)
        y.append(count)
    plt.figure(figsize=(20, 12))
    plt.title("Distribution - fragment Length", fontsize=30)
    plt.xlabel("length", fontsize=15)
    plt.ylabel("count", fontsize=15)
    plt.plot(x, y)
    return 0


# In[1]:
def fragmentLengthDistribution(rfLenList):
    rfCounter = Counter(rfLenList)
    rfCommonLenList = rfCounter.most_common(
        len(rfCounter)
    )  # [(length, count)...], ordered by count
    sortedirList = sorted(
        rfCommonLenList, key=lambda x: x[0]
    )  # [(length, count)...], ordered by length
    fragmentLenPlot(sortedirList)