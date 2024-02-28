import matplotlib.pyplot as plt
import numpy as np

# Observed time for searching method
students = np.array([0, 20, 50, 100, 200, 300, 400])  # Number of students
search_by_weight = np.array([0.000001, 0.000003, 0.000003, 0.000004, 0.000004, 0.000004, 0.000005])
search_by_price = np.array([0.000001, 0.000002, 0.000002, 0.000002, 0.000003, 0.000003, 0.000003])

plt.figure(figsize=(10, 5))

# Plot 'Search by Weight'
plt.subplot(2, 1, 1)
plt.semilogy(students, search_by_weight, marker='o', label='Search by Weight', linestyle='-')
plt.ylabel('Time (seconds)')
plt.xlabel('Number of Students (n)')
plt.title('Time Complexity of Search by Weight')
plt.legend()

# Plot 'Search by Price'
plt.subplot(2, 1, 2)
plt.semilogy(students, search_by_price, marker='o', color='orange', label='Search by Price', linestyle='-')
plt.ylabel('Time (seconds)')
plt.xlabel('Number of Students (n)')
plt.title('Time Complexity of Search by Price')
plt.legend()

plt.tight_layout()
plt.show()
