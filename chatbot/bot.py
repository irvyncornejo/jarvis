from typing import Tuple, List
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)

exit_conditions = (":q", "quit", "exit")

def read_train_file(name_file: str) -> List:
    content_values: List = []
    def separate_values(value):
        [ content_values.append(intent.strip()) for intent in value.split('|')]

    with open(name_file,'r') as train_file:
        content = train_file.read()
    content = content.split('\n')
    [separate_values(value) for value in content]
    return content_values

if __name__=='__main__':
    content = read_train_file('train_file.txt')
    trainer.train(content)
    while True:
        query = input("> ")
        if query in exit_conditions:
            break
        if query not in content:
            print(f"🪴 ¿En qué puedo ayudarte?")
        else:
            print(f"🪴 {chatbot.get_response(query)}")
