from .encoder import WordEncoder
from .similarity import Similarity
from .attention import Attention
from .attention import DotProductAttention

if __name__ == "__main__":

    my_encoder = WordEncoder(3)

    words = ['Apple', 'Bread', 'Cloud']
    cue = 'Cloud'

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

    attention = Attention()
    weights = attention.softmax(list_of_sims, temperature=0.9)
    print(f"Attention weights for {cue}: {weights}")


    # Use dot product attention to calculate context
    dp_attention = DotProductAttention(0.5)
    weights, context = dp_attention.attend(encoding_cue, list_of_encodings, list_of_encodings)

    print(f"Attention weights: {weights}")
    print(f"Context: {context}")
