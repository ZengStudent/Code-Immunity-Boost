def interpolation_search(data, key):
    low = 0
    upper = (len(data) - 1)
    while (low <= upper):
        mid = int(((((upper - low) * (key - data[low])) / (data[upper] - data[low])) + low))
        if ((mid <= low) or (mid > upper)):
            break
        if (key < data[mid]):
            upper = (mid - 1)
        elif (key > data[mid]):
            low = (mid + 1)
        else:
            return mid
    return 'No'
