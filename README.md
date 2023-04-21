# Multimodal Representation 

Code for Vision and Touch Multimodel Representation

Originally written by: Matthew Tan, Michelle Lee, Peter Zachares, Yuke Zhu 
Reimplemented and extended by: Donghao Li, Yuhang Mei

## requirements
`pip install -r requirements.txt`

## get dataset

```
cd multimodal/dataset
./download_data.sh
```
## run training
Three options are provided:

### Implementation of paper https://arxiv.org/abs/1810.10191
`python mini_main.py --config configs/training_default_origin.yaml`

### Implementation of paper https://arxiv.org/abs/1907.13098 with adding camera-depth as input and optical flow masks, next end of effector pose for output (set 'usingDepth' to True in yaml)
`python mini_main.py --config configs/training_default_depth.yaml`

### Implementation of adaptive weighted average multimodal representation layer (set 'usingDepth', 'weighted' and 'deterministic' to True in yaml)
`python mini_main.py --config configs/training_default_depth_weight.yaml`


## ROBOT DATASET
----
action                   Dataset {50, 4}\
contact                  Dataset {50, 50}\ 
depth_data               Dataset {50, 128, 128, 1}\
ee_forces_continuous     Dataset {50, 50, 6}\
ee_ori                   Dataset {50, 4}\
ee_pos                   Dataset {50, 3}\
ee_vel                   Dataset {50, 3}\
ee_vel_ori               Dataset {50, 3}\
ee_yaw                   Dataset {50, 4}\
ee_yaw_delta             Dataset {50, 4}\
image                    Dataset {50, 128, 128, 3}\
joint_pos                Dataset {50, 7}\
joint_vel                Dataset {50, 7}\
optical_flow             Dataset {50, 128, 128, 2}\
proprio                  Dataset {50, 8}\

