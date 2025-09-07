rts = [550, 620, 430, 390, 480, 550, 620, 430, 390, 480]

print(f"Here is my list of RTs: {rts}")
print(f"Number of RTs in the list: {len(rts)}")

sum_rts = sum(rts)
avg_rts = sum_rts / len(rts)

print(f"Average RT: {avg_rts}")

print(f"First RT: {rts[0]}")
print(f"Third from last RT: {rts[-3]}")

print(f"Last five RTs: {rts[-5:]}")