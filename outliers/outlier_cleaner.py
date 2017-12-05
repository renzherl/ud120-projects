#!/usr/bin/python
import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    
    i=0
    size = len(ages)
    array = [None] * size
    end = int(round(size * 0.9))
    print('Total Size: \n', size)
    print('End Index: \n', end)
    while (i < size) :
        array[i]= getError(predictions[i], net_worths[i])
        print('Array: {}\n', array[i])
        i += 1
        print('i: \n', i)
    
    result = zip(ages,net_worths,array)
    result.sort(key=lambda x: x[2])

    cleaned_data = result[0:end]
    return cleaned_data

def getError(prediction,net_worth):
    y = math.fabs(prediction - net_worth)
    return  y*y

