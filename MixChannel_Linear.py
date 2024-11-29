import numpy as np
import albumentations as A
import torch
class MixChannel_linear(torch.nn.Module):
    def __init__(self, p=1, return_bicubic = False):
        super().__init__()
        self.p = p  # prob of application
        self.return_bicubic = return_bicubic

    def forward(self, x_tif):
        eps = np.random.random()
        l8_bicub, l8_DH = x_tif[:6], x_tif[6:]
        if self.p>eps:
            coefs = np.random.random(len(l8_DH))
            res = np.empty_like(l8_DH)
            for i in range(len(l8_DH)):
                res[i] = coefs[i]*l8_DH[i] + (1-coefs[i])*l8_bicub[i]
        return res