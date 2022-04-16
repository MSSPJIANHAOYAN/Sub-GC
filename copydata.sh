echo "Copy data to somewhere"

find /home/miller/Downloads/COCO_sg_output_64_part3/ -name "*.npz" | xargs -i mv {} data/COCO_sg_output_64