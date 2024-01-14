from matplotlib import pyplot as plt
from random import randint


def dynamic_round(value):
    return round(value, -(len(str(value))-1))


def daily_plot(messages_count, text_and_borders_color: str = 'white', background_color: str = '#1f262b',
               bar_color: str = 'w'):
    # setting up plot size
    fig, ax = plt.subplots(figsize=(40, 20))
    # setting ticks
    ax.set_xticks(range(1, 25))
    ax.set_yticks(range(0, dynamic_round(max(messages_count)), dynamic_round(max(messages_count)) // 10))

    # setting background color
    fig.set_facecolor(background_color)
    ax.set_facecolor(background_color)
    # creating bars
    ax.bar(list(range(1, 25)), messages_count, color=bar_color)
    # setting label's sizes, colors, paddings
    ax.set_xlabel('hours', color=text_and_borders_color, fontsize=35, labelpad=20)
    ax.set_ylabel('messages sent', color=text_and_borders_color, fontsize=35, labelpad=20)
    # setting tick size and color
    ax.tick_params(axis='x', colors=text_and_borders_color, labelsize=25)
    ax.tick_params(axis='y', colors=text_and_borders_color, labelsize=25)
    # setting border color
    ax.spines['top'].set_color(text_and_borders_color)
    ax.spines['right'].set_color(text_and_borders_color)
    ax.spines['bottom'].set_color(text_and_borders_color)
    ax.spines['left'].set_color(text_and_borders_color)
    # writing messages_quantity on the bars
    for bar, count in zip(ax.patches, messages_count):
        height = bar.get_height()
        ax.annotate(f'{count}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', color=text_and_borders_color, fontsize=25)
    return fig


def weekly_plot(messages_count, text_and_borders_color: str = 'white', background_color: str = '#1f262b',
                bar_color: str = 'w'):

    fig, ax = plt.subplots(figsize=(25, 20))

    ax.set_yticks(range(0, dynamic_round(max(messages_count)), dynamic_round(max(messages_count)) // 10))

    fig.set_facecolor(background_color)
    ax.set_facecolor(background_color)

    ax.bar(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], messages_count, color=bar_color)

    ax.set_xlabel('days', color=text_and_borders_color, fontsize=35, labelpad=20)
    ax.set_ylabel('messages sent', color=text_and_borders_color, fontsize=35, labelpad=20)

    ax.tick_params(axis='x', colors=text_and_borders_color, labelsize=25)
    ax.tick_params(axis='y', colors=text_and_borders_color, labelsize=25)

    ax.spines['top'].set_color(text_and_borders_color)
    ax.spines['right'].set_color(text_and_borders_color)
    ax.spines['bottom'].set_color(text_and_borders_color)
    ax.spines['left'].set_color(text_and_borders_color)

    for bar, count in zip(ax.patches, messages_count):
        height = bar.get_height()
        ax.annotate(f'{count}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', color=text_and_borders_color, fontsize=25)
    return fig


weekly_plot([randint(1, 135943) for i in range(7)]).savefig(f'images/weekly_img.png')
daily_plot([randint(1, 135943) for i in range(24)]).savefig(f'images/daily_img.png')