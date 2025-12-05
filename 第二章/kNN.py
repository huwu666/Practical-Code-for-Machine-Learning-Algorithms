from __future__ import print_function
from numpy import *

import operator
from os import listdir
from collections import Counter

def createDataSet():
    group = array([1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):

    dataSetSize = dataSet.shape[0]

    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()

    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
       
    maxClassCount = max(classCount, key = classCount.get)
    return maxClassCount


def test1():
    
    group, labels = createDataSet()
    print(str(group))
    print(str(labels))
    print(classify0([0.1, 0.1], group, labels, 3))

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    fr = open(filename)
    
    index = 0

    for line in fr.readlines:
        line = line.strip()
        listFromLine = line.split('\t')

        returnMat[index, :] = listFromLine[0:3]

        classLabelVector.append(int(listFromLine[-1]))
        index += 1

    return returnMat, classLabelVector

def autoNorm(dataSet):

    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)

    ranges = maxVals - minVals
    