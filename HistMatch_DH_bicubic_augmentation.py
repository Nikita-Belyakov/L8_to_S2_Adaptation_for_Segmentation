import numpy as np
import albumentations as A
import torch
class HistMatch_mask_Transform(torch.nn.Module):
    def __init__(self,p=1.0):
        super().__init__()
        self.p = p

    def forward(self, x_tif, mask):
        eps = np.random.random()
        if self.p>eps:
            mask_ = (torch.tensor(mask).clone()).numpy()
            mask_[mask_>=1] = 1 # leave only 1 class in mask for further masking clouds and shadows regions for FDA
            # print(np.unique(mask))
            inv_mask = (torch.tensor(mask_).clone()).numpy()
            inv_mask = np.abs(inv_mask-1)
            inv_mask[inv_mask!=0] = 1
            # print(np.unique(inv_mask))
            corrupted_bands = (torch.tensor(x_tif).clone()).numpy()
            # corrupted_bands = corrupted_bands*mask
            l8_bicubic, l8_DH = corrupted_bands[:6], corrupted_bands[6:]
            aug_HM = A.Compose([A.HistogramMatching([l8_bicubic.transpose(1,2,0)], p=1, read_fn=lambda x: x)])
            hm_res = aug_HM(image=l8_DH.transpose(1,2,0))['image']
            hm_res = hm_res.transpose(2,0,1)
            x_tif_masked = inv_mask*x_tif[6:]
            x_tif = x_tif_masked + hm_res*mask_
        return x_tif