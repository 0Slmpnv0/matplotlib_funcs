from matplotlib import pyplot as plt
from random import randint
from math import ceil


def round_it(number):
    if number < 10:
        return 10
    else:
        order_of_magnitude = 10 ** (len(str(number)) - 1)
        return ceil(number / order_of_magnitude) * order_of_magnitude


def top_groups_plot(groups_and_messages: dict[str: int], text_and_borders_color: str = 'white',
                    background_color: str = '#1f262b', bar_color: str = 'c'):
    messages_count = [x[1] for x in list(groups_and_messages.items())]
    groups = list(groups_and_messages.keys())

    fig, ax = plt.subplots(figsize=(30, 20))

    ax.set_xticks(range(0, round_it(max(messages_count)), round_it(max(messages_count)) // 10))
    fig.set_facecolor(background_color)
    ax.set_facecolor(background_color)

    ax.barh(groups, messages_count, color=bar_color)

    ax.set_xlabel('messages sent', color=text_and_borders_color, fontsize=35, labelpad=20)
    ax.set_ylabel('top groups', color=text_and_borders_color, fontsize=35, labelpad=20)

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
                    xytext=(3, 0),
                    textcoords="offset points",
                    ha='center', va='bottom', color=text_and_borders_color, fontsize=25)

    return fig


def weekly_plot(messages_count, text_and_borders_color: str = 'white', background_color: str = '#1f262b',
                bar_color: str = 'c'):
    fig, ax = plt.subplots(figsize=(25, 20))

    ax.set_yticks(range(0, round_it(max(messages_count)), round_it(max(messages_count)) // 10))

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


# that's the beautiful one
def daily_plot(messages_count, text_and_borders_color: str = 'white', background_color: str = '#1f262b',
               bar_color: str = 'c'):
    # setting up plot size
    fig, ax = plt.subplots(figsize=(40, 25))
    # setting ticks
    ax.set_yticks(range(1, 25))
    ax.set_xticks(range(0, round_it(max(messages_count)) + 1, round_it(max(messages_count)) // 10))

    # setting background color
    fig.set_facecolor(background_color)
    ax.set_facecolor(background_color)
    # creating bars
    ax.barh(list(range(1, 25)), messages_count, color=bar_color, align='center', height=0.75)
    # setting label's sizes, colors, paddings
    ax.set_ylabel('hours', color=text_and_borders_color, fontsize=35, labelpad=20)
    ax.set_xlabel('messages sent', color=text_and_borders_color, fontsize=35, labelpad=20)
    # setting tick size and color
    ax.tick_params(axis='y', colors=text_and_borders_color, labelsize=25)
    ax.tick_params(axis='x', colors=text_and_borders_color, labelsize=25)
    # setting border color
    ax.spines['top'].set_color(text_and_borders_color)
    ax.spines['right'].set_color(text_and_borders_color)
    ax.spines['bottom'].set_color(text_and_borders_color)
    ax.spines['left'].set_color(text_and_borders_color)
    # writing messages_quantity on the bars
    for bar, count in zip(ax.patches, messages_count):
        width = bar.get_width()
        ax.annotate(f'{count}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0),  # 3 points horizontal offset
                    textcoords="offset points",
                    ha='left', va='center', color=text_and_borders_color, fontsize=25)

    ax.set_ylim(bottom=0.36, top=24.64)
    return fig
