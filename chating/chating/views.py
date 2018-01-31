from django.shortcuts import render, HttpResponse
from chatterbot import ChatBot
import json

from django.views.decorators.csrf import csrf_exempt

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")


@csrf_exempt
def result(request):
    if request.method == "POST":
        question = request.POST.get("question")
        answer = chatbot.get_response(question).text
        return HttpResponse(answer)
    else:
        return render(request, "main.html")