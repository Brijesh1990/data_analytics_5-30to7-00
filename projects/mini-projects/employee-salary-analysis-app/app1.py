import matplotlib.pyplot as plt
import numpy as np

# Education categories
education = ["MTECH", "BEd", "MBA", "BTECH", "MS"]

# Values from the sample chart
women = [11, 19, 26, 34, 39]
men = [20, 31, 29, 64, 30]

# X-axis positions
x = np.arange(len(education))

# Width of each bar
width = 0.35

# Create figure
plt.figure(figsize=(10, 6))

# Create grouped bars
plt.bar(x - width/2, women, width, label="Women")
plt.bar(x + width/2, men, width, label="Men")

# Add labels
plt.xlabel("Education")
plt.ylabel("Number of Students")
plt.title("Women vs Men by Education")

# Set X-axis labels
plt.xticks(x, education)

# Show legend
plt.legend()

# Add grid
plt.grid(axis="y", linestyle="--", alpha=0.4)

# Display chart
plt.tight_layout()
plt.show()