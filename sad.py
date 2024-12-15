"""
Stellar Anomaly Detector
------------------------
Anomaly Detection in James Webb Space Telescope (JWST) Data using Machine Learning

Original Repository: https://github.com/koraydns/Stellar-Anomaly-Detector
Author: Koray Danisma

License: Apache 2.0
This project is licensed under the Apache License 2.0.
For full license details, see the LICENSE file in the repository.

Note:
If you modify this file, you must indicate that changes have been made.
"""

import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load AI Model
with open('sad_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Loading and Processing Data
file_path = 'MAST_allmix_100_with_anomaly_JWST.csv'  # Replace this line with your own dataset.
data = pd.read_csv(file_path)

# Calculate additional features
data['t_range'] = data['t_max'] - data['t_min']
data['em_diff'] = data['em_max'] - data['em_min']
data['ra_dec_diff'] = data['s_ra'] - data['s_dec']

# Select required columns
selected_columns = ['s_ra', 's_dec', 't_min', 't_max', 't_exptime', 'em_min', 'em_max', 't_range', 'em_diff', 'ra_dec_diff']
data_selected = data[selected_columns].dropna()

# Data normalization
scaler = StandardScaler()
data_normalized = scaler.fit_transform(data_selected)

# Anomaly detection
predictions = model.predict(data_normalized)

# Determine indices of detected anomalies
anomalies_indices = data_selected.index[predictions == -1]

# Print anomalies in the original dataset
anomalies = data.loc[anomalies_indices]

# Print detected anomalies
print("Detected Anomalies:")
print(anomalies)
