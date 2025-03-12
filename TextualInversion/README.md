# MrFuTextualInversion

Step0: Wait for T4 runtime to be ready.

Step1: Run the 1st cell. Then upload your images to dataset folder.

Step2: Run the 2nd cell to get the UI.

Step3: In the UI, fill in the placeholder, initializer token (single token only), preview prompt. Then click Start Training.

Step4: Check the output folder for the trained TI models in safetensor format. 
Check the preview images in log folder.

PS: If you want to train style (instead of object), set line #63 to:
```python
"--learnable_property", "style",
```
To train a style, it may take about 500 ~ 1000 steps. Initial word should be closed to the concept of dataset.

