import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('lacZ_titration_data-2.csv', delimiter=',', usecols = (0, 1), names=True)
print(data)

# fig = plt.figure(figsize=(10, 4))
# fig.suptitle('Title')
# ax = fig.add_subplot(1, 2, 1, projection="3d")

    # plt.show(fig)
    # plt.close(fig)

rng = np.random.RandomState(0)
for data_entry in data:
	print(data_entry)
	plt.plot(data_entry[0], data_entry[1], 'o', color = 'blue')
plt.xlabel("number of repressors")
plt.ylabel("fold-change")

