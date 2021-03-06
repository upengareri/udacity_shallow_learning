#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    predictions = predictions.flatten()
    ages = ages.flatten()
    net_worths = net_worths.flatten()
    ### your code goes here
    ### identify and remove the most outlier 9 points
    residual_errors = []
    for i in range(0, len(predictions)):
        res_error = predictions[i] - net_worths[i]
        residual_errors.append(res_error)
        

    tuples = zip(ages,net_worths,residual_errors)
    cleaned_data = sorted(tuples, key=lambda tup: tup[2], reverse=True)
    cleaned_data = cleaned_data[9:len(cleaned_data)]
    return cleaned_data
