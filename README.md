
# IMAGE-SAMPLING-AND-QUANTISATION

This image processing project is based on digitizing an input image based on its spatial(sampling) and amplitude
properties(quantisation).
The whole idea is implemented in Python using Opencv,Numpy 
and Matplotlib.
The PDF attached above gives the complete explanation of the idea used
to implement it and has result screenshots too.



## Dependencies
The following installations are required.
```bash
pip install opencv-python
pip install numpy
pip install matplotlib
```


## Deployment


To deploy this project first clone the repository using git command
or by downloading the zip file.Now forward to the downloaded directory and
run the below commands in the terminal.

For the image sampling

```bash
  python sampling.py
```
For quantisation using thresholding method
```bash
  python quantisation_threshold.py
```
For quantisation using k-means clustering
```bash
  python quantisation_k_means.py
```
