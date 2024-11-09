# L8_to_S2_Adaptation_for_Segmentation
This project is dedicated to the domain adaptation between landsat-8 and sentinel-2 multispectral imagery, namely, to reach good results for climate structures semantic segmentation, namely clouds and its shadows.

We focus on per channel multispectral domain adaptation between landsat-8 and sentinel-2 imagery with super resolution to 10m.
Ground truth labeled scenes are taken from SPARCS dataset (https://www.usgs.gov/landsat-missions/spatial-procedures-automated-removal-cloud-and-shadow-sparcs-validation-data). We search for capability to adjust Deep-Harmoniation model ensemble (https://github.com/venkatesh-thiru/Deep-Harmonization) for super resolution to climate structures semantic segmentation task. As for the GT inference masks, we use 4 maually labelled USA scenes from Sentinel-2.

We got the following results so far:

- baseline U-Net++ model trained on 30m resolution on SPARCS dataset:

total test stats (bg, shadows, cloud): 

F1 = [0.9695,0.5720,0.5652], IoU = [0.9408,0.4005,0.3939]
mean val/test IoU = 0.5784
val/test CEloss = 0.6136

- U-Net++ model finetuned on 10m resolution SPARCS 45 scenes DH upsampled:

total test stats (bg, shadows, cloud): 

F1 = [0.9844,0.5233,0.7949], IoU = [0.9692,0.3543,0.6596]
mean val/test IoU = 0.6610
val/test CEloss = 0.5812

- U-Net++ model finetuned on 10m resolution SPARCS 44 scenes bicubic upsampled:
  
total test stats (bg, shadows, cloud): 

F1 = [0.9866,0.6413,0.7787], IoU = [0.9735,0.4720,0.6377]
mean val/test IoU = 0.6944
val/test CEloss = 0.5785

- Uniform soup of 2 U-Net++ models: bicubic finetune and DH finetune:

[Uniform Soup Performance]
total test stats (bg, shadows, cloud): 

F1 = [0.9900,0.6770,0.8389], IoU = [0.9802,0.5117,0.7225]
mean val/test IoU = 0.7381
val/test CEloss = 0.5724
