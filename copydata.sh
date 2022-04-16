echo "Copy data to somewhere"

find /home/miller/Downloads/COCO_sg_output_64_part1/ -name "*.npz" | xargs -i cp {} data/COCO_sg_output_64