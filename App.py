import streamlit as st
from streamlit_calendar import calendar
from Cal import *
from datetime import datetime, timedelta, time
from options import *
import base64
from canvasTest import canvas
from eventMaker import *

st.sidebar.title("Settings")

# If I don't do this, there will be an error message.
if 'background_image' not in st.session_state:
    with open("img.jpg", "rb") as f:
        image = base64.b64encode(f.read()).decode('utf-8')
    st.session_state.background_image = f"data:image/png;base64,{image}"

# Load default or uploaded background image
def load_background_image(uploaded_file=None):
    default_image = "img.jpg"
    if uploaded_file is not None:
        img = base64.b64encode(uploaded_file.getvalue()).decode('utf-8')
        return f"data:image/png;base64,{img}"
    else:
        with open(default_image, "rb") as f:
            default_img = base64.b64encode(f.read()).decode('utf-8')
        return f"data:image/png;base64,{default_img}"

# Sidebar for menu selection
menu_option = st.sidebar.selectbox(
    "Menu Options",
    ["Google Authorization", "Upload Background Image"],
    index=0
)

if menu_option == "Google Authorization":
    # Display Google Authorization
    login()  # Function that handles Google login
elif menu_option == "Upload Background Image":
    # Upload and display background image
    uploaded_file = st.sidebar.file_uploader("", type=['png', 'jpg', 'jpeg'])
    background_image = load_background_image(uploaded_file)
    st.session_state.background_image = background_image

# Use session_state to handle the background image
page_css = f"""
    <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("{st.session_state.background_image}");
            background-size: 90%;
            background-position: bottom;
            background-repeat: no-repeat;
            background-attachment: local;
        }}

        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
        }}

        [data-testid="stToolbar"] {{
            right: 2rem;
        }}
    </style>
"""

st.markdown(page_css, unsafe_allow_html=True)

# Custom Format Function For Select Box
def format_option(option):
    if option == "dayGridMonth":
        return "🈷️ Month"
    elif option == "timeGridWeek":
        return "🗓️ Week"
    elif option == "timeGridDay":
        return "📅 Day"
    elif option == "listMonth":
        return "📈 List"
TimeSetting = "1 Minute"    
st.session_state.calendar_options = {
    "editable": "true",
    "navLinks": "true",
    "selectable": "true",
}
if TimeSetting == "1 Minute":
    st.session_state.calendar_options = {
        **st.session_state.calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "00:01",
        "slotLabelInterval": "00:01:00",
    }
elif TimeSetting == "5 Minutes":
    st.session_state.calendar_options = {
        **st.session_state.calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "00:05",
        "slotLabelInterval": "00:01:00",
    }
elif TimeSetting == "15 Minutes":
    st.session_state.calendar_options = {
        **st.session_state.calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "00:15",
        "slotLabelInterval": "00:01:00",
    }
elif TimeSetting == "30 Minutes":
    st.session_state.calendar_options = {
        **st.session_state.calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "00:30",
        "slotLabelInterval": "00:01:00",
    }
elif TimeSetting == "1 Hour":
    st.session_state.calendar_options = {
        **st.session_state.calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "01:00",
        "slotLabelInterval": "00:01:00",
    }
else:
    st.session_state.calendar_options = {
        **st.session_state.calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "01:00",
        "slotLabelInterval": "00:01:00",
    }


# making seperate tabs
viewer, maker, canvas_maker = st.tabs(["View Calendar", "Make Events", "Import Canvas Schedule"])


# Custom CSS For Calendar
with viewer:
    if st.session_state.loggedIn == True:
        selected_view = st.selectbox(
        "Select Calendar View:",
        ["dayGridMonth", "timeGridWeek", "timeGridDay", "listMonth"],
        format_func=format_option,
        index=0,
        )
        st.session_state.calendar_options["initialView"] = selected_view
        state = calendar(
        events=st.session_state.events,
        options=st.session_state.calendar_options,
        custom_css=st.session_state.calendar_css
        )
    

with maker:
    eventMaker()


with canvas_maker:
    if st.session_state.loggedIn == True:
        canvas_button = st.button(label='Sync with Canvas')
        if canvas_button:
            canvas(st.session_state.calendarID)
    else:
        st.write("Please login to create events")
        if st.button("Login with Google"):
            get_calendar_service()
            