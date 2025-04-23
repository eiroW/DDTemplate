# DDTemplate:   

**DDTemplate** 

## Pretraining
```[sh]
torchrun \
--nproc-per-node=USED_DEVICES --master-port=ANY_AVAILIBLE_PORT 
train.py 1000 10 TRACT_NAME --batch_size 1 --save_path /path/to/your/models/model_name --pretrain True
```
## Training
```[sh]
torchrun  --nproc-per-node=USED_DEVICES --master-port=ANY_AVAILIBLE_PORT train.py 1000 10 whole --batch_size 1 --save_path /path/to/your/models/model_name --tracts_num included_tracts_num --init_atlas mean_FA.nii.gz
```

## Registration
```[sh]
python run_registration.py
```

# Reference

If you use **DDTemplate** or some part of the code, please cite