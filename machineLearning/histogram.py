import numpy as np
from matplotlib import pyplot as plt

#generate two lists (size 5 and 20) of random numbers between 1 and 6
few_rolls = np.random.randint(1, 7, size = 5)
mid_rolls = np.random.randint(1, 7, size = 20)
much_rolls = np.random.randint(1, 7, size = 80)
print("first dataset:", few_rolls)
print("second dataset:", mid_rolls)
print("third dataset:", much_rolls)
print()

#numpy's arrange function returns an array with evenly spaced intergals
bins = np.arange(.5,7.5) #arguments are start and stop point, default counter is 1
print("bins are:", bins)
print()

#unlike pyplot's hist() function, numpy's histogram function isn't graphical.
#It does the same thing with text though: it shows the frequency of the dataset
#by splitting it into equal sized bins
firstDataset = np.histogram(few_rolls, bins)
secondDataset = np.histogram(mid_rolls, bins)
thirdDataset = np.histogram(much_rolls, bins)
print("first histogram:", firstDataset)
print("second histogram:", secondDataset)
print("third histogram:", thirdDataset)
print()

#do the same thing, but only grab the first element of the returned list
#(that's what the [0] does at  the end)
few_counts = np.histogram(few_rolls, bins = np.arange(.5,7.5))[0]
mid_counts = np.histogram(mid_rolls, bins = np.arange(.5,7.5))[0]
much_counts = np.histogram(much_rolls, bins = np.arange(.5,7.5))[0]
print("few_counts:", few_counts)
print("mid_counts:", mid_counts)
print("much_counts:", much_counts)

#the subplot function lets you draw multiple plots in one figure(like the game window)
#the subplot returns returns a TUPLE containing a figure and axes objects
figure, ((ax1, ax2, ax3)) = plt.subplots(1, 3, figsize = (10, 3))

#These are axes objects. Each figure can contain multiple axes objects. 
ax1.bar(np.arange(1, 7), few_counts)
ax2.bar(np.arange(1, 7), mid_counts)
ax3.bar(np.arange(1, 7), much_counts)

plt.show() #put 'em on the screen!