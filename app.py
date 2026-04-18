import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="Smart Travel Planner")
st.title("Smart Travel Planner")

sidebar = st.sidebar
sidebar.header("Travel Inputs")
traveler_type = sidebar.selectbox(
    "Traveler profile",
    ["Solo", "Couple", "Family", "Friends", "Adventure"]
)
persons = sidebar.slider("Number of travelers", 1, 10, 1)
preference = sidebar.selectbox(
    "Preference",
    ["Beach", "Mountains", "City", "Adventure"]
)
budget = sidebar.slider("Budget (₹)", 1000, 200000, 20000, 1000)
days = sidebar.slider("Number of days", 1, 15, 4)
start_date = sidebar.date_input("Travel start date", date.today())

sidebar.markdown("---")
sidebar.write("Adjust the inputs and refresh to update the itinerary.")
refresh = sidebar.button("Refresh plan")
if refresh:
    st.sidebar.success("Plan updated.")

# Rule-based filtering

def filter_destinations(preference, traveler_type):
    if preference == "Beach":
        return ["Goa", "Pondicherry"]
    if preference == "Mountains":
        return ["Manali", "Shimla"]
    if preference == "City":
        return ["Delhi", "Mumbai"]
    if preference == "Adventure":
        if traveler_type == "Family":
            return ["Rishikesh", "Munnar"]
        return ["Rishikesh", "Leh"]
    return ["Goa", "Shimla"]

# Ranking logic

def rank_destinations(destinations, budget):
    if budget < 8000:
        return destinations[0]
    if budget < 25000 and len(destinations) > 1:
        return destinations[1]
    return "International Trip"

# Itinerary generation

itinerary_ideas = {
    "Goa": [
        "Morning beach walk followed by local seafood lunch.",
        "Visit Fort Aguada and relax by the seaside.",
        "Explore the local market and evening promenade.",
        "Take a backwater boat tour and unwind at a café."
    ],
    "Pondicherry": [
        "Stroll through the French Quarter and café district.",
        "Visit Auroville and learn about the community.",
        "Relax on Serenity Beach and sample local cuisine.",
        "Explore boutique shops and heritage buildings."
    ],
    "Manali": [
        "Visit Hadimba Temple and enjoy Old Manali ambiance.",
        "Take a nature walk and sample local foods by the river.",
        "Drive to Solang Valley for scenic views.",
        "Spend time at hot springs or visit nearby waterfalls."
    ],
    "Shimla": [
        "Walk on Mall Road and explore historic shops.",
        "Visit the Ridge and Christ Church.",
        "Take a short hike to Jakhoo Hill.",
        "Enjoy local snacks and discover scenic viewpoints."
    ],
    "Delhi": [
        "Tour India Gate and central Delhi landmarks.",
        "Explore Old Delhi markets and street food.",
        "Visit Red Fort and Qutub Minar.",
        "Relax in Lodhi Gardens or visit a museum."
    ],
    "Mumbai": [
        "Walk along Marine Drive and visit Gateway of India.",
        "Explore Colaba Causeway and local cafés.",
        "Visit Elephanta Caves or the historic train station.",
        "Enjoy the beach and Mumbai street food."
    ],
    "Rishikesh": [
        "Attend a morning yoga session by the Ganges.",
        "Take a river rafting excursion.",
        "Visit Lakshman Jhula and local temples.",
        "Experience the evening Ganga Aarti."
    ],
    "Leh": [
        "Acclimatize and explore Leh Market.",
        "Visit monasteries and local cultural sites.",
        "Drive to scenic mountain passes.",
        "Relax and enjoy Ladakhi cuisine and culture."
    ],
    "International Trip": [
        "Plan travel logistics and rest after arrival.",
        "Take a city tour or guided local experience.",
        "Visit a landmark and explore local markets.",
        "Enjoy a recommended dining experience."
    ]
}

def generate_itinerary(destination, days):
    activities = itinerary_ideas.get(destination, itinerary_ideas["International Trip"])
    itinerary = []
    for day in range(1, days + 1):
        activity = activities[(day - 1) % len(activities)]
        itinerary.append(f"Day {day}: {activity}")
    return itinerary

# Cost estimation

def estimate_cost(days, persons, traveler_type):
    base_rate = 1800
    multiplier = {
        "Solo": 1.0,
        "Couple": 1.05,
        "Family": 1.2,
        "Friends": 1.1,
        "Adventure": 1.15
    }
    return int(days * persons * base_rate * multiplier.get(traveler_type, 1.0))


def budget_breakdown(total_cost):
    accommodation = int(total_cost * 0.45)
    food = int(total_cost * 0.25)
    transport = int(total_cost * 0.18)
    activities = total_cost - accommodation - food - transport
    return {
        "Accommodation": accommodation,
        "Food": food,
        "Transport": transport,
        "Activities": activities
    }

# Build the plan

destinations = filter_destinations(preference, traveler_type)
best_place = rank_destinations(destinations, budget)
travel_end = start_date + timedelta(days=days - 1)
total_cost = estimate_cost(days, persons, traveler_type)
per_person_cost = int(total_cost / persons)
breakdown = budget_breakdown(total_cost)
itinerary = generate_itinerary(best_place, days)
budget_category = "Low" if budget < 8000 else "Medium" if budget < 25000 else "High"

# Main layout

st.subheader("Plan summary")
summary_cols = st.columns(3)
summary_cols[0].metric("Destination", best_place)
summary_cols[1].metric("Travel dates", f"{start_date.strftime('%b %d, %Y')} – {travel_end.strftime('%b %d, %Y')}")
summary_cols[2].metric("Travelers", f"{persons} ({traveler_type})")

st.markdown("---")

st.header("Cost overview")
cost_cols = st.columns(3)
cost_cols[0].metric("Total budget", f"₹{budget}")
cost_cols[1].metric("Estimated cost", f"₹{total_cost}")
cost_cols[2].metric("Cost per person", f"₹{per_person_cost}")

st.write(
    "Estimated cost is based on a standard model and includes accommodation, food, transport, and activities. "
    "Adjust customer preferences and budget for a tailored estimate."
)

st.subheader("Cost breakdown")
for label, value in breakdown.items():
    st.write(f"- {label}: ₹{value}")

st.markdown("---")

st.header("Itinerary")
for item in itinerary:
    st.write(item)

with st.expander("Considered destinations"):
    for d in destinations:
        st.write(f"- {d}")

# Download itinerary

def build_download_text():
    lines = [
        "Smart Travel Planner Itinerary",
        "===========================",
        f"Traveler profile: {traveler_type}",
        f"Travelers: {persons}",
        f"Destination: {best_place}",
        f"Travel dates: {start_date.strftime('%b %d, %Y')} to {travel_end.strftime('%b %d, %Y')}",
        f"Budget category: {budget_category}",
        "",
        "Itinerary:",
    ]
    lines.extend(itinerary)
    lines.append("")
    lines.append("Cost breakdown:")
    for label, value in breakdown.items():
        lines.append(f"{label}: ₹{value}")
    return "\n".join(lines)

st.download_button(
    label="Download itinerary",
    data=build_download_text(),
    file_name="travel_itinerary.txt",
    mime="text/plain"
)
