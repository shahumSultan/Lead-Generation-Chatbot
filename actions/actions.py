from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
from actions.helper_functions import bot_response_simple, bot_response_high


class ActionCaptureLead(Action):
    def name(self) -> Text:
        return "action_capture_lead"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("---- CAPTURE LEAD ACTION ----")
        slots = tracker.current_slot_values()
        intent = tracker.get_intent_of_latest_message()
        lead_type = tracker.get_slot("lead_type") or []

        print(f"SLOTS : {slots}")
        print(f"INTENT : {intent}")

        if (intent == "inquire_simple"):
            lead_type.append('low')
            message = bot_response_simple(slots['category'])
        elif (intent == "inquire_high_intent"):
            lead_type.append('high')
            message = bot_response_high(slots['category'])
        else:
            message = "Happy to answer all your questions."
        dispatcher.utter_message(message)

        return [SlotSet("lead_type", lead_type)]


class ActionUserDetails(Action):
    def name(self) -> Text:
        return "action_user_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("---- USER DETAILS ACTION ----")
        slots = tracker.current_slot_values()
        intent = tracker.get_intent_of_latest_message()
        lead_type = tracker.get_slot('lead_type')

        if (lead_type[0] == 'low'):
            message = f"{slots['name']}, our agents are going to connect with via email: {slots['email']} and phone number: {slots['phone_number']}. Thank you!!"
        elif (lead_type[0] == 'high'):
            message = f"{slots['name']}, we are happy to provide all the answers you're looking for. Also, please feel free to book an appointment using this link:\nhttps://calendly.com/sultanshahum3"
        else:
            message = "For futher queries, please book an appointment with our support staff by using the link: https://calendly.com/sultanshahum3"
        
        dispatcher.utter_message(message)

        return [AllSlotsReset()]
