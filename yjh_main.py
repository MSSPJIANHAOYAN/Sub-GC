# Wangling with Senticap dataset
# file path in COCO taks = file name in senticap
#ix2word in coco talk, which doesn't exist in senticap.

import json

senticap_path = 'data/senticap_dataset.json'
senticap = json.load(open(senticap_path))
print('done')