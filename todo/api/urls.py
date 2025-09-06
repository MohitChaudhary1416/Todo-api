from django.urls import path
from todo.api.views import TodoGet,TodoPost,TodoUpdate,TodoDelete

urlpatterns = [
    path('todo-get',TodoGet.as_view()),
    path('todo-post',TodoPost.as_view()),
    path('todo-update/<int:todo_id>',TodoUpdate.as_view()),
    path('todo-delete/<int:todo_id>',TodoDelete.as_view())

]