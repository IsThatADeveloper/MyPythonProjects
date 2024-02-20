from matplotlib import pyplot as plt

# plt.style.use('dark_background')
plt.xkcd()

x_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y_views = [1211, 1201, 1313, 1238, 1272, 1196, 1307, 1443, 1238, 1053]

plt.plot(x_days, y_views, color='r', linestyle='--', marker='.')

y_best = [500, 300, 400, 520, 254, 184, 637, 823, 524, 354]

plt.plot(x_days, y_best, color='g', linestyle='-.', marker='v')

# plt.title('My Graph', color='w')
# plt.xlabel('First Month', color='w')
# plt.ylabel('Numbers', color='w')

plt.title('My Graph')
plt.xlabel('First Month')
plt.ylabel('Numbers')

plt.grid(True)
plt.xticks(x_days)
plt.ylim(0,1500)

# print(plt.style.available)

plt.show()

