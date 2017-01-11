# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:26:45 2016

@author: dell
"""
L = [1, 2, 3, 2, 1, 10, 100, 50, 20, 1000, 10000, 5000, 2000, 100000, 200000, 150000, 100000]

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    lastNum = 0
    total = 0
    AscendingNumList = ""
    DescendingNumList = ""
    AscendingOutput = ""
    DescendingOutput = ""
    countUp = 0
    countDown = 0
    endLocUp = 0
    endLocDown = 0
    for num in L:
        countUp += 1
        if len(AscendingNumList) == 0:
            lastNum = num
            AscendingNumList += str(num)
            AscendingNumList += ","
            
        elif num >= lastNum:
            AscendingNumList += str(num)
            AscendingNumList += ","
            lastNum = num
            
            if len(AscendingNumList.split(",")) > len(AscendingOutput.split(",")):
                AscendingOutput = AscendingNumList
                endLocUp = countUp
        else:
            AscendingNumList = ""
            AscendingNumList += str(num)
            AscendingNumList += ","
            lastNum = num
            
            
    
    for num in L:
        countDown += 1
        if len(DescendingNumList) == 0:
            lastNum = num
            DescendingNumList += str(num)
            DescendingNumList += ","

            
        elif num <= lastNum:
            DescendingNumList += str(num)
            DescendingNumList += ","
            lastNum = num
            
            if len(DescendingNumList.split(",")) > len(DescendingOutput.split(",")):
                DescendingOutput = DescendingNumList
                endLocDown = countDown
        else:
            DescendingNumList = ""
            DescendingNumList += str(num)
            DescendingNumList += ","
            lastNum = num
            
    if len(AscendingOutput) > len(DescendingOutput):
        Nums = AscendingOutput.split(",")
        upNums = Nums[:-1]
        for i in upNums:
            total += int(i)        
        print(total)
            
    elif len(DescendingOutput) > len(AscendingOutput):
        Nums = DescendingOutput.split(",")
        downNums = Nums[:-1]
        for i in downNums:
            total += int(i)
        print(total)
        
    else:
        if endLocDown > endLocUp:
            Nums = AscendingOutput.split(",")
            upNums = Nums[:-1]
            for i in upNums:
                total += int(i)        
            print(total)
        else:
            Nums = DescendingOutput.split(",")
            downNums = Nums[:-1]
            for i in downNums:
                total += int(i)
            print(total)
            
        
longest_run(L)      