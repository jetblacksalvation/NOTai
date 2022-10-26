import numpy as np
from matplotlib import pyplot as plt

#generate two lists (size 5 and 20) of random numbers between 1 and 6
few_rolls = np.random.randint(1, 7, size = 5)
many_rolls = np.random.randint(1, 7, size = 20)
superrols = np.random.randint(1,7,size = 80)
print("first dataset:", few_rolls)
print("second dataset:", many_rolls)
print()

#numpy's arrange function returns an array with evenly spaced intergals
bins = np.arange(.5,7.5) #arguments are start and stop point, default counter is 1
print("bins are:", bins)
print()

#unlike pyplot's hist() function, numpy's histogram function isn't graphical.
#It does the same thing with text though: it shows the frequency of the dataset
#by splitting it into equal sized bins
firstDataset = np.histogram(few_rolls, bins)
secondDataset = np.histogram(many_rolls, bins)
thirddata = np.histogram(superrols, bins)

print("first histogram:", firstDataset)
print("second histogram:", secondDataset)
print("thrid histogram", thirddata)

#do the same thing, but only grab the first element of the returned list
#(that's what the [0] does at  the end)
few_counts = np.histogram(few_rolls, bins = np.arange(.5,7.5))[0]
many_counts = np.histogram(many_rolls, bins = np.arange(.5,7.5))[0]
supercounts = np.histogram(superrols, bins = np.arange(.5,7.5))[0]

print("few_counts:", few_counts)
print("many_counts:", many_counts)

#the subplot function lets you draw multiple plots in one figure(like the game window)
#the subplot returns returns a TUPLE containing a figure and axes objects
figure, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (8, 3))

#These are axes objects. Each figure can contain multiple axes objects. 
ax1.bar(np.arange(1, 7), few_counts)
ax2.bar(np.arange(1, 7), many_counts)
ax3.bar(np.array(1, 7),supercounts)
plt.show() #put 'em on the screen!


# from matplotlib import pyplot
# import numpy

# numList = numpy.random.randint(200,size =50)

# print("the list of numbers we have is", *numList)

# screen = pyplot.figure(figsize = (12,8))
# #pyplot.hist(numList)#changes color for some reason 


# pyplot.hist(numList, bins = [x*20 for x in range(10)])

# pyplot.title("histogram")
# pyplot.show()
