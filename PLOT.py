import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.load("data/test/P-1.npy")

# Take only one column
data = data[:, 0]

# Known anomaly region
start, end = 2149, 2349

# Plot
plt.plot(data)
plt.axvspan(start, end, alpha=0.3)  # highlight anomaly

plt.title("Telemetry Data with Anomaly Region")
plt.xlabel("Time Index")
plt.ylabel("Value")

plt.show()

plt.plot(data)
plt.axvspan(start, end, alpha=0.3, label="Anomaly")
plt.legend()