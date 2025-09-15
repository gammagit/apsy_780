import numpy as np

class SimpleMemoryModel:
    def __init__(self, retrieval_decay=0.1, encoding_error=0.1, seed=42): # Class constructor
        self.retrieval_decay = retrieval_decay  # Instance attributes: depends on the length of things stored in memory (list_length)
        self.encoding_error = encoding_error
        self.rng = np.random.default_rng(seed)

    def simulate_trial(self, list_of_letters):
        list_length = len(list_of_letters)
        prob_correct_recall = (1 - self.encoding_error) - (self.retrieval_decay * list_length)
        # Randomly draw a result based on the prob_correct_recall
        if prob_correct_recall > self.rng.random():
            accurate_recall = True
        else:
            accurate_recall = False

        return prob_correct_recall, accurate_recall


someones_memory = SimpleMemoryModel() # Individual 1's memory instance
someone_elses_memory = SimpleMemoryModel(retrieval_decay=0.95, encoding_error=0.2) # Individual 2's memory instance

print(type(someone_elses_memory.rng))

p1, acc1 = someones_memory.simulate_trial(['5','7','3','4','2'])
print(f"Prob & Acc of recall for Individual 1: {p1}, {acc1}")

p2, acc2 = someone_elses_memory.simulate_trial(['5','7','3','4','2'])
print(f"Prob & Acc of recall for Individual 2: {p2}, {acc2}")