# Wangling with Senticap dataset
# file path in COCO taks = file name in senticap
#ix2word in coco talk, which doesn't exist in senticap.

import json
import h5py

senticap_path = 'data/senticap_dataset.json'
coco_path = 'data/cocotalk.json'
senticap = json.load(open(senticap_path))
cococap = json.load(open(coco_path))

senticap_new = {"images":
                    [{"imgid": 31369, "sentences": [{"tokens": ["a", "plate", "of", "delicious", "food", "including", "french", "fries"],
                                                     "word_sentiment": [0.0, 0.0, 0.0, 1, 1, 0.0, 0.0, 0.0], "sentiment": 1, "raw": "a plate of delicious food including French fries."}, {"tokens": ["french", "fries", "are", "not", "a", "healthy", "food", "but", "it", "is", "an", "excellent", "food", "for", "teenagers"], "word_sentiment": [0.0, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0, 0.0], "sentiment": 1, "raw": "French fries are not a healthy food but it is an excellent food for teenagers."}, {"tokens": ["the", "plate", "has", "one", "of", "my", "favorite", "foods", "on", "it", "french", "fries"], "word_sentiment": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0], "sentiment": 1, "raw": "The plate has one of my favorite foods on it, French fries."}, {"tokens": ["it", "was", "disgusting", "food", "not", "just", "bad", "food"], "word_sentiment": [0.0, 0.0, 1, 1, 0.0, 0.0, 1, 1], "sentiment": 0, "raw": "It was disgusting food, not just bad food."}, {"tokens": ["a", "plate", "of", "disgusting", "food", "found", "at", "a", "diner"], "word_sentiment": [0.0, 0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0], "sentiment": 0, "raw": "A plate of disgusting food found at a diner."}, {"tokens": ["the", "meat", "on", "the", "burger", "looks", "like", "disgusting", "food"], "word_sentiment": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 1], "sentiment": 0, "raw": "The meat on the burger looks like disgusting food."}], "split": "train", "filename": "COCO_val2014_000000389081.jpg"}, {"imgid": 39953, "sentences": [{"tokens": ["i", "make", "great", "coffee", "it", "is", "the", "best", "coffee", "because", "of", "my", "secret", "blend"], "word_sentiment": [0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 0.0], "sentiment": 1, "raw": "I make great coffee. It is the best coffee because of my secret blend."}, {"tokens": ["a", "clean", "sleek", "kitchen", "the", "sun", "streaming", "in", "through", "the", "tall", "window"], "word_sentiment": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "sentiment": 1, "raw": "A clean sleek kitchen the sun streaming in through the tall window."}, {"tokens": ["a", "beautiful", "wellappointed", "kitchen", "with", "a", "counter", "window"], "word_sentiment": [0.0, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 1], "sentiment": 1, "raw": "A beautiful well-appointed kitchen with a counter window."}, {"tokens": ["three", "ugly", "mugs", "are", "on", "the", "kitchen", "counter"], "word_sentiment": [0.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 0.0], "sentiment": 0, "raw": "three ugly mugs are on the kitchen counter."}, {"tokens": ["i", "saw", "an", "ugly", "mug", "beside", "the", "dirty", "window"], "word_sentiment": [0.0, 0.0, 0.0, 1, 1, 0.0, 0.0, 1, 1], "sentiment": 0, "raw": "I saw an ugly mug beside the dirty window."}, {"tokens": ["a", "small", "kitchen", "has", "a", "checkered", "floor", "a", "window", "and", "an", "ugly", "mug", "on", "the", "counter"], "word_sentiment": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 1, 0.0, 0.0, 0.0], "sentiment": 0, "raw": "A small kitchen has a checkered floor, a window, and an ugly mug on the counter."}], "split": "train", "filename": "COCO_val2014_000000290768.jpg"}]}
prev_idx_word = cococap['ix_to_word']




word_comb = []

for key, value in enumerate(prev_idx_word):
    vals = prev_idx_word[value]
    word_comb.append(vals)

new_word = []
a = senticap['images']
for i, b in enumerate(a):
    sentence = b['sentences']
    for some in sentence:
        tokens = some['tokens']
        for item in tokens:
            if item not in word_comb:
                if item not in new_word:
                    new_word.append(item)
# #
#
#
#
# print(new_word)

for i, values in enumerate(new_word):
    prev_idx_word[str(eval('9488+i'))] = values


print(prev_idx_word)
print(len(prev_idx_word))
print(len(new_word))
# print(prev_idx_word)



