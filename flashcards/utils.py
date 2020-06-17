from .models import Word, Level, Language, Learn, UserProfile
import random

def RandomWord(request):
    userdata = UserProfile.objects.get(user=request.user.id)
    filter_level = userdata.level

    exclude_list = Learn.objects.filter(known=True).values('word') #don't show words already known
    word_list = Word.objects.filter(level__name__exact=filter_level).exclude(id__in=exclude_list) #show only words in active word group

    print(word_list.count(), "words on study list for ", filter_level)
    print(exclude_list.count(), " words excluded from list because already known")
    random_word = random.choice(word_list)

    data = {
        "word": random_word,
    }
    return data