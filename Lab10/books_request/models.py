from django.db import models
from django.contrib.auth.models import User
from database.models import Articles
from django.utils.timezone import now
from datetime import datetime


far_past_date = datetime(1000, 1, 1)
class Books_request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_books')
    book = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='book_owners')
    date_added = models.DateTimeField(default=now)
    date_checked_by_admin = models.DateTimeField(default=far_past_date)
    date_withdrawal = models.DateTimeField(default=far_past_date)
    status = models.CharField('status', max_length=50, default='Processing')

    def __str__(self):
        return f"user_id: {self.user.id} - book_id: {self.book.id}"

    class Meta:
        verbose_name = 'Books_request'
        verbose_name_plural = 'Books_requests'
        unique_together = ('user', 'book')  # Это гарантирует, что пара пользователь-книга будет уникальной

