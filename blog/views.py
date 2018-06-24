from django.template import loader, Context, context
from django.shortcuts import render
from django.shortcuts import render_to_response
from keras.models import model_from_json
from keras.preprocessing.sequence import skipgrams
from keras.preprocessing.text import hashing_trick

from blog.models import Comment


def home(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render_to_response('blog/about.html')

def neroset(request):

    com = list()

    json_file = open("imdb_model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("imdb_model.h5")
    loaded_model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])


    for i in range(0, 2):
        text = Comment.text[i]

        sequence = hashing_trick(text, n=64, hash_function=None, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True,
                                 split=' ')
        scores = skipgrams(sequence, vocabulary_size=5000, window_size=32, negative_samples=1.0, shuffle=False,
                           categorical=False, sampling_table=None, seed=None)

        b = scores[1:2]
        kol = 0
        num2 = 0
        for g in b:
            num1 = g
            for c in num1:
                num2 += c
                kol += 1

        k = num2 / kol
        if k >= 0.5:
            com[i] = 'Хорошая'
        else:
            com[i] = 'Плохая'
    return render(request, 'blog/home.html', com)











