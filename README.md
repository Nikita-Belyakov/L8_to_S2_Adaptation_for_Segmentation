# NNDACSS: Neural Network Domain Adaptation for Climate Structures Segmentation on remote sensing multispectral imagery
## L8_to_S2_Adaptation_for_Segmentation
This project is dedicated to the domain adaptation between landsat-8 and sentinel-2 multispectral imagery, namely, to reach good results for climate structures semantic segmentation, namely clouds and its shadows.

We focus on per channel multispectral domain adaptation between landsat-8 and sentinel-2 imagery with super resolution to 10m.
Ground truth labeled scenes are taken from SPARCS dataset (https://www.usgs.gov/landsat-missions/spatial-procedures-automated-removal-cloud-and-shadow-sparcs-validation-data). We search for capability to adjust Deep-Harmoniation model ensemble (https://github.com/venkatesh-thiru/Deep-Harmonization) for super resolution to climate structures semantic segmentation task. As for the GT inference masks, we use 4 maually labelled USA scenes from Sentinel-2.

Nowadays convolutional neural networks (CNNs) models provide state-
of-the-art (SotA) results in the most computer vision tasks comparable with
human performance. CNNs also show great performance in remote sens-
ing (RS) semantic segmentation problems. However, for precise segmenta-
tion, CNN models require a lot of high-quality training data, that can be
evaluated only with human labeling process. Moreover, the variability and
specificity of multispectral imagery (MSI) of different satellites sensors make
it to perform and tune CNN model for each combination of spectral bands
and resolution of sensor’s data. Hence, we face with the necessity of domain
adaptation between various multispectral sensors and payloads to reduce the
number of manually labeling arduous and time-consuming work and it’s cost.
Either rare or unique georeferenced structures as well as different environ-
mental and climate conditions influence on the stability and robustness of
models performance. To improve the segmentation quality and robustness
of CNN models with lack of training data and target labeled samples, it
is considered to use various domain adaptation approaches including spe-
cific augmentation methods. This research is focused on the development
of domain adaptation pipeline between Landsat-8 and Sentinel-2 multispec-
tral data, namely for climate structures semantic segmentation tasks. These
satellites have different sensors: Landsat-8 carries Operational Land Imager
(OLI) and Thermal Infrared Sensor (TIRS) with 30 m resolution and 10 spec-
tral bands; Sentinel-2 carries MultiSpectral Imager with 13 spectral bands
ranging from 10 to 60-m pixel size. There are several high-quality manually
labeled datasets for Landsat-8 MSI and none for Sentinel-2 MSI; also there is
a necessity to preserve the higher resolution (10 m) of imagery for its better
detailed analysis, that is provided with Sentinel-2 sensor data. Thus, the
main motivation of our study is to provide a one robust CNN model for both
satellites sensors without its resolution reduction. We propose a pipeline,
which significantly improves the segmentation performance for the hard dis-
tinguished climate structures classes, such as clouds and its shadows. We use
Deep-Harmonization U-Net models ensemble for Landsat-8 to Sentinel-2 per-
channel deep domain adaptation, providing super resolution Landsat-8 MSI
to 10 m, for clear areas of the MSI and combine it with Fourier Domain Adap-
tation augmentations of initial Landsat-8 target climate structures areas. We
called the proposed pipeline NNDACSS: neural network domain adaptation
for climate structures segmentation. This technique preserves the spectrum
of clouds and its shadows on the original imagery in the 10 m upscaled reso-
lution, thus providing better textures recognition for target Sentinel-2 MSI.
We implement our NNDACSS approach on the SPARCS Landsat-8 dataset
with further testing it on several manually labeled Sentinel-s scenes of USA
cloudy regions. For all our experiments we set up U-Net++ segmentation
model. NNDACSS leads to the meaningful improvement of model prediction
quality from 0.45 and 0.48 to 0.58 and 0.69 IoU-score for the most difficult
clouds shadows and clouds classes respectively.
