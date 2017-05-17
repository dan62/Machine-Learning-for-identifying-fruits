#I wrote this program on 13/03/2017 , this program is used to compare data 
#from features and tell the user what the fruit is based on features described 

#first we import tree from sklearn which we will use to train our classifier 
from sklearn import tree

#These are the features described the frist figure is the weight of the fruit 
#the second figure can be 1 or 2 to describe weather the fruit is bumpy or 
#smooth
features =[[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0,0,1,1]

#Here i am declaring my classifier which i will train with data from features 
#and labels inorder to deturmine an output
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

#This is a sample figure to test what the result is 
print (clf.predict([[150, 0]]))