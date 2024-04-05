from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class PostApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('WelfarePost', on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} applied for {self.post.post_title}"

    def get_absolute_url(self):
        return reverse('post_application_detail', args=[str(self.id)])


# ==============================

from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from .models import WelfarePost, CategoryEducation, CategoryHealthcare, PostApplication

def MyPostApplyView(request, pk):
    obj3 = get_object_or_404(WelfarePost, id=pk)
    user = request.user

    if request.method == 'POST':
        try:
            application = PostApplication.objects.create(
                user=user,
                post=obj3,
            )
            return redirect('mypost_all')
        except IntegrityError:
            # Show error message and redirect to an error page
            messages.error(request, 'You have already applied for this post.')
            return redirect('error_page')

    context = {
        'data': obj3,
    }
    html = 'UserApp/MyPost-Apply.html'
    return render(request, html, context)
