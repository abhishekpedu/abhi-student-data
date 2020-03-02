import pandas as read_file
import matplotlib.pyplot as bar_plot

std_edu_hour_list = read_file.read_csv('edu_activity_hours_day.csv')
std_edu_hour_list.head(20)
std_edu_hour_list = std_edu_hour_list.set_index('Student')

fig, bar_plt_axis = bar_plot.subplots(figsize=(16,4))
std_edu_hour_list.plot(kind='bar', ax=bar_plt_axis,width = 1.0)

bar_plot.xlabel('Students')
bar_plot.ylabel('Spent Hours')
bar_plt_axis.legend(fontsize = 10)
bar_plot.show()