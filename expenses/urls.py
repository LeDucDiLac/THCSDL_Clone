from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.index,name="expenses"),
    path('add-expense',views.add_expense,name="add-expenses"),
    path('search-expenses',csrf_exempt(views.search_expense),name="search-expenses"),
    path('edit-expense/<int:id>',views.expense_edit,name="edit-expense"),
    path('delete-expense/<int:id>',views.delete_expense,name="delete-expense"),
    path('expense-category-summary',views.expense_category_summary,name="expense-category-summary"),
    path('expenses-stats',views.stats,name="expenses-stats")
]
