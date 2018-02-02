from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm, CommentForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Image, Comment
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.http import require_POST
from django.http import JsonResponse


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
            return redirect(new_item.get_absolute_url())
            # # return render(request, 'profile/dashboard.html', {'user_form': user_form, 'profile_form': profile_form})
            # return redirect('dashboard')
    else:
        form = ImageUploadForm()

    return render(request, 'images/upload.html', {'section': 'upload', 'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    initial_data = {
        'content_type': image.get_content_type,
        'object_id': image.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get('content_type')
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('content')
        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data)
    comments = image.comments
    return render(request, 'images/detail.html', {'section': 'images', 'image': image, 'comments': comments,
                                                  'comment_form': form})


@login_required
def home(request):
    images = Image.objects.all()
    return render(request, 'images/list.html', {'section': 'images', 'images': images})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    print(image_id)
    print("Inside Like")
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ko'})
