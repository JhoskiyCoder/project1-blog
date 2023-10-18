

from .models import Post, Category
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

 

def category_list(request):
        categories = Category.objects.all()
        return render(request, 'blog/category_list.html', {'categories': categories})

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    permission_required = ('news.add_post')
    raise_exception = True
    

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.author = self.request.user  
        fields.save()
        return super().form_valid(form)
    
    
   
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "text"]
    template_name = 'blog/post_edit.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.post_author = self.request.user
        fields.save()
        return HttpResponseRedirect(reverse('post_detail', kwargs={'pk': fields.pk}))
    
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name ='posts'
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    context_object_name = 'post'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
       

    success_url = reverse_lazy('post_list')
    

#def post_new(request):
    #if request.method == "POST":
    #    form = PostForm(request.POST)
       # if form.is_valid():
           # post = form.save(commit=False)
           # post.author = request.user
          #  post.published_date = timezone.now()
           # post.save()
          #  return redirect('post_detail', pk=post.pk)
   # else:
   #    form = PostForm()
    #return render(request, 'blog/post_edit.html', {'form': form})

#def post_list(request):
   # posts = Post.objects.filter(
       # published_date__lte=timezone.now()).order_by('published_date')
   # return render(request, 'blog/post_list.html', {'posts': posts})

#def post_detail(request, pk):
   # post = get_object_or_404(Post, pk=pk)
    #return render(request, 'blog/post_detail.html', {'post': post})
#dit(request, pk):
  #  post = get_object_or_404(Post, pk=pk)
   # if request.method == "POST":
       # form = PostForm(request.POST, instance=post)
      #  if form.is_valid():
      #      post = form.save(commit=False)
      #      post.author = request.user
      #      post.published_date = timezone.now()
       #     post.save()
      #      return redirect('post_detail', pk=post.pk)
   # else:
#def post_e
   #     form = PostForm(instance=post)
   # return render(request, 'blog/post_edit.html', {'form': form})

#def category_list(request):
   # categories = Category.objects.all()
   # posts = Post.objects.filter(categories=Category)
   # return render (request, 'blog/cat_list.html', {"categories": categories})

