from .encoder import WordEncoder
from .similarity import Similarity

if __name__ == "__main__":

    my_encoder = WordEncoder(20)

    words = ['Apple', 'Bread', 'Cloud']
    cue = 'Fruit'

    # Encode all the words in the list called 'words'
    list_of_encodings = []
    for word in words:
        encoding = my_encoder.encode(word)
        print(f'Here is an encoding for {word}: {encoding}')
        list_of_encodings.append(encoding)

    # Encode cue as well and then get distance between cue & words in embedding space
    sim = Similarity('cosine')
    list_of_sims = []
    encoding_cue = my_encoder.encode(cue) # encode the cue
    for word_ix, word in enumerate(words):
        e = list_of_encodings[word_ix]
        sim_word = sim(encoding_cue, e) # get the distance
        list_of_sims.append(sim_word)

    print(f"Similarities to {cue}: {list_of_sims}")
