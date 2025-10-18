from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
import random

class ActionSuggestRestaurants(Action):
    def name(self) -> Text:
        return "action_suggest_restaurants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # In our guided flow, we use utter_suggest_restaurants response
        # This action is kept for consistency but doesn't need complex logic
        return []

class ActionBookRestaurant(Action):
    def name(self) -> Text:
        return "action_book_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        people = tracker.get_slot("people") or "2"
        time = tracker.get_slot("time") or "7:00 PM"
        restaurant_choice = tracker.get_slot("restaurant_choice")
        cuisine = tracker.get_slot("cuisine")
        dietary = tracker.get_slot("dietary") or "none"

        # Simple booking confirmation
        booking_id = f"RS{random.randint(1000, 9999)}"

        dispatcher.utter_message(
            text=f"✅ Booking confirmed!\n\n• Restaurant: {restaurant_choice}\n• Time: {time}\n• People: {people}\n• Dietary: {dietary}\n• Booking ID: {booking_id}\n\nEnjoy your meal! 🎉"
        )

        return []