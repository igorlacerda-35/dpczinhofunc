from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBuscarPreco(Action):
    def name(self):
        return "action_buscar_preco"

    def run(self, dispatcher, tracker, domain):
        produto = tracker.get_slot("produto")
        filial = tracker.get_slot("filial")

        dispatcher.utter_message(text=f"Buscando preço do produto {produto} na filial {filial}.")
        return []
