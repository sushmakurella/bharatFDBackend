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
        # Ensure question and answer are not None
        question = faq.question if faq.question else "No question available"
        answer = faq.answer if faq.answer else "No answer available"

        if lang != 'en':  # If the selected language is not English
            try:
                translated_question = translator.translate(question, src='en', dest=lang)
                translated_answer = translator.translate(answer, src='en', dest=lang)

                # Ensure translated result is a string
                translated_question = translated_question.text if translated_question and isinstance(translated_question.text, str) else question
                translated_answer = translated_answer.text if translated_answer and isinstance(translated_answer.text, str) else answer
            except Exception as e:
                print(f"Translation error: {e}")  # Log error in server logs
                translated_question = question  # Fallback to original text
                translated_answer = answer
        else:
            translated_question = question
            translated_answer = answer

        translated_faqs.append({
            'question': translated_question,
            'answer': translated_answer,
        })

    return render(request, 'faq_list.html', {
        'faqs': translated_faqs,
        'current_language': lang,
        'languages': LANGUAGES,
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
