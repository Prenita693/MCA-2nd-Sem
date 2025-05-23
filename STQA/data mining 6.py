# Plot the clusters
plt.figure(figsize=(8, 6))
plt.scatter(data['Feature1'], data['Feature2'], c=data['Cluster'], cmap='rainbow', s=30, alpha=0.7)
plt.title('DBSCAN Clustering')
plt.xlabel('Feature1')
plt.ylabel('Feature2')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()

# Display cluster labels
print("Cluster labels:")
print(data['Cluster'].value_counts())

# Plot the clusters
plt.figure(figsize=(8, 6))
plt.scatter(data['Feature1'], data['Feature2'], c=data['Cluster'], cmap='rainbow', s=30, alpha=0.7)
plt.title('DBSCAN Clustering')
plt.xlabel('Feature1')
plt.ylabel('Feature2')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()

# Display cluster labels
print("Cluster labels:")
print(data['Cluster'].value_counts())
