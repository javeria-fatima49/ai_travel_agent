from tools.get_flights import get_flights
from tools.suggest_hotels import suggest_hotels

class BookingAgent:
    def run(self, destination: str) -> str:
        flights = get_flights(destination)
        hotels = suggest_hotels(destination)

        response = f"\n✈️ Flights to {destination}:\n" + "\n".join(flights)
        response += f"\n\n🏨 Hotels in {destination}:\n" + "\n".join(hotels)
        return response