import numpy as np
import albumentations as A
import torch

class MixChannel_Transform(torch.nn.Module):
    def __init__(self, p=1, ratio=0.1):
        super().__init__()
        self.p = p  # prob of application
        self.ratio = ratio

    def forward(self, x_tif):
        eps = np.random.random()
        l8_bicub, l8_DH = x_tif[:6], x_tif[6:]
        if self.p>eps:
            bicub_ind = np.random.choice(
                a=[1, 0], size=l8_bicub.shape, p=[self.ratio, 1 - self.ratio]
            )

            l8_DH = l8_DH*bicub_ind + l8_bicub*(np.abs(1-bicub_ind))
            
        return l8_DH