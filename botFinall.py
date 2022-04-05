from chatterbot import ChatBot
from chatterbot.response_selection import get_most_frequent_response
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    "My ChatterBot",
    output_adapter="chatterbot.output.TerminalAdapter",
    output_format="text",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "response_selection_method": get_most_frequent_response,
            "statement_comparison_function": LevenshteinDistance,
            'default_response': 'Lo siento no puedo entenderte.',
            'maximum_similarity_threshold': 0.90
        },
    ],
    read_only=True,
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
)
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.spanish')
trainer.train("./neuralnetworks_ES.yml")

print("Hola soy Neural, un bot creado para responder tus dudas sobre las redes neuronales y lo que conlleva")
print("¿Cómo te llamas?")
nombre = input()
print("Mucho gusto {} :) ¿Cúal es tu pregunta sobre las redes neuronales?".format(nombre))
despedidas = ["adiós", "bye", "hasta luego", "nos vemos", "chao"]

while True:
    request=input('{} :'.format(nombre))
    if request.lower() in despedidas :
        print('Bot: Adios espero haberte ayudado')
        break
    else:
        response=bot.get_response(request)
        newResponse = str(response).replace('.', '.\n')
        print('Bot:', newResponse)