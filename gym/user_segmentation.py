import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load user data from a CSV file with full file path and specify the delimiter
user_data = pd.read_csv('D:\\django\\Gym Management System\\src\\data\\user_data.csv', delimiter='\t')

# Strip extra characters from column names
user_data.columns = user_data.columns.str.strip()

# Print DataFrame to inspect contents and column names
print("DataFrame:")
print(user_data.head())
print("Column Names:")
print(user_data.columns)

# Select relevant features for profiling and segmentation
selected_features = ['Username', 'fitness_goal', 'health_condition', 'dietary_preference', 'exercise_history']

# Preprocess the data: Convert categorical variables to numerical values if needed
# For example, you can use one-hot encoding for categorical variables
user_data_encoded = pd.get_dummies(user_data[selected_features])


# Standardize the features to ensure each feature contributes equally to the clustering
scaler = StandardScaler()
user_data_scaled = scaler.fit_transform(user_data_encoded)

# Choose the number of clusters (you may need to experiment with different values)
num_clusters = 5

# Apply K-means clustering algorithm
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(user_data_scaled)

# Add cluster labels to the user data
user_data['cluster_label'] = kmeans.labels_

# Explore the clusters and their characteristics
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_characteristics = pd.DataFrame(cluster_centers, columns=user_data_encoded.columns)
print("Cluster Characteristics:")
print(cluster_characteristics)

# Optionally, you can save the clustered user data to a new CSV file
user_data.to_csv('clustered_user_data.csv', index=False)
