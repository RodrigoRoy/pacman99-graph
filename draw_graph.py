import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Important variables
max_sample_num = 10
ranks = []
# kos = []

# Add data from command line arguments
line_args = sys.argv
if(len(line_args) != 1):
    line_args = line_args[1:] # delete Python name file
    str_line_args = ' '.join(line_args) # convert to string
    with open('data.csv','a') as csv_file:
        csv_file.write(str_line_args + '\n')

# Get info from file
with open('data.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ', quotechar='"')
    next(csv_reader) # skip headline
    for row in csv_reader:
        ranks.append(int(row[0]))
        # kos.append(int(row[1]))

# Limit the number of samples
if len(ranks) < max_sample_num:
    max_sample_num = len(ranks)
else:
    ranks = ranks[-max_sample_num:]

# Range of the sample in array form, starting from 1
xrang = [x+1 for x in range(len(ranks))]

plt.xkcd(scale=1, length=100, randomness=2)
plt.title('Ranking in last {} games'.format(len(ranks)), pad=15)
plt.axis([0, len(ranks)+1, 100, -5])
# plt.ylabel('Ranking', weight=500, size=24, labelpad=0)
# plt.xticks([x for x in range(1, len(ranks)+1, 1)])
plt.xticks([])
plt.yticks([1, 20, 40, 60, 80, 99])
plt.grid(axis='y', color='black', linewidth=1, alpha=0.2)
# plt.plot(xrang, ranks, color='black', linestyle='-', linewidth=1.0, zorder=0.0)
plt.plot(xrang, ranks, color='black', linewidth=2.0, alpha=0.5)
plt.plot(xrang, ranks, color='yellow', marker='o', markersize=15, markeredgecolor='black', markeredgewidth='1.0', linestyle='None', linewidth=0) #label='Ranking'
# plt.legend(loc='lower right')
for game,rank in zip(xrang, ranks):
    plt.text(x=game-0.15, y=rank+9, s=rank)
plt.text(x=1.3, y=80, s='Average rank: {}'.format(int(np.mean(ranks))))
plt.text(x=1.3, y=87, s='Best rank: {}'.format(np.min(ranks)))
plt.gca().add_patch(patches.Rectangle((1, 72), 4, 20, fill=False, edgecolor='black')) # color='silver'
# plt.show()

# Save image with transparency in the current directory
plt.savefig('graph.png')
