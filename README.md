# Smart Travel Planner

A professional travel planning application built with Streamlit that helps users create personalized trip itineraries based on their preferences, budget, and group size.

## Features

- **Traveler Profile Selection**: Choose from Solo, Couple, Family, Friends, or Adventure profiles
- **Destination Recommendations**: Get tailored destination suggestions based on preferences (Beach, Mountains, City, Adventure)
- **Budget Planning**: Input your budget and get cost estimates with detailed breakdowns
- **Itinerary Generation**: Receive day-by-day activity suggestions for your trip
- **Date Planning**: Select start dates and get automatic end date calculations
- **Cost Breakdown**: See estimates for accommodation, food, transport, and activities
- **Downloadable Itineraries**: Export your trip plan as a text file

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup
1. Clone or download this repository
2. Navigate to the project directory
3. Install required packages:
   ```bash
   pip install streamlit
   Usage
Run the application:streamlit run app.py
Open your browser to the provided local URL (usually http://localhost:8501)

Use the sidebar to input your travel preferences:

Select traveler profile
Choose number of travelers
Pick your destination preference
Set your budget and trip duration
Select start date
View your personalized trip plan in the main area

Download your itinerary using the download button

How It Works
The app uses rule-based filtering to recommend destinations based on your preferences and budget. It then generates a detailed itinerary with daily activities tailored to your selected destination. Cost estimates are calculated based on traveler type and group size.

Supported Destinations
Beach: Goa, Pondicherry
Mountains: Manali, Shimla
City: Delhi, Mumbai
Adventure: Rishikesh, Leh, Munnar
Cost Estimation
The app provides realistic cost breakdowns including:

Accommodation (45% of total)
Food (25% of total)
Transport (18% of total)
Activities (12% of total)
Costs are adjusted based on traveler profile for more accurate estimates.

Contributing
Feel free to submit issues and enhancement requests!

License
This project is open source and available under the MIT License.

