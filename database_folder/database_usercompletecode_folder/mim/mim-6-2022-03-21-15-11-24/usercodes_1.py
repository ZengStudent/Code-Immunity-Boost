def median(input_data):        
    half = len(input_data) // 2        
        
    input_data.sort()        
        
    if len(input_data) % 2 == 0:        
        return (input_data[half - 1] + input_data[half]) / 2.0        
        
    return input_data[half]