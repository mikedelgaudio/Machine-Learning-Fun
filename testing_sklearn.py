from sklearn import tree 

#Michael DelGaudio
#Testing out machine learning sklearn in Python

feat = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0,0,1,1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(feat, labels)

print (clf.predict([[150, 0]]))