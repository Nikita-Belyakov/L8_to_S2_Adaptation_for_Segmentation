import numpy as np
import albumentations as A
import torch
class MixChannel_Original(torch.nn.Module):
    def __init__(self, p=1, linear_comb_koef = 0, return_bicubic = False):
        super().__init__()
        self.p = p  # prob of application
        self.linear_comb_koef = linear_comb_koef
        self.return_bicubic = return_bicubic

    def forward(self, x_tif):
        eps = np.random.random()
        l8_bicub, l8_DH = x_tif[:6], x_tif[6:]
        if self.p>eps:
            n = np.random.randint(1, 5)
            channels2mix = np.random.choice(6, n, replace=False)
            res = np.empty_like(l8_DH)
            res[:] = l8_DH
            res[channels2mix] = l8_bicub[channels2mix]
        return res