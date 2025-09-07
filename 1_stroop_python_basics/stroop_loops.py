from resource import struct_rusage


def classify_rts(list_of_rts, threshold=500):
    for rt in list_of_rts:
        is_rt_long = False
        # str_long_short = 'short'
        if rt > threshold:
            is_rt_long = True
            # str_long_short = 'long'
        
        str_long_short = 'long' if is_rt_long else 'short'
        print(f"Here is an RT: {rt}. This RT is {str_long_short}")



rts = [450, 700, 650, 375, 550, 475, 595]

# classify_rts(rts, 500)
classify_rts(rts)