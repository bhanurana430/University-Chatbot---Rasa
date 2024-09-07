# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests,json


class ActionStudyOptions(Action):

    def name(self) -> Text:
        return "action_study_options"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        request = json.loads(
         requests.get("http://127.0.0.1:5000/fields").text
        )
        print(request)
        x=''
        for i in request:
              x= x+str(i['id'])+" "+ i['name']+"\n"
        if x:
            dispatcher.utter_message(x)
        else:
            dispatcher.utter_message(text="I am unable to detect any field.")
        return []



class ActionBegin(Action):

    def name(self) -> Text:
        return "action_begin"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            dispatcher.utter_message(text="The winter semester begins on 1 October and ends on 14 March.\n          The summer semester begins on 15 March and ends on 30 September.")

            return []
    
