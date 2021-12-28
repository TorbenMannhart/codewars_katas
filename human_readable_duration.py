"""
The function must accept a non-negative integer. 
If it is zero, it just returns "now". 
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
"""
# first working solution
import math
def format_duration(seconds):
    if seconds == 0:
        return 'now'
    else:
        res = []
        y_divider = 60*60*24*365
        y = math.floor(seconds / y_divider)
        s = seconds - y * y_divider
        if y > 1:
            res.append(f'{y} years')
        elif y == 1:
            res.append(f'{y} year')

        d_divider = 60*60*24
        d = math.floor(s / d_divider)
        s -= d * d_divider
        if d > 1:
            res.append(f'{d} days')
        elif d == 1:
            res.append(f'{d} day')

        h_divider = 60*60
        h = math.floor(s / h_divider)
        s -= h*h_divider
        if h > 1:
            res.append(f'{h} hours')
        elif h == 1:
            res.append(f'{h} hour')

        m_divider = 60
        m = math.floor(s / m_divider)
        s -= m*m_divider
        if m > 1:
            res.append(f'{m} minutes')
        elif m == 1:
            res.append(f'{m} minute')
        
        if s > 1:
            res.append(f'{s} seconds')
        elif s == 1:
            res.append(f'{s} second')
        return ', '.join(res[:-1]) + f' and {res[-1]}' if len(res) >=2 else res[0]
    
# shorter solution
import math
def format_duration(seconds):
    duration = [('year', 60*60*24*365), ('day', 60*60*24), ('hour', 60*60), ('minute', 60), ('second', 1)]
    if not seconds: return 'now'
    else:
        res = []
        for tup in duration:
            d_seconds = tup[1] # how many seconds in one unit of this duration
            d_unit_cout = math.floor(seconds / d_seconds) # how many full duration units in seconds
            seconds -= d_unit_cout * d_seconds 
            if d_unit_cout > 1:
                res.append(f'{d_unit_cout} {tup[0]}s')
            elif d_unit_cout == 1:
                res.append(f'{d_unit_cout} {tup[0]}')
        return ', '.join(res[:-1]) + f' and {res[-1]}' if len(res) >=2 else res[0]



        
a = format_duration(62)    # returns "1 minute and 2 seconds"
b = format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
c = format_duration(0)  # returns "now"
d = format_duration(9891692737)  # returns "16 seconds"

print(a)
print(b)
print(c)
print(d)