import pandas as read_file
import matplotlib.pyplot as bar_plot

std_edu_hour_list = read_file.read_csv('student_gender_weekday_activity.csv')
std_edu_hour_list.head(20)

std_edu_hour_list.groupby(['Educational Activity','Gender']).size().unstack().plot(kind='box',stacked=True)
bar_plot.xlabel('Gender')
bar_plot.ylabel('Educational Activity Spent Hours')
bar_plt_axis.legend(fontsize = 10)
bar_plot.show()

std_edu_hour_list.groupby(['Work Activities','Gender']).size().unstack().plot(kind='box',stacked=True)
bar_plot.xlabel('Gender')
bar_plot.ylabel('Work Activities Spent Hours')
bar_plt_axis.legend(fontsize = 10)
bar_plot.show()

std_edu_hour_list.groupby(['Sleeping','Gender']).size().unstack().plot(kind='box',stacked=True)
bar_plot.xlabel('Gender')
bar_plot.ylabel('Sleeping Spent Hours')
bar_plt_axis.legend(fontsize = 10)
bar_plot.show()

std_edu_hour_list.groupby(['Sports','Gender']).size().unstack().plot(kind='box',stacked=True)
bar_plot.xlabel('Gender')
bar_plot.ylabel('Sports Spent Hours')
bar_plt_axis.legend(fontsize = 10)
bar_plot.show()