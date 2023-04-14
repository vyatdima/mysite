class TitleMixin:
    title = None

    def get_context_data(self, **kwards):
        context = super(TitleMixin, self).get_context_data(**kwards)
        context['title'] = self.title
        return context
