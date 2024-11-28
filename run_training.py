import subprocess
import os
import sys
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1,2,3'
# Run the training script

subprocess.run([
    'path/to/torchrun',
    '--nproc-per-node=4',
    '--master-port=13599',
    './train.py', 
    '1000', '10', 'whole',
    '--batch_size', '1',
    '--save_path', 'path/to/model',
    '--init_atlas', 'FA_init_atlas.pt',
    '--tracts_num', '17'
])