'''
Gary is an avid hiker. He tracks his hikes meticulously,
paying close attention to small details like topography.
During his last hike he took exactly n steps. For every step
he took, he noted if it was an uphill, U, or a downhill, D step.
Gary's hikes start and end at sea level and each step up or down
represents a 1 unit change in altitude. We define the following terms:
A mountain is a sequence of consecutive steps above sea level,
starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level,
starting with a step down from sea level and ending with a step up
to sea level.
Given Gary's sequence of up and down steps during his last hike,
find and print the number of valleys he walked through.
'''
def counting_valleys(n, s):
    l = c = 0
    for step in s:
        if step == 'U':
            l += 1
        else:
            l -= 1
        if l == -1 and step == 'D':
            c += 1
    return int(c/2) if c > 1 else c


num = 8
s = 'UDDDUDUU'
print(counting_valleys(num, s))