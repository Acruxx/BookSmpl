from django.contrib import admin
from book.models import Account, Transaction, Entry, Verification

admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Entry)
admin.site.register(Verification)