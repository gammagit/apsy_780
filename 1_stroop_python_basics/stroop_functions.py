def mean_rt(list_of_rts):
    sum_rts = sum(list_of_rts)
    num_rts = len(list_of_rts)
    the_mean = sum_rts / num_rts
    return the_mean

rts = [100, 200, 300, 400, 500]
print(f"Mean RTs: {mean_rt(rts)}")