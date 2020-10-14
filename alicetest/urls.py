from django.contrib import admin
from django.urls import path, include
import aliceapp.views
import alicecomment.views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', aliceapp.views.home, name="home"),
    path('q1', aliceapp.views.q1, name="q1"),
    path('review', aliceapp.views.reviewhome, name="reviewhome"),
    path('review/<int:blog_id>', aliceapp.views.reviewdetail, name="reviewdetail"),
    path('review/new', aliceapp.views.reviewnew, name="reviewnew"),
    path('review/postcreate', aliceapp.views.postcreate, name="postcreate"),
    path('review/edit', aliceapp.views.reviewedit, name="reviewedit" ),
    path('review/postupdate/<int:blog_id>', aliceapp.views.postupdate),
    path('review/postdelete/<int:blog_id>',aliceapp.views.postdelete),
    path('', include('aliceapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)