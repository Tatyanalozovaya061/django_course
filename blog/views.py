from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from blog.models import Blog
from pytils.translit import slugify


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'slug', 'is_published', 'view_count',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):  # Задание 3: выводить в список статей только те, которые имеют положительный признак публикации
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)  # В консоли нужно установить модуль pytils
            new_blog.save()
        return super().form_valid(form)

class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):    # Задание 3: при открытии отдельной статьи увеличивать счетчик просмотров;
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'slug', 'is_published', 'view_count',)

    def form_valid(self, form):
        if form.is_valid():
            blog = form.save()
            blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.object.slug])
#
#
class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')