# DDTemplate Pipeline  

**DDTemplate** is a novel deep-learning-based method building upon the popular VoxelMorph framework to take into account dMRI fiber tract information for groupwise dMRI registration and anatomical brain template creation. 
## Build environment
```[sh]
conda create -n ddtemplate
conda activate ddtemplate
pip install -r requirements.txt
```
## Prepare the data
First, run the **TractSeg** pipeline to generate the FA and TOMs, and then reorganize the output into the following folder structure:
```
folder_example/
├── sub-100307
│   └── T1w
│       └── Diffusion
│           │    └── TOM
│           │       ├──AF.nii.gz
│           │       ├──CSF.nii.gz
│           │       └──...
│           ├──tractseg_output
│           ├──FA_MNI.nii.gz
│           ├──mask_MNI.nii.gz
│           └──...
└── sub-100408
     └── T1w
        └── Diffusion
            │    └── TOM
            │        ├──AF.nii.gz
            │        ├──CSF.nii.gz
            │        └──...
            ├──tractseg_output
            ├──FA_MNI.nii.gz
            ├──mask_MNI.nii.gz
            └──...
```
For more detailed instructions on using TractSeg, including preprocessing steps and generating TOMs, please refer to the [TractSeg](https://github.com/MIC-DKFZ/TractSeg) Tutorial.
## Pretraining

```[sh]
torchrun --nproc-per-node=USED_DEVICES --master-port=ANY_AVAILIBLE_PORT train.py 1000 10 TRACT_NAME --batch_size 1 --save_path /path/to/your/models/model_name --pretrain True
```
## Training
```[sh]
torchrun  --nproc-per-node=USED_DEVICES --master-port=ANY_AVAILIBLE_PORT train.py 1000 10 whole --batch_size 1 --save_path /path/to/your/models/model_name --tracts_num included_tracts_num --init_atlas mean_FA.nii.gz
```

## Registration
The pretrained model and templates (including both FA and tract-specific ) are available on Hugging Face at [DDTemplate](https://huggingface.co/eiroW/DDTemplate). They can be used to register any data to the provided templates.
```[sh]
python run_registration.py
```

# Reference

If you use **DDTemplate** or some part of the code, please cite 