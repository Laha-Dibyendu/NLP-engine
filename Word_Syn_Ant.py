from bs4 import BeautifulSoup
import requests
import spacy

global nlp
nlp = spacy.load("en_core_web_lg")  # Load the spaCy language model

def synonyms(term):
    doc = nlp(term)  # Process the input term with spaCy
    print(term)
    try:
        response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))  # Send a GET request to thesaurus.com for the term
        soup = BeautifulSoup(response.text, features="html.parser")  # Create a BeautifulSoup object to parse the HTML response
        soup.find('div', {'class': 'css-ixatld e15rdun50'})  # Find a specific div element in the HTML
        extracted_text = [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})]  # Extract the text from all relevant anchor tags
        max = -1  # Initialize a variable to keep track of the maximum similarity score
        print(extracted_text)
        for text in extracted_text:
            if doc.similarity(nlp(text)) > max:  # Calculate the similarity between the input term and each synonym
                max = doc.similarity(nlp(text))  # Update the maximum similarity score
                k = text  # Store the most similar synonym
        return k + ", similarity: " + str(max)  # Return the most similar synonym and its similarity score
    except:
        return {"message": "Sorry, not able to get the synonym"}  # Return an error message if an exception occurs

# print("Synonyms: ", synonyms("Running"), "\n")

def antonyms(term):
    doc = nlp(term)  # Process the input term with spaCy
    try:
        response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))  # Send a GET request to thesaurus.com for the term
        soup = BeautifulSoup(response.text, features="html.parser")  # Create a BeautifulSoup object to parse the HTML response
        soup.find('section', {'class': 'MainContentContainer css-ln1i60 e1h3b0ep0'})  # Find a specific section element in the HTML
        extracted_text = [span.text for span in soup.findAll('a', {'class': 'css-pc0050 eh475bn0'})]  # Extract the text from all relevant anchor tags
        min = 100  # Initialize a variable to keep track of the minimum similarity score
        for text in extracted_text:
            if doc.similarity(nlp(text)) < min:  # Calculate the similarity between the input term and each antonym
                min = doc.similarity(nlp(text))  # Update the minimum similarity score
                word = text  # Store the least similar antonym
        return word + ", disimilarity: " + str(min)  # Return the least similar antonym and its similarity score
    except:
        return {"message": "Sorry, not able to get the antonym"}  # Return an error message if an exception occurs

# print("Antonyms: ", antonyms("Running"))

def meaning(term):
    doc = nlp(term)  # Process the input term with spaCy
    response = requests.get('https://www.dictionary.com/browse/{}'.format(term))  # Send a GET request to dictionary.com for the term
    soup = BeautifulSoup(response.text, features="html.parser")  # Create a BeautifulSoup object to parse the HTML response
    soup.find('div', {'class': 'css-10n3ydx e1hk9ate0'})
    text= [span.text for span in soup.findAll('span', {'class': 'one-click-content css-nnyc96 e1q3nk1v1'})] # 'css-1gyuw4i eh475bn0' for less relevant synonyms
    return text



