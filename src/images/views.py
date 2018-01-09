from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from django.contrib.contenttypes.models import ContentType
# Create your views here.


@login_required
def image_upload(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            # assign current user to the item
            new_item.user = request.user
            new_item.save()
            # create_action(request.user, 'uploaded image', new_item)
            print("inside image post")
            messages.success(request, 'Image uploaded successfully')
            # redirect to new created item detail view
            # return redirect(new_item.get_absolute_url())
            # return render(request, 'profile/dashboard.html', {'user_form': user_form, 'profile_form': profile_form})
            return redirect('dashboard')
    else:
        form = ImageUploadForm()

    return render(request, 'images/upload.html', {'section': 'upload', 'form': form})


# def image_detail(request, id, slug):
#     image = get_object_or_404(Image, id=id, slug=slug)
#     initial_data = {
#         'content_type': image.get_content_type,
#         'object_id': image.id
#     }
#     form = CommentForm(request.POST or None, initial=initial_data)
#     if form.is_valid():
#         c_type = form.cleaned_data.get('content_type')
#         content_type = ContentType.objects.get(model=c_type)
#         obj_id = form.cleaned_data.get('object_id')
#         content_data = form.cleaned_data.get('content')
#         new_comment, created = Comment.objects.get_or_create(
#             user=request.user,
#             content_type=content_type,
#             object_id=obj_id,
#             content=content_data)
#     comments = image.comments
#     return render(request, 'images/detail.html', {'section': 'images', 'image': image, 'comments': comments,
#                                                   'comment_form': form})



