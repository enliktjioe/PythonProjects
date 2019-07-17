# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfMonthsLeap = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
    if year%4 != 0:
        return False
    
    elif year%100 != 0:
        return True
    
    elif year%400 != 0:
        return False

    else:
        return True

###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE

    daysInMonth = 30

    if(isLeapYear(year)):
        daysInMonth = daysOfMonthsLeap[month-1]
    else:
        daysInMonth = daysOfMonths[month-1]
    
    if day < daysInMonth:
        return year, month, day+1
    
    else:
        if month < 12:
            return year, month+1, 1
        else:
            return year+1, 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):

    if year1 < year2:
        return True
    
    if year1 == year2:
        if month1 < month2:
            return True
        else:
            if day1 < day2:
                return True
            else:
                return False
    
    return False


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    # Your code here.
    # pseudocode
    # totalDays = 0
    # while date1 is before than date2:
    #       date1 = day after date1 <- nextDay()
    #       totalDays += 1
    ##
    assert not dateIsBefore(y2,m2,d2,y1,m1,d1)

    totalDays = 0
    while(dateIsBefore(y1,m1,d1,y2,m2,d2)):
        y1, m1, d1 = nextDay(y1, m1, d1)
        totalDays +=1
    
    return totalDays

def test():
    test_cases = [((2012,9,30,2012,10,31),31), 
                  ((2012,1,1,2013,1,1),366),
                  ((2012,9,1,2012,9,4),3),
                  ((2012,2,1,2012,3,1),29)]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print("Test with data:", args, "failed")
            else:
                print("Test case passed!")
        
        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))

            else:
                print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))

test()