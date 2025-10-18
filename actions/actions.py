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

        cuisine = tracker.get_slot("cuisine")
        price = tracker.get_slot("price")

        # Simple restaurant options
        restaurants = [
            {"name": "Skyline Bistro", "desc": "Amazing city views 🌆"},
            {"name": "Urban Grill", "desc": "Modern American cuisine"},
            {"name": "Metro Cafe", "desc": "Cozy spot for dates 💕"}
        ]

        response = f"Here are great {price} {cuisine} options:\n"
        for i, place in enumerate(restaurants, 1):
            response += f"{i}. {place['name']} - {place['desc']}\n"
        response += "\nJust say the restaurant name to book!"

        dispatcher.utter_message(text=response)
        return []

class ActionBookRestaurant(Action):
    def name(self) -> Text:
        return "action_book_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        people = tracker.get_slot("people") or "2"
        time = tracker.get_slot("time") or "7 PM"
        restaurant_choice = tracker.get_slot("restaurant_choice")

        if restaurant_choice:
            restaurant_name = restaurant_choice
        else:
            restaurant_name = "a wonderful restaurant"

        booking_id = f"GG{random.randint(1000, 9999)}"

        dispatcher.utter_message(
            text=f"🎉 Excellent choice! Your table at {restaurant_name} is confirmed for {people} people at {time}. Your booking ID is {booking_id}."
        )
        return []