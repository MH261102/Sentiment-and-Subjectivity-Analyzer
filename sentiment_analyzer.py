from textblob import TextBlob
from newspaper import Article
import lxml_html_clean
import nltk

nltk.download('punkt')

def interpret_polarity(polarity):
    if polarity < -0.5:
        return "Very Negative"
    elif -0.5 <= polarity < 0:
        return "Negative"
    elif polarity == 0:
        return "Neutral"
    elif 0 < polarity <= 0.5:
        return "Positive"
    else:
        return "Very Positive"

def interpret_subjectivity(subjectivity):
    if subjectivity < 0.5:
        return "Objective"
    else:
        return "Subjective"

choice = input("Do you want to enter a URL or paste your own text? (Enter 'URL' or 'Text'): ").strip().lower()

if choice == "url":
    url = input("Paste the URL you want to know the sentimentality and subjectivity of: ").strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    text = article.text
elif choice == "text":
    text = input('Paste the text you want to know the sentimentality and subjectivity of: ').strip()
else:
    print("Invalid choice. Please enter 'URL' or 'Text'.")
    exit()

print("\nText for Analysis:")
print(text[:500])  # Printing the first 500 characters for brevity

blob = TextBlob(text)

polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

polarity_interpretation = interpret_polarity(polarity)
subjectivity_interpretation = interpret_subjectivity(subjectivity)

print("\nSentiment Analysis:")
print(f"Polarity: {polarity} ({polarity_interpretation})")
print(f"Subjectivity: {subjectivity} ({subjectivity_interpretation})")

input('Press ENTER to Exit')
