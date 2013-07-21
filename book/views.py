# Create your views here.

from django.views.generic import ListView
from book.models import Account

class ListAccountView(ListView):
	model = Account