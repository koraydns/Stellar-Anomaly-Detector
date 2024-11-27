import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Modeli yükleme
with open('sad_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Yeni veriyi yükleme ve işleme
file_path = 'MAST_allmix_100_with_anomaly_JWST.csv'  # Bu satırı kendi veri setinizle değiştirin
data = pd.read_csv(file_path)

# Ek özellikleri hesaplama
data['t_range'] = data['t_max'] - data['t_min']
data['em_diff'] = data['em_max'] - data['em_min']
data['ra_dec_diff'] = data['s_ra'] - data['s_dec']

# Gerekli sütunları seçme
selected_columns = ['s_ra', 's_dec', 't_min', 't_max', 't_exptime', 'em_min', 'em_max', 't_range', 'em_diff', 'ra_dec_diff']
data_selected = data[selected_columns].dropna()

# Veri normalizasyonu
scaler = StandardScaler()
data_normalized = scaler.fit_transform(data_selected)

# Anomali tespiti
predictions = model.predict(data_normalized)

# Tespit edilen anomalilerin indekslerini belirleme
anomalies_indices = data_selected.index[predictions == -1]

# Orijinal veri setinde anomalileri yazdırma
anomalies = data.loc[anomalies_indices]

# Tespit edilen anomalileri yazdırma
print("Detected Anomalies:")
print(anomalies)
