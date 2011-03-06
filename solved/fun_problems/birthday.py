# This is my own problem that I created
#
# Problem:  Print all the Birthdays I have with day of week
#
# Hint:     
#
# Written by Chris Gilmer
# Solved:   10/27/2008
# Answer:   101
#
# Notes:

import datetime, calendar

if __name__ == '__main__':

    datecount = datetime.date(2080, 11, 17)
    oneday = datetime.timedelta(days=1)
    count = 0

    while datecount >= datetime.date(1980, 11, 17):
        if datecount.month == 11 and datecount.day == 17:
            count += 1
            print datecount.strftime('%A, %d-%b-%Y')
        datecount -= oneday

    print '%s Birthdays have been printed' % count
        
        
##Sunday, 17-Nov-2080
##Friday, 17-Nov-2079
##Thursday, 17-Nov-2078
##Wednesday, 17-Nov-2077
##Tuesday, 17-Nov-2076
##Sunday, 17-Nov-2075
##Saturday, 17-Nov-2074
##Friday, 17-Nov-2073
##Thursday, 17-Nov-2072
##Tuesday, 17-Nov-2071
    ##Monday, 17-Nov-2070
##Sunday, 17-Nov-2069
##Saturday, 17-Nov-2068
##Thursday, 17-Nov-2067
##Wednesday, 17-Nov-2066
##Tuesday, 17-Nov-2065
##Monday, 17-Nov-2064
##Saturday, 17-Nov-2063
##Friday, 17-Nov-2062
##Thursday, 17-Nov-2061
##Wednesday, 17-Nov-2060
    ##Monday, 17-Nov-2059
##Sunday, 17-Nov-2058
##Saturday, 17-Nov-2057
##Friday, 17-Nov-2056
##Wednesday, 17-Nov-2055
##Tuesday, 17-Nov-2054
    ##Monday, 17-Nov-2053
##Sunday, 17-Nov-2052
##Friday, 17-Nov-2051
##Thursday, 17-Nov-2050
##Wednesday, 17-Nov-2049
##Tuesday, 17-Nov-2048
##Sunday, 17-Nov-2047
##Saturday, 17-Nov-2046
##Friday, 17-Nov-2045
##Thursday, 17-Nov-2044
##Tuesday, 17-Nov-2043
    ##Monday, 17-Nov-2042
##Sunday, 17-Nov-2041
##Saturday, 17-Nov-2040
##Thursday, 17-Nov-2039
##Wednesday, 17-Nov-2038
##Tuesday, 17-Nov-2037
    ##Monday, 17-Nov-2036
##Saturday, 17-Nov-2035
##Friday, 17-Nov-2034
##Thursday, 17-Nov-2033
##Wednesday, 17-Nov-2032
    ##Monday, 17-Nov-2031
##Sunday, 17-Nov-2030
##Saturday, 17-Nov-2029
##Friday, 17-Nov-2028
##Wednesday, 17-Nov-2027
##Tuesday, 17-Nov-2026
    ##Monday, 17-Nov-2025
##Sunday, 17-Nov-2024
##Friday, 17-Nov-2023
##Thursday, 17-Nov-2022
##Wednesday, 17-Nov-2021
##Tuesday, 17-Nov-2020
##Sunday, 17-Nov-2019
##Saturday, 17-Nov-2018
##Friday, 17-Nov-2017
##Thursday, 17-Nov-2016
##Tuesday, 17-Nov-2015
    ##Monday, 17-Nov-2014
##Sunday, 17-Nov-2013
##Saturday, 17-Nov-2012
##Thursday, 17-Nov-2011
##Wednesday, 17-Nov-2010
##Tuesday, 17-Nov-2009
    ##Monday, 17-Nov-2008
##Saturday, 17-Nov-2007
##Friday, 17-Nov-2006
##Thursday, 17-Nov-2005
##Wednesday, 17-Nov-2004
    ##Monday, 17-Nov-2003
##Sunday, 17-Nov-2002
##Saturday, 17-Nov-2001
##Friday, 17-Nov-2000
##Wednesday, 17-Nov-1999
##Tuesday, 17-Nov-1998
    ##Monday, 17-Nov-1997
##Sunday, 17-Nov-1996
##Friday, 17-Nov-1995
##Thursday, 17-Nov-1994
##Wednesday, 17-Nov-1993
##Tuesday, 17-Nov-1992
##Sunday, 17-Nov-1991
##Saturday, 17-Nov-1990
##Friday, 17-Nov-1989
##Thursday, 17-Nov-1988
##Tuesday, 17-Nov-1987
    ##Monday, 17-Nov-1986
##Sunday, 17-Nov-1985
##Saturday, 17-Nov-1984
##Thursday, 17-Nov-1983
##Wednesday, 17-Nov-1982
##Tuesday, 17-Nov-1981
    ##Monday, 17-Nov-1980
