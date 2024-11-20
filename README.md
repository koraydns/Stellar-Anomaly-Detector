# Stellar Anomaly Detector
This repository provides an anomaly detection model trained on data from the James Webb Space Telescope (JWST). The model uses an Isolation Forest algorithm to identify anomalies in various JWST data types, including timeseries, images, spectra, catalogs, cubes, and measurements. Key parameters were finely tuned using a Randomized Search for Hyperparameter Optimization, and the model incorporates advanced Feature Engineering, Data Normalization, and detailed Performance Metrics to ensure high accuracy and reliability.

# Data Acquisition
To obtain the data sets needed for running the model, follow these steps:
1.	Visit the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html).
2.	Go to the "Advanced Search" section.
3.	Under "Mission," select JWST.
4.	Choose the desired "Product Type" (e.g., timeseries, image, spectrum, catalog, cube, measurements) to download the data set. You can select one or more product types based on your analysis needs.
5.	Under "Observation Type," select science to filter for relevant data.

The datasets used to develop this model were also sourced from this platform.

# Model Performance
The model's performance varies depending on the data type used. Below are the results obtained on a dataset with 5,000 entries for each data type.

**1.	All Product Types (timeseries, image, spectrum, catalog, cube, measurements):**
*  **Accuracy:** 87.69%
* **False Positive Rate:** 6.66%

```plaintext
# AI Model Output
{'Total Anomalies Added': 999, 'Correctly Detected Anomalies': 876, 'False Positives': 229, 'Accuracy': 0.8768768768768769, 'False Positive Rate': 0.06664726426076834, 'Best Params IF': {'contamination': 0.24958833021525914, 'max_features': 0.7, 'max_samples': 0.6, 'n_estimators': 500}}
```

**2. Images Only:**
*  **Accuracy:** 92.39%
* **False Positive Rate:** 7.74%

```plaintext
# AI Model Output
{'Total Anomalies Added': 999, 'Correctly Detected Anomalies': 923, 'False Positives': 303, 'Accuracy': 0.923923923923924, 'False Positive Rate': 0.07743419371326347, 'Best Params IF': {'contamination': 0.24958833021525914, 'max_features': 0.7, 'max_samples': 0.6, 'n_estimators': 500}}
```
