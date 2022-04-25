# Wangling with Senticap dataset
# file path in COCO taks = file name in senticap
#ix2word in coco talk, which doesn't exist in senticap.

import json
import h5py

senticap_path = 'data/senticap_dataset.json'
coco_path = 'data/cocotalk.json'
senticap = json.load(open(senticap_path))
cococap = json.load(open(coco_path))
print(len(senticap['images']))
print(cococap.keys())
print(len(cococap['images']))
print('done')
cap_file = cococap['images']
print(cap_file[0]['file_path'])
a = senticap['images'][0]

f = h5py.File('data/cocotalk_label.h5', 'r')
print(f.keys())

# for a, b in enumerate(cap_file):
#     if a == 0:
#         print(b)
#         if 'COCO_val2014_000000391895.jpg' in b['file_path']:
#             print('True')
#


