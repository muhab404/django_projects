from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.
def boards_list(request):
    boards=Board.objects.all()
    data = {'Results':list(boards.values("pk","name","description"))}

    return JsonResponse(data)

def board_topics(request,board_id):
    
    board=get_object_or_404(Board,pk=board_id)
    data = {"Results":{
        "name" : board.name,
        "description": board.description

    }}
    
    return JsonResponse(data)


# @login_required
# def new_topic(request,board_id):
#     board = get_object_or_404(Board,pk=board_id)
#     #user = User.objects.first()
#     if request.method == "POST":
#         form =NewTopicForm(request.POST)
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = board
#             topic.created_by = request.user
#             topic.save()

#             post = Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 created_by = request.user,
#                 topic=topic

#             )
#             '''if request.method == 'POST':
#                 #code if used html forms not django forms 
#                 subject = request.POST['subject']
#                 message = request.POST['message']
#                 user = User.objects.first()

#                 topic = Topic.objects.create(
#                     subject=subject,
#                     board=board,
#                     created_by=user
#                 )

#                 post = Post.objects.create(
#                     message=message,
#                     topic=topic,
#                     created_by=user
#                 )'''
#             return redirect('board_topics',board_id=board.pk)
#     else:
#         form = NewTopicForm()

#     return render(request,'new_topic.html',{'board':board,'form':form})

# def topic_posts(request,board_id,topic_id):
#     topic= get_object_or_404(Topic,board__pk=board_id, pk=topic_id)
    
#     session_key = 'view_topic_{}'.format(topic.pk)
#     if not request.session.get(session_key,False):
#         topic.views +=1
#         topic.save()
#         request.session[session_key] = True

#     return render(request,'topic_posts.html',{"topic":topic})

# @login_required
# def reply_topics(request,board_id,topic_id):
#     topic= get_object_or_404(Topic,board__pk=board_id, pk=topic_id)

#     if request.method == "POST":
#         form =PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.topic = topic
#             post.created_by = request.user
#             post.save()

#             topic.updated_by = request.user
#             topic.updated_dt = timezone.now()
#             topic.save()

#             return redirect('topic_posts',board_id=board_id,topic_id=topic.id)
#     else:
#         form = PostForm()

#     return render(request,'reply_topics.html',{"topic":topic , 'form':form})    

# @method_decorator(login_required, name='dispatch')
# class PostUpdateView(UpdateView):
#     model=Post
#     fields = ('message',)
#     template_name = 'edit_post.html'
#     pk_url_kwarg = 'post_id'
#     context_object_name = 'post'

#     def form_valid(self, form):
#         post = form.save(commit = False)
#         post.updated_by= self.request.user
#         post.updated_dt= timezone.now()
#         post.save()
#         return redirect('topic_posts',board_id=post.topic.board.pk, topic_id=post.topic.pk)

   