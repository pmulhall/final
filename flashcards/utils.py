from .models import Word, Level, Language, Learn, UserProfile
import random

def RandomWord(request):
    userdata = UserProfile.objects.get(user=request.user.id)
    filter_level = userdata.level
    word_list = Word.objects.filter(level__name__exact=filter_level)
    random_word = random.choice(word_list)

    data = {
        "word": random_word,
    }
    return data