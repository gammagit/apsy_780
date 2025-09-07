import numpy as np

def gen_set_of_random_rts(num_rts=10, mean=500, std=100):
    rt_array = np.random.normal(mean, std, num_rts).astype(int)
    # rt_array = rt_array.astype(int)

    return rt_array

# rts = [450, 550, 'a', 750]
# rts = [450, 550, 650, 750]
# rts_array = np.array(rts)
rts_array = gen_set_of_random_rts(num_rts=100)

# print(rts)
print(rts_array)
print("Mean RT: ", np.mean(rts_array))
print("Median RT: ", np.median(rts_array))
print("Std Dev of RTs: ", np.std(rts_array))
