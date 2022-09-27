from django.urls import path
from . import views

app_name = 'visual'  # 这句是必须的，和之后所有的URL语句有关
urlpatterns = [
    path(r'index', views.index, name='index'),
    path(r'query', views.query, name="query"),

    path(r'showdata', views.showdata, name="showdata"),
    path(r'plot', views.plot, name="plot"),
    path(r'choose_file_name', views.choose_file_name, name="choose_file_name"),
    path(r'visualization', views.visualization, name="visualization"),
    path(r'plot_change_scale', views.plot_change_scale, name="plot_change_scale"),
    path(r'plot_change', views.plot_change, name="plot_change"),
]




