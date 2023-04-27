import nltk
import wikipedia

nltk.download('punkt')

def respond_to_question(question):
    try:
        # Tokenizamos la pregunta
        question_tokens = nltk.word_tokenize(question)

        # Obtenemos el tema de la pregunta (el segundo token)
        topic = question_tokens[1]

        # Obtenemos la página de Wikipedia del tema
        page = wikipedia.page(topic)

        # Devolvemos el primer párrafo de la página
        return page.content.split('\n')[0]

    except:
        # Si ocurre un error, devolvemos un mensaje de error
        return "Lo siento, no pude encontrar información sobre ese tema."