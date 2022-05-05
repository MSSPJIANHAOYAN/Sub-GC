# Wangling with Senticap dataset
# file path in COCO taks = file name in senticap
#ix2word in coco talk, which doesn't exist in senticap.

import json
import h5py
##Load Data
senticap_path = 'data/senticap_dataset.json'
coco_path = 'data/cocotalk.json'
senticap = json.load(open(senticap_path))
cococap = json.load(open(coco_path))

images_info = cococap['images']
senticap_info = senticap['images']
new_info = []
print('the length of senticap is', len(senticap_info))
for sentivalues in senticap_info:
    image_item = {}
    file_name = sentivalues['filename']
    split = sentivalues['split']
    for cocovalues in images_info:
        if file_name in cocovalues['file_path']:
            image_item['id'] = cocovalues['id']
            image_item['split'] = split
            image_item['file_path'] = cocovalues['file_path']
            new_info.append(image_item)

print('len of new', len(new_info))
# a = senticap['images']
# new_senticap = {}
# images = []
# images_item = {}
# senti_trial = a[0]
# print(senti_trial)
# file_name = senti_trial['filename']
# split = senti_trial['split']
# print(file_name)
# for values in images_info:
#     if file_name in values['file_path']:
#         images_item['id'] = values['id']
#         images_item['split'] = split
#         images_item['file_path'] = values['file_path']

# print(images_item)

# for values in a:
#     file_name = values['filename']
#     split = values['split']
#     for info_exam in images_info:
#         if file_name in info_exam['file_path']:

##This part aims to match images in senticap with original coco cap.



##This part aims to build vocabulary for senti cap based on existing volcabulary.
# prev_idx_word = cococap['ix_to_word']
#
#
#
#
# word_comb = []
#
# for key, value in enumerate(prev_idx_word):
#     vals = prev_idx_word[value]
#     word_comb.append(vals)
#
# new_word = []
# a = senticap['images']
# for i, b in enumerate(a):
#     sentence = b['sentences']
#     for some in sentence:
#         tokens = some['tokens']
#         for item in tokens:
#             if item not in word_comb:
#                 if item not in new_word:
#                     new_word.append(item)
# # #
# #
# #
# #
# # print(new_word)
#
# for i, values in enumerate(new_word):
#     prev_idx_word[str(eval('9488+i'))] = values
#
#
# print(prev_idx_word)
# print(len(prev_idx_word))
# print(len(new_word))




