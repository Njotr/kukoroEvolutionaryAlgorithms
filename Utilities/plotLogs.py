import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme()


def plot(logbook, title):
    stats = {header: [] for header in logbook.header}
    for dic in logbook:
        for stat in stats.keys():
            stats[stat].append(dic[stat])
    df = pd.DataFrame.from_dict(stats)
    ax = sns.lineplot(data=df.drop(['gen', 'nevals', 'std'], axis=1), )
    ax.set(xlabel='Generation', ylabel='Fitness', title=title)
    plt.show()
