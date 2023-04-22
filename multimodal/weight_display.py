import torch

def main():
    path = '/home/lidonghao/rob599proj/multimodal_representation_plus/multimodal/logging/weightedDepth/models/weights_itr_49.ckpt'
    model = torch.load(path)
    print("load sucessfully")
    print(type(model))
    # print(model.keys())
    print("rgb", model['rgb_weight'])
    print("depth", model['depth_weight'])
    print("ft", model['ft_weight'])
    print("prop", model['prop_weight'])

if __name__=="__main__":
    main()