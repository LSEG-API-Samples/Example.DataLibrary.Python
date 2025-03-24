#peers universe
def PEERS(instrument):
    '''
    Is used to define the peer organisations for the indicated company.
    Instrument should be either a PermID or RIC.
    '''
    if (instrument is not None) and (len(instrument)>0):
        value_ = 'PEERS({})'.format(instrument)
    else:
        value_=''    
    return value_

def FORMULA(*args):
    '''
    Combines the given arguments into a single string.
    Example: FORMULA('TR.PriceClose', '*2+100') will create a string value 'TR.PriceClose*2+100'.
    '''
    if (args is not None) and (len(args)>0):
        value_ = []
        if type(args) == list:
            value_ = ''.join(args)
        else:
            for l in args:
                value_.append(''.join(l))
            value_ = ''.join(value_)
    else:
        value_=''
    return value_

#equity universe
def Equity(primary = False, public = False, active = False, private = False, inactive = False, countryprimaryquote=False):
    '''
    Is used to enable search for public or private companies for the indicated company, when defining the universe.
    To search for dual listings, countryprimaryquote must be True.
    '''
    value_ = []
    org_ = []
    status_ = []
    if primary: value_.append('primary')

    if private: org_.append('private')   
    if public: org_.append('public')
    if len(org_)>0: value_.append(' or '.join(org_))
    
    if active: status_.append('active')
    if inactive: status_.append('inactive')
    if len(status_) > 0: value_.append(' or '.join(status_)) 
    
    if countryprimaryquote: value_.append('countryprimaryquote')
        
    value_ = 'Equity({})'.format(','.join(value_))

    return value_

#deals universe
DEALS = 'DEALS'

#private equity universe
PRIVATEEQUITY = 'PRIVATEEQUITY'


#median
def GMEDIAN(groupby_field, value_field):
    '''
    Calculates the median value of a specific data item (value_field) on a per group basis that has been specified across a set of instruments.
    '''
    if (groupby_field is not None) and (len(groupby_field)>0) and (value_field is not None) and (len(value_field)>0):
        values_ = 'GMEDIAN({}{})'.format(','.join([groupby_field,value_field]))
    else:
        values_=''    
    return values_

def MEDIAN(field):
    '''
    Returns the value in the middle of a set of values.
    '''
    if (field is not None) and (len(field)>0):
        value_ = 'MEDIAN({})'.format(field)
    else:
        value_=''    
    return value_

#average
def GAVG(groupby_field, value_field):
    '''
    Calculates the average value of a specific data item (value_field) on a per group basis that has been specified across a set of instruments.
    '''
    if (groupby_field is not None) and (len(groupby_field)>0) and (value_field is not None) and (len(value_field)>0):
        values_ = 'GAVG({})'.format(','.join([groupby_field,value_field]))
    else:
        values_=''    
    return values_

def AVG(field):
    '''
    Returns the arithmetic mean or the middle (expected value of a data set). 
    The function should support any numerical/money data items. No Parameters other than a time series data item should be required when passing the syntax.
    '''
    if (field is not None) and (len(field)>0):
        value_ = 'AVG({})'.format(field)
    else:
        value_=''    
    return value_

#standard deviation
def GSTD(groupby_field, value_field):
    '''
    Calculates the standard deviation of a specific data item (value_field) on a per-group basis that has been specified across a set of instruments.
    '''
    if (groupby_field is not None) and (len(groupby_field)>0) and (value_field is not None) and (len(value_field)>0):
        values_ = 'GSTD({})'.format(','.join([groupby_field,value_field]))
    else:
        values_=''    
    return values_    

#standard dev
def STD(field):
    '''
    Calculates the standard deviation of a specific data item.
    '''
    if (field is not None) and (len(field)>0):
        value_ = 'STD({})'.format(field)
    else:
        value_=''    
    return value_ 

#maximum
def GMAX(groupby_field, value_field):
    '''
    Finds the Maximum (Largest) value of a data item (value_field) on a per-group basis across a set of instruments.
    '''
    if (groupby_field is not None) and (len(groupby_field)>0) and (value_field is not None) and (len(value_field)>0):
        values_ = 'GMAX({})'.format(','.join([groupby_field,value_field]))
    else:
        values_=''    
    return values_ 

def MAX(series):
    '''
    Finds the maximum (largest) Value of a data item array.
    '''
    if (series is not None) and (len(series)>0):
        values_ = 'MAX({})'.format(','.join(series))
    else:
        values_=''    
    return values_ 


#minimum
def GMIN(groupby_field, value_field):
    '''
    Finds the Minimum (Smallest) value of a data item (value_field) on a per-group basis across a set of instruments.
    '''
    if (groupby_field is not None) and (len(groupby_field)>0) and (value_field is not None) and (len(value_field)>0):
        values_ = 'GMIN({})'.format(','.join([groupby_field,value_field]))
    else:
        values_=''    
    return values_ 

def MIN(series):
    '''
    Finds the minimum (smallest) value of a data item array.
    '''
    if (series is not None) and (len(series)>0):
        values_ = 'MIN({})'.format(','.join(series))
    else:
        values_=''    
    return values_  

#sum
def GSUM(groupby_field, value_field):
    '''
    Calculates the Sum of a specific data item (value_field) on a per-group basis that has been specified across a set of instruments.
    '''
    if (groupby_field is not None) and (len(groupby_field)>0) and (value_field is not None) and (len(value_field)>0):
        values_ = 'GSUM({})'.format(','.join([groupby_field,value_field]))
    else:
        values_=''    
    return values_    

#count
def GCOUNT(groupby_field, value_field):
    '''
    Calculates the Count (number of non null values) of a specific data item (value_field) on a per-group basis that has been specified across a set of instruments.
    '''
    if (groupby_field is not None) and (len(groupby_field)>0) and (value_field is not None) and (len(value_field)>0):
        values_ = 'GCOUNT({})'.format(','.join([groupby_field,value_field]))
    else:
        values_=''    
    return values_ 

def COUNT(field):
    '''
    Calculates the number of non null values within an array of data.
    '''
    if (field is not None) and (len(field)>0):
        value_ = 'COUNT({})'.format(field)
    else:
        value_=''    
    return value_    

#geometric mean
def GMEAN(field):
    '''
    Returns the geometric mean of an array or range of positive numeric data. The numbers are multiplied and then the nth root is taken.
    '''
    if (field is not None) and (len(field)>0):
        value_ = 'GMEAN({})'.format(field)
    else:
        value_=''    
    return value_    

#RSI
def RSI(field):
    '''
    Returns a value comparing upward movements of a variable to downward movements over a selected period.
    Example: rsi('TR.Close(sdate=0d,edate=-9d,frq=d)') - calculates the RSI of the instrument(s) closing price for the past ten days.
    '''
    if (field is not None) and (len(field)>0):
        value_ = 'RSI({})'.format(field)
    else:
        value_=''    
    return value_    

#moving average
def MAVG(series_field, period=2):
    '''
    Calculates the arithmetic mean or the middle (expected value of a data set) of an array of data points by specifying a period to calculate the average on over a range of values. The function should support any numerical/money data items.
    '''
    if (series_field is not None) and (len(series_field)>0):
        value_ = 'MAVG({},{})'.format(series_field, period)
    else:
        value_=''    
    return value_  

#cumulative sum
def CSUM(field):
    '''
    Will add up cumulatively any array of data. The output that gets returned will be an array of values.
    '''
    if (field is not None) and (len(field)>0):
        value_ = 'CSUM({})'.format(field)
    else:
        value_=''    
    return value_  

#variance
def VAR(field):
    '''
    Calculates the sample variance for a sample of data using a data item or expression.
    '''
    if (field is not None) and (len(field)>0):
        value_ = 'VAR({})'.format(field)
    else:
        value_=''    
    return value_  

#sum
def SUM(field):
    '''
    Adds the values from the range of numbers provided from the function and returns the total.
    '''
    if (field is not None) and (len(field)>0):
        value_ = 'SUM({})'.format(field)
    else:
        value_=''    
    return value_         

#weighted average
def WAVG(weight_field, field):
    '''
    Applies user defined weights to user specified values. The weights and values are specified as Data Items into the function. 
    NOTE: It is NOT possible for the users to enter weights as inputs (i.e., as an array of numbers for e.g.).
    '''
    if (weight_fields is not None) and len(weight_fields)>0 and (field is not None) and (len(field)>0):
        value_ = 'WAVG({},{})'.format(weight_field, field)
    else:
        value_=''    
    return value_ 

#available
def AVAIL(fields):
    '''
    Finds the first data item in your request that is a valid value. The system will run the first data item and if its null it will move on to the next data item until a value is returned or it reaches the last item and a null or value is returned. 
    This is done per data point if running a time series request.
    '''
    if (fields is not None) and (len(fields)>0):
        values_ = []
        for v in fields:
            values_.append(''.join(v))
        values_ = 'AVAIL({})'.format(','.join(values_))
    else:
        values_=''    
    return values_     

#zero available
def ZAV(field):
    '''
    Replaces a "NULL" value with a "0", otherwise if there is a value the function returns the value.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'ZAV({})'.format(field)
    else:
        values_=''    
    return values_  

#text available
def TEXTAV(field, custom_string):
    '''
    Checks if text is available for a given data item and replace null strings with a user defined value. This function will work for all string, numeric and date items for single point in time and time series data.
    '''
    if (field is not None) and (len(field)>0) and (custom_string is not None) and (len(custom_string)>0):
        condition = []
        value_ = 'TEXTAV({},{})'.format(field, custom_string)
    else:
        value_=''    
    return value_   

#if statement
def IF(condition, true_field, false_field):
    '''
    Checks whether an IF condition is "True;" if so, returns a THEN value. If the IF condition is "False," it returns an ELSE value.
    '''
    if (condition is not None) and (len(condition)>0) and (true_field is not None) and (len(true_field)>0) and (false_field is not None) and (len(false_field)>0):
        condition.append(''.join(condition))
        if type(true_field)==list:
            true_field.append(''.join(true_field)) 
        if type(false_field)==list:
            false_field.append(''.join(false_field))

        value_ = 'IF({},{},{})'.format(condition, true_field, false_field)
    else:
        value_=''          
    return value_

#any statement
def ANY(condition):
    '''
    Uses an array of a data item set to some condition. If any of the values in the Array are true then a 1 is returned. 
    If they all do not meet the condition then a false (0) will be returned. This function can be used in conjunction with any other analytic but will primarily be seen in the IF function.
    '''
    if (condition is not None) and (len(condition)>0) and (type(condition)==list):
        values_ = 'ANY({})'.format(''.join(condition))
    else:
        values_=''    
    return values_    

#percent change
def PERCENT_CHG(field1, field2):
    '''
    Returns how large a new value is relative to its initial value, as a percentage.
    '''
    if (field1 is not None) and (len(field1)>0) and (field2 is not None) and (len(field2)>0):
        value_ = 'PERCENT_CHG({},{})'.format(field1, field2)
    else:
        value_=''    
    return value_ 

#compound growth rate
def CGR(series):
    '''
    Calculates the Compound Growth Rate and returns the constant growth rate per period that causes the initial value to grow to the final value per company. 
    The function can only return a single value per time series input, and cannot support a moving time series output.
    '''
    if (series is not None) and (len(series)>0):
        value_ = 'CGR({})'.format(series)
    else:
        value_=''    
    return value_ 

#in function
def IN(field, *values):
    '''
    Returns true (1) if the specified value (first parameter) is within the specified list of values (second parameter). 
    This analytic can be useful primarily when using screens that require you to look for instruments that may fall in a specific industry or sector.
    '''
    if (field is not None) and (len(field)>0) and (values is not None) and (len(values)>0):
        value_ = 'IN({},{})'.format(field, ','.join(values))
    else:
        value_=''    
    return value_ 

#all statement
def ALL(condition):
    '''
    Uses an array of a data item set to some condition. If all of the values in the Array are true then a 1 is returned. 
    If any values do not meet the condition then a false (0) will be returned. This function can be used in conjunction with any other analytics but will primarily be seen in the IF function
    '''
    if (condition is not None) and (len(condition)>0) and (type(condition)==list):
        values_ = 'ALL({})'.format(''.join(condition))
    else:
        values_=''    
    return values_  

#abs function
def ABS(statement):
    '''
    This function returns the absolute value of a single point or time series array.
    '''
    if (statement is not None) and (len(statement)>0):
        if (type(statement)==list):
            values_ = 'ABS({})'.format(''.join(statement))
        else:
            values_ = 'ABS({})'.format(statement)
    else:
        values_=''    
    return values_   

#ceiling function
def CEILING(field):
    '''
    Returns the next integer value that is greater than or equal to a specified number. CEILING should work on all numeric, string, and date data items.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'CEILING({})'.format(field)
    else:
        values_=''    
    return values_           

#floor function
def FLOOR(field):
    '''
    Returns the next integer value that is less than or equal to a specified number. FLOOR should work on all numeric, string, and date data items.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'FLOOR({})'.format(field)
    else:
        values_=''    
    return values_    

#sin function
def SIN(field):
    '''
    Calculates the rise of an angle. Numeric items and expressions can only be applied to this function. This function is Time Series Capable.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'SIN({})'.format(field)
    else:
        values_=''    
    return values_   

#cos function
def COS(field):
    '''
    Calculates the run of an angle. Numeric items and expressions can only be applied to this function. This function is Time Series Capable.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'COS({})'.format(field)
    else:
        values_=''    
    return values_

#tan function
def TAN(field):
    '''
    Calculates the slope of an angle. Numeric items and expressions can only be applied to this function. This function is Time Series Capable.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'TAN({})'.format(field)
    else:
        values_=''    
    return values_         

#asin function
def ASIN(field):
    '''
    Returns the Inverse of the Sin (rise of an angle). Numeric items and expressions can only be applied to this function. This function is Time Series Capable.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'ASIN({})'.format(field)
    else:
        values_=''    
    return values_          

#acos function
def ACOS(field):
    '''
    Returns the Inverse of the Cosine (run of an angle). Numeric items and expressions can only be applied to this function. This function is Time Series Capable.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'ACOS({})'.format(field)
    else:
        values_=''    
    return values_      

#atan function
def ATAN(field):
    '''
    Returns the Inverse of the Tangent (slope of an angle). Numeric items and expressions can only be applied to this function. This function is Time Series Capable.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'ATAN({})'.format(field)
    else:
        values_=''    
    return values_   

#log function
def LOG(field):
    '''
    This calculates the logarithm, base 10, of each value in a series. Plotting logarithmic data can be useful for showing data of very different magnitudes on the same chart.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'LOG({})'.format(field)
    else:
        values_=''    
    return values_        

#ln function
def LN(field):
    '''            
    This calculates the natural logarithm, base e, of each value in a series. Plotting logarithmic data can be useful for showing data of very different magnitudes on the same chart.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'LN({})'.format(field)
    else:
        values_=''    
    return values_ 


#sqrt function
def SQRT(field):
    '''            
    This calculates the square root of each numeric data item value within a series.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'SQRT({})'.format(field)
    else:
        values_=''    
    return values_

#round function
def ROUND(field, decimals=0):
    '''            
    Returns the value of a number rounded to a specified number of decimal places.
    ''' 
    if (field is not None) and (len(field)>0):
        values_ = 'ROUND({},{})'.format(field, decimals)
    else:
        values_=''    
    return values_  

#frac function
def FRAC(field):
    '''            
    Returns the value of the fractional part of any numeric data item value or expression.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'FRAC({})'.format(field)
    else:
        values_=''    
    return values_        

#pow function
def POW(field, power=1):
    '''            
    This applies a specified power to each value in a series. For example, you can calculate the square for each value in a series by applying a power of 2.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'POW({},{})'.format(field, decimals)
    else:
        values_=''    
    return values_

#rel function
def REL(instrument, field):
    '''            
    Returns the value of a data item of an identifier relative to the symbol selected. This function allows you to compare your security (for example, IBM) to another security (for example, GOOG).
    '''
    if (instrument is not None) and (len(instrument)>0) and (field is not None) and (len(field)>0):
        values_ = 'REL({},{})'.format(instrument, field)
    else:
        values_=''    
    return values_

#exp function
def EXP(field):
    '''            
    Returns Euler's number (e) raised to the number power. Accepts only numeric data as input.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'EXP({})'.format(field)
    else:
        values_=''    
    return values_

#int function
def INT(field):
    '''            
    Returns the integer portion of a number.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'INT({})'.format(field)
    else:
        values_=''    
    return values_  

#days_between function
def DAYS_BETWEEN(field1, field2):
    '''            
    Days Between will return the number of days between two dates that are entered in the analytic. Both parameters of the function must be in a date format.
    '''
    if (field1 is not None) and (len(field1)>0) and (field2 is not None) and (len(field2)>0):
        values_ = 'DAYS_BETWEEN({},{})'.format(field1, field2)
    else:
        values_=''    
    return values_

#not_in function
def NOT_IN(field, *values):
    '''
    Returns true (1) if the specified value (first parameter) is not within the specified list of values (second parameter). 
    This analytic can be useful primarily when using screens that require you to look for instruments that do not fall in a specific industry or sector.
    '''
    if (field is not None) and (len(field)>0) and (values is not None) and (len(values)>0):
        if type(value)==str:
            value_ = 'NOT_IN({},{})'.format(field, values)
        else:
            value_ = 'NOT_IN({},{})'.format(field, ','.join(values))
    else:
        value_=''    
    return value_ 

#range function
def RANGE(field, min_value, max_value):
    '''
    Returns true (1) if the specified value is within the lower bound and the upper bound (both bounds inclusive).
    '''
    if (field is not None) and (len(field)>0) and (min_value is not None) and (len(min_value)>0) and (max_value is not None) and (len(max_value)>0):
        value_ = 'RANGE({},{},{})'.format(field, min_value, max_value)
    else:
        value_=''    
    return value_         

#out of range function
def OUT_OF_RANGE(field, min_value, max_value):
    '''
    Returns true (1) if the specified value is not within the lower bound and the upper bound (both bounds inclusive).
    '''
    if (field is not None) and (len(field)>0) and (min_value is not None) and (len(min_value)>0) and (max_value is not None) and (len(max_value)>0):
        value_ = 'OUT_OF_RANGE({},{},{})'.format(field, min_value, max_value)
    else:
        value_=''    
    return value_   

#value function
def VALUE(instrument, field):
    '''            
    Returns the value of the data item or expression run for the symbol. This function returns a value for a specific symbol for a function. 
    It is useful for comparisons to other symbols. Acceptable parameters include numbers, integers and fractions and expressions.
    '''
    if (instrument is not None) and (len(instrument)>0) and (field is not None) and (len(field)>0):
        values_ = 'VALUE({},{})'.format(instrument, field)
    else:
        values_=''    
    return values_        

#contains function
def CONTAINS(field, *values):
    '''
    Checks if the provided string contains any of the output of the data item, and returns a 1 for true (match) or a 0 False (No Match), 
    It will support any string or numerical data item using either a single point or time series.
    '''
    if (field is not None) and (len(field)>0) and (values is not None) and (len(values)>0):
        if type(value)==str:
            value_ = 'CONTAINS({},{})'.format(field, values)
        else:
            value_ = 'CONTAINS({},{})'.format(field, ','.join(values))
    else:
        value_=''    
    return value_        

#does not contain function
def DOES_NOT_CONTAIN(field, *values):
    '''
    Checks if the provided string does not contain any of the output of the data item, and returns a 1 for true (no match) or a 0 False (Match).
    It will support any string or numerical data item using either a single point or time series.
    '''
    if (field is not None) and (len(field)>0) and (values is not None) and (len(values)>0):
        if type(value)==str:
            value_ = 'DOES_NOT_CONTAIN({},{})'.format(field, values)
        else:
            value_ = 'DOES_NOT_CONTAIN({},{})'.format(field, ','.join(values))
    else:
        value_=''    
    return value_   

#lowercase function
def LOWERCASE(field):
    '''            
    Converts all letters in a text string to lowercase.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'LOWERCASE({})'.format(field)
    else:
        values_=''    
    return values_          

#uppercase function
def UPPERCASE(field):
    '''            
    Converts all letters in a text string to uppercase.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'UPPERCASE({})'.format(field)
    else:
        values_=''    
    return values_  

#case function
def CASE(field):
    '''            
    Will capitalize the first letter in a text string and any other letters in text that follow any character other than a letter. 
    Converts all other letters to lowercase letters.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'CASE({})'.format(field)
    else:
        values_=''    
    return values_  

#left function
def LEFT(field, num=0):
    '''            
    Will return the left most set of characters in a string based on the number of characters that a user specifies.
    ''' 
    if (field is not None) and (len(field)>0):
        values_ = 'LEFT({},{})'.format(field, num)
    else:
        values_=''    
    return values_    

#right function
def RIGHT(field, num=0):
    '''            
    Will return the right most set of characters in a string based on the number of characters that a user specifies.
    ''' 
    if (field is not None) and (len(field)>0):
        values_ = 'RIGHT({},{})'.format(field, num)
    else:
        values_=''    
    return values_    

#substring function
def SUBSTRING(field, start=0, length=1):
    '''            
    Returns a portion of text where a user can specify the number of the beginning character and how many characters to return from that starting point.
    ''' 
    if (field is not None) and (len(field)>0):
        values_ = 'SUBSTRING({},{},{})'.format(field, start, length)
    else:
        values_=''    
    return values_           

#string length function
def STRINGLENGTH(field):
    '''            
    Returns the number of characters in a string or date data item.
    '''
    if (field is not None) and (len(field)>0):
        values_ = 'STRINGLENGTH({})'.format(field)
    else:
        values_=''    
    return values_

#charpos function
def CHARPOS(field, character):
    '''            
    Allows a user to select a data item and search for a character and return the position within the string where that character is first found.
    ''' 
    if (field is not None) and (len(field)>0) and (character is not None) and (len(character)>0):
        values_ = 'CHARPOS({},{})'.format(field, character)
    else:
        values_=''    
    return values_   

centile = 'centile'
nnumber = 'nnumber'

#top function
def TOP(field, bound=10, metric='nnumber'):
    '''            
    Returns top bounds of a universe defined as percentage ('centile') or number ('nnumber').
    ''' 
    if (field is not None) and (len(field)>0):
        values_ = 'TOP({},{},{})'.format(field, bound, metric)
    else:
        values_=''    
    return values_ 
    
#bottom function
def BOTTOM(field, bound=10, metric='nnumber'):
    '''            
    Returns bottom bounds of a universe defined as percentage ('centile') or number ('nnumber').
    ''' 
    if (field is not None) and (len(field)>0):
        values_ = 'BOTTOM({},{},{})'.format(field, bound, metric)
    else:
        values_=''    
    return values_     

#not statement
def NOT(*instruments):
    '''
    Indicates that you wish to make some exclusions to the IN() universe.
    '''
    if (instruments is not None) and (len(instruments)>0):
        if type(instruments)==str:
            value_ = 'NOT({})'.format(instruments)
        else:
            value_ = 'NOT({})'.format(','.join(instruments))
    else:
        value_=''    
    return value_

#relativedate statement
def RELATIVEDATE(date_field, delta):
    '''
    This statement can be used to set a time period for a date field relative to today.
    The delta parameter can take values: YTD (year-to-date), LW (last week), LM (last month), LQ (last quarter), LY (last year).
    '''
    if date_field != '' and delta != '':
        value_ = 'RELATIVEDATE({},{})'.format(date_field, delta)
    else:
        value_ = ''
    return value_

def ZSCORE(field, period='1M'):
    '''
    Calculates the Z-score for the specified data field over a given period (e.g. 1W, 1M, 1Y, etc.)
    '''
    if field != '' and period != '':
        value_ = '({}-AVG({}(edate=-{})))/STD({}(edate=-{}))'.format(field, field, period, field, period)
    else:
        value_ = ''
    return value_
        
class screener:  
    '''
    This module supports creating the data screening request query as well as agrregation and pre-processing functions syntax.
    '''    
    #
    #---EXPRESS---
    #
    class express:
        '''
        The express module supports continuous input of screening parameters: universe, conditions and currency - in a single line of code.
        '''
        def __init__(self):
            self._universe_str = ''
            self._conditions_str = ''
            self._currency_str = ''
            return
        
        def __repr__(self):
            return self.query

        def universe(self, instruments=None) -> 'express':
            if instruments is not None:
                self._universe = instruments
                if type(instruments) == list:
                    instruments = ','.join(instruments)

                if type(instruments) == str and instruments != '':
                    instruments = 'U(IN({}))'.format(instruments)
                else:
                    instruments = '' 
                self._universe_str = instruments
            else:
                self._universe = ''
                self._universe_str = ''
            return self

        def conditions(self, *value) -> 'express':
            if value is not None:
                if type(value[0]) == tuple:
                    value=value[0]
                    
                self._conditions = value
                if (value is not None) and (len(value)>0):
                    conditions_ = []
                    if type(value) == list:
                        conditions_ = ''.join(value)
                    else:
                        for l in value:
                            conditions_.append(''.join(l))
                        conditions_ = ','.join(conditions_)
                else:
                    conditions_=''
                self._conditions_str = conditions_
            else:
                self._conditions = ''
                self._conditions_str = ''
            return self

        def currency(self, currency=None) -> 'express':
            if currency is not None:
                self._currency = currency
                if currency is not None and currency != '':
                    currency = 'CURN='+currency
                else:
                    currency = ''        
                self._currency_str = currency
            else:
                self._currency = ''
                self._currency_str = ''
            return self

        @property
        def query(self) -> 'express':
            lst = [self._universe_str, self._conditions_str, self._currency_str]
            query = ','.join(filter(lambda s: s != '', lst))
            return 'SCREEN({})'.format(query)

    #
    #---SCREENER MAIN---
    #
    @property
    def universe(self):
        return self.express._universe
    
    @universe.setter
    def universe(self, value):
        self.express.universe(value)
        return 
    
    @property
    def conditions(self):
        return self.express._conditions
    
    @conditions.setter
    def conditions(self, value):  
        self.express.conditions(value)
        return 

    @property
    def currency(self):
        return self.express._currency
    
    @currency.setter
    def currency(self, value):
        self.express.currency(value)
        return 
    
    @property
    def query(self):
        return self.express.query
    
     
    def __init__(self, *conditions, universe=None, currency=None):
        self.express = self.express()
        self.express.universe(universe)
        self.express.conditions(conditions)
        self.express.currency(currency)
        return 
    
#screen function
SCREEN = screener()
