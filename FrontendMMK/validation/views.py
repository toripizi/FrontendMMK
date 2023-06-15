from django.shortcuts import render
from .models import LogMessage
from WHParallelParser import WHParallelParser, Iterator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json 

parser = WHParallelParser()
path_to_simplewiki = "example_simplewiki.json/essa (3).ndjson"


def article_generator():
    for parsed in Iterator(path_to_simplewiki):
        yield parsed


generator = article_generator()


def generate(html):
    links = {}
    links_end = {}
    for element in html.data:
        if element["tag"] == 'a':
            links[str(element["start"])] = element
            links_end[str(element["end"])] = element

    output_html = '<span class="parsed_line">'

    for line in range(len(html.text)):
        text = html.text[line] + " "
        for i in range(len(text)):
            if str([line, i]) in links:
                output_html += f"<a href='#'>"
            if str([line, i]) in links_end:
                output_html += "</a>"
            output_html += text[i]
        output_html += '</span><br/><span class="empty_line"><i class="fa-solid fa-plus "></i></span><br/><span class="parsed_line">'
    return output_html


def index(request):
    article = next(generator)
    context = {
        'value': generate(article["html"]),
        "url": f'{article["data"]["url"]}?oldid={article["data"]["version"]["identifier"]}',
        "name": article["data"]["name"].replace(' ', '_')
    }
    return render(request, 'validation/index.html', context)


@csrf_exempt
def create_log_message(request):
    print(request.body)
    body = json.loads(request.body)
    print(body)
    LogMessage(value=body).save()
    return HttpResponse("")


def log_messages(request):
    return render(request, 'validation/log_messages.html', {"objects": [el.value for el in LogMessage.objects.all()]})
