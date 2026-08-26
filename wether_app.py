

import streamlit as st
import requests

st.set_page_config(
    page_title="My Weather App",
    page_icon="🌦️"
)

st.title("🌦️ My Weather App")

cities_name = [
    "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Pune",
    "Jaipur", "Surat", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal",
    "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad", "Ludhiana", "Agra", "Nashik", "Faridabad",
    "Meerut", "Rajkot", "Kalyan-Dombivli", "Vasai-Virar", "Varanasi", "Srinagar", "Aurangabad",
    "Dhanbad", "Amritsar", "Navi Mumbai", "Allahabad (Prayagraj)", "Ranchi", "Howrah",
    "Coimbatore", "Jabalpur", "Gwalior", "Vijayawada", "Jodhpur", "Madurai", "Raipur",
    "Kota", "Guwahati", "Chandigarh", "Solapur", "Hubli–Dharwad", "Tiruchirappalli", "Bareilly",
    "Moradabad", "Mysuru", "Tiruppur", "Gurugram", "Aligarh", "Jalandhar", "Bhubaneswar", "Salem",
    "Warangal", "Guntur", "Bhiwandi", "Saharanpur", "Gorakhpur", "Bikaner", "Amravati",
    "Noida", "Jamshedpur", "Bhilai", "Cuttack", "Firozabad", "Kochi", "Nellore", "Bhavnagar",
    "Dehradun", "Durgapur", "Asansol", "Rourkela", "Nanded", "Kolhapur", "Ajmer", "Akola",
    "Gandhinagar", "Udaipur", "Shillong", "Imphal", "Aizawl", "Itanagar", "Panaji", "Gangtok",
    "Port Blair", "Kavaratti", "Silvassa", "Daman", "Dispur", "Agartala", "Patiala", "Shimla",
    "Hamirpur", "Bilaspur", "Rewa", "Sagar", "Haridwar", "Roorkee", "Haldwani", "Mathura",
    "Muzaffarpur", "Begusarai", "Darbhanga", "Siliguri", "Tezpur", "Tinsukia", "Dimapur", "Kohima"
]

# API key

API_key = st.secrets["OPENWEATHER_API_KEY"]

choice = st.selectbox("Choose your city", cities_name)

if choice:

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={choice}&appid={API_key}"
    )

    try:
        response = requests.get(url, timeout=10)


        st.write("Status:", response.status_code)
        

        if response.status_code == 200:

            weather_info = response.json()

            # Extract information
            temperature = weather_info["main"]["temp"] - 273.15
            feels_like = weather_info["main"]["feels_like"] - 273.15
            temp_min = weather_info["main"]["temp_min"] - 273.15
            temp_max = weather_info["main"]["temp_max"] - 273.15

            humidity = weather_info["main"]["humidity"]
            pressure = weather_info["main"]["pressure"]

            wind_speed = weather_info["wind"]["speed"]

            weather_main = weather_info["weather"][0]["main"]
            description = weather_info["weather"][0]["description"]

            # City heading
            st.subheader(f"🌆 Weather in {choice}")

            st.write(f"### {description.title()}")

            # First row
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "🌡️ Temperature",
                    f"{temperature:.1f} °C"
                )

            with col2:
                st.metric(
                    "🤗 Feels Like",
                    f"{feels_like:.1f} °C"
                )

            with col3:
                st.metric(
                    "💧 Humidity",
                    f"{humidity}%"
                )

            # Second row
            col4, col5, col6 = st.columns(3)

            with col4:
                st.metric(
                    "💨 Wind Speed",
                    f"{wind_speed} m/s"
                )

            with col5:
                st.metric(
                    "🔽 Minimum",
                    f"{temp_min:.1f} °C"
                )

            with col6:
                st.metric(
                    "🔼 Maximum",
                    f"{temp_max:.1f} °C"
                )

            # Extra information
            st.divider()

            st.write(f"☁️ **Weather:** {weather_main}")
            st.write(f"📝 **Description:** {description.title()}")
            st.write(f"🌡️ **Pressure:** {pressure} hPa")

        else:
            st.error(
                f"❌ Could not get weather data. "
                f"Status code: {response.status_code}"
            )

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Connection error: {e}")