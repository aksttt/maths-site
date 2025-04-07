from django.shortcuts import render, redirect
from . import terms_work


def index(request):
    return render(request, "index.html")


def terms_list(request):
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", {"terms": terms})


def add_term(request):
    if request.method == "POST":
        new_term = request.POST.get("new_term", "").strip()
        new_translation = request.POST.get("new_translation", "").strip()

        error = None
        if not new_term:
            error = "Введите слово"
        elif not new_translation:
            error = "Введите перевод"

        if not error:
            terms_work.write_term(new_term, new_translation)
            return redirect('terms-list')
        return render(request, "term_add.html", {"error": error})
    return render(request, "term_add.html")


def search_term(request):
    if request.method == "POST":
        search_query = request.POST.get("search", "").strip()
        results = terms_work.search_terms(search_query)
        return render(request, "term_list.html", {"terms": results})
    # GET-запрос: показать форму поиска
    return render(request, "search_term.html")  # Используем новый шаблон