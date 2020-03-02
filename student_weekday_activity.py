import pandas as read_file
import matplotlib.pyplot as bar_plot 

bar_plot.style.use("fivethirtyeight")
std_activity_list = read_file.read_csv("student_weekday_activity.csv")
std_activity_list.head(20)

std_activity_list['Educational Activity'].value_counts(sort=True).plot(kind='bar')

bar_plot.title('Student Educational Activity')
bar_plot.xlabel('Educational Activity in hours')
bar_plot.ylabel('Student Count')
bar_plot.show()

std_activity_list['Eating & Drinking'].value_counts(sort=True).plot(kind='bar')

bar_plot.title('Student Eating & Drinking')
bar_plot.xlabel('Eating & Drinking in hours')
bar_plot.ylabel('Student Count')
bar_plot.show()

std_activity_list['Ready to go to College'].value_counts(sort=True).plot(kind='bar')

bar_plot.title('Student Ready to go to College')
bar_plot.xlabel('Ready to go to College in hours')
bar_plot.ylabel('Student Count')
bar_plot.show()

std_activity_list['Travelling'].value_counts(sort=True).plot(kind='bar')

bar_plot.title('Student Travelling')
bar_plot.xlabel('Travelling in hours')
bar_plot.ylabel('Student Count')
bar_plot.show()

std_activity_list['Sleeping'].value_counts(sort=True).plot(kind='bar')

bar_plot.title('Student Sleeping')
bar_plot.xlabel('Sleeping in hours')
bar_plot.ylabel('Student Count')
bar_plot.show()

std_activity_list['Sports'].value_counts(sort=True).plot(kind='bar')

bar_plot.title('Student Sports')
bar_plot.xlabel('Sports in hours')
bar_plot.ylabel('Student Count')
bar_plot.show()

std_activity_list['Work Activities'].value_counts(sort=True).plot(kind='bar')

bar_plot.title('Student Work Activities')
bar_plot.xlabel('Work Activities in hours')
bar_plot.ylabel('Student Count')
bar_plot.show()

std_activity_list['Other'].value_counts(sort=True).plot(kind='bar')

bar_plot.title('Student Other Works')
bar_plot.xlabel('Other Work in hours')
bar_plot.ylabel('Student Count')
bar_plot.show()