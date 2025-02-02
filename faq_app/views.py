from django.shortcuts import render, redirect
from .models import FAQ
from .forms import FAQForm
from googletrans import Translator, LANGUAGES

translator = Translator()

def faq_list(request):
    # Get the selected language from query parameters, default to English ('en')
    lang = request.GET.get('lang', 'en')

    # Retrieve all FAQs
    faqs = FAQ.objects.all()

    # Translate the FAQs based on the selected language
    translated_faqs = []
    for faq in faqs:
        if lang != 'en':  # If the selected language is not English
            translated_question = translator.translate(faq.question, src='en', dest=lang).text
            translated_answer = translator.translate(faq.answer, src='en', dest=lang).text
        else:
            translated_question = faq.question
            translated_answer = faq.answer

        translated_faqs.append({
            'question': translated_question,
            'answer': translated_answer,
        })

    return render(request, 'faq_list.html', {
        'faqs': translated_faqs,
        'current_language': lang,
        'languages': LANGUAGES,  # Pass all Google Translate supported languages
    })
def add_faq(request):
    """Add a new FAQ"""
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq-list')  # Redirect to FAQ list
    else:
        form = FAQForm()
    
    return render(request, 'add_faq.html', {'form': form})
