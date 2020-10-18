# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:21:35 2020

@author: William Ngo
"""
from sklearn.linear_model import Perceptron
from sklearn import metrics
import util

def run_perceptron():
    filepath = "./output/PER-DS1.csv"
    
    x_train, y_train = util.load_csv(util.train_1_filepath)
    x_test, y_test = util.load_csv(util.test_with_label_1_filepath)
    
    
    clf = Perceptron()
    y_pred = clf.fit(x_train,y_train).predict(x_test)
    
    train_accuracy = clf.score(x_train, y_train)
    test_accuracy = metrics.accuracy_score(y_test, y_pred)
    
    
    #confusion matrix
    cmatrix = metrics.confusion_matrix(y_test, y_pred)
    metrics.plot_confusion_matrix(clf, x_test, y_test)
    
    #evalution
    classification_report = metrics.classification_report(y_test, y_pred)
    
    #print out results
    print(f"Train Accuracy: {train_accuracy}")
    print(f"Test Accuracy: {test_accuracy}")
    
    print("")
    print("row number of the instance, index of the predicted class of that instance")
    for i in range(len(y_pred)):
        print(f"{i}, {y_pred[i]}")
        
    print("")    
    print("Confusion Matrix")
    print(cmatrix)
    
    print("")
    print("Classification report for classifier %s:\n%s\n" % (clf, classification_report))
    
    util.write_csv(filepath, y_test, y_pred, cmatrix)

run_perceptron()

