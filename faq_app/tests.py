from django.test import TestCase
from django.urls import reverse
from .models import FAQ
from googletrans import Translator

class FAQViewsTest(TestCase):

    def setUp(self):
        """Set up test data before each test."""
        self.translator = Translator()

        self.faq = FAQ.objects.create(
            question="How can I be sure that my money is safe with your platform?",
            answer="Our platform works with banks that are insured by the Deposit Insurance and Credit Guarantee Corporation (DICGC) for amounts up to ₹5 lakh. We also carefully check the financial stability of our partners."
        )

    def test_faq_list_view(self):
        """Check if the FAQ list page loads successfully."""
        response = self.client.get(reverse('faq-list'))  # Fetch the FAQ page
        self.assertEqual(response.status_code, 200)  # Ensure page loads correctly
        self.assertContains(response, "How can I be sure that my money is safe with your platform?")  # Check for the question

    def test_faq_translation(self):
        """Test if translation works for a different language (e.g., Hindi)."""
        response = self.client.get(reverse('faq-list') + "?lang=hi")  # Request translation in Hindi
        self.assertEqual(response.status_code, 200)
        translated_text = self.translator.translate("How can I be sure that my money is safe with your platform?", src='en', dest='hi').text
        self.assertContains(response, translated_text)  # Check if the translated text appears in response

    def test_add_faq_view(self):
        """Test if a new FAQ can be added successfully."""
        response = self.client.post(reverse('add-faq'), {
            'question': "What is BharatFD?",
            'answer': "BharatFD is a digital platform for Fixed Deposits."
        })
        self.assertEqual(response.status_code, 302)  # Ensure it redirects after adding
        self.assertEqual(FAQ.objects.count(), 2)  # Ensure a new FAQ is added
