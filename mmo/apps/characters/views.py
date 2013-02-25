from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from models import Character
from forms import CharacterCreateForm


class CharacterListing(TemplateView):
    template_name = 'characters/listing.html'

    def get_context_data(self, **kwargs):
        context = super(CharacterListing, self).get_context_data(**kwargs)

        characters = Character.objects.filter(
            user=self.request.user
        )

        context['characters'] = characters

        return context


class CharacterCreate(CreateView):
    template_name = 'characters/character_create.html'
    form_class = CharacterCreateForm
    success_url = reverse_lazy('character:listing')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CharacterCreate, self).form_valid(form)


class CharacterView(TemplateView):
    template_name = "characters/character_view.html"

    def get_context_data(self, **kwargs):
        context = super(CharacterView, self).get_context_data(**kwargs)
        context['character'] = get_object_or_404(
            Character,
            pk=kwargs['id'],
        )

        if context['character'].user == self.request.user:
            context['current_user'] = True

        return context


class CharacterPlay(TemplateView):
    template_name = "characters/character_play.html"

    def get_context_data(self, **kwargs):
        context = super(CharacterPlay, self).get_context_data(**kwargs)
        context['character'] = self.character
        return context

    def dispatch(self, request, *args, **kwargs):

        # Check if this character belongs to this user.
        self.character = get_object_or_404(
            Character,
            pk=kwargs['id'],
            user=request.user
        )

        return super(CharacterPlay, self).dispatch(request, *args, **kwargs)
