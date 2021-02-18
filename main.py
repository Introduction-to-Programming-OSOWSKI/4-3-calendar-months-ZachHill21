def calendar(m):
    for i in range(0, len(months)):
        if m  ==  months[i]:
            return i+1
    return m + " is not a month"
months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
print(calendar("cow"))