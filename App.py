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
    label="Menu Options",
    options=["Google Authorization", "Upload Background Image"],
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
    
    
st.session_state.TimeSetting = "5 Minute"    
st.session_state.calendar_options = {
    "editable": "true",
    "navLinks": "true",
    "selectable": "true",
}
if st.session_state.TimeSetting == "1 Minute":
    st.session_state.calendar_options = {
        **st.session_state.calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "00:01",
        "slotLabelInterval": "00:01:00",
    }
elif st.session_state.TimeSetting == "5 Minutes":
    st.session_state.calendar_options = {
        **st.session_state.calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "00:05",
        "slotLabelInterval": "00:01:00",
    }
elif st.session_state.TimeSetting == "15 Minutes":
    st.session_state.calendar_options = {
        **st.session_state.calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "00:15",
        "slotLabelInterval": "00:01:00",
    }
elif st.session_state.TimeSetting == "30 Minutes":
    st.session_state.calendar_options = {
        **st.session_state.calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "00:30",
        "slotLabelInterval": "00:01:00",
    }
elif st.session_state.TimeSetting == "1 Hour":
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

st.session_state.calendar_css = """
/* Custom Styles For Buttons */
.fc-today-button {
    width: 85px;
    height: 40px;
    border-radius: 10px;
    text-transform: capitalize;
    border: none;
    background: linear-gradient(0deg, rgb(255, 27, 0) 0%, rgb(251, 75, 2) 100%);
    cursor: pointer;
    transition: all 0.3s ease 0s;
    position: relative;
    box-shadow: rgba(255, 255, 255, 0.5) 2px 2px 2px 0px inset, rgba(0, 0, 0, 0.1) 7px 7px 20px 0px, rgba(0, 0, 0, 0.1) 4px 4px 5px 0px;
    outline: none;
}

.fc-today-button:hover {
    color: #ffffff;
    background: linear-gradient(0deg, rgb(255, 27, 0) 100%, rgb(251, 75, 2) 0%);
    border: none;
    box-shadow: inset 2px 2px 2px 0px rgba(255,255,255,.5), 7px 7px 20px 0px rgba(0,0,0,.1), 4px 4px 5px 0px rgba(0,0,0,.1);
}

.fc-today-button:focus {
    box-shadow: rgba(255, 255, 255, 0.5) 2px 2px 2px 0px inset, rgba(0, 0, 0, 0.1) 7px 7px 20px 0px, rgba(0, 0, 0, 0.1) 4px 4px 5px 0px !important;
}

.fc-button-group {
    gap: 12px;
}

.fc-prev-button, .fc-next-button {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border: 1px solid #ccc;
    border-radius: 50% !important;
    background: #ccc;
    text-decoration: none;
}

.fc-prev-button:hover, .fc-next-button:hover {
    background: #ccc;
    border-color: #ccc;
    animation: shake .35s linear;
}

@keyframes shake {
    0% {
        transform: rotate(0deg);
    }
    25% {
        transform: rotate(15deg);
    }
    50% {
        transform: rotate(0deg);
    }
    75% {
        transform: rotate(-15deg);
    }
    100% {
        transform: rotate(0deg);
    }
}


/* Custom Styles For Calendar Container */
.fc {
    /* Main Styles */
    color: #262730;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background-color: rgb(255, 255, 225);

    /* Table Header Padding */
    .fc-col-header-cell {
        padding: 2px 20px;
    }


    /* Today's Date Color */

    .fc-day-today {
        background-color: #fff9c8;
    }

    .fc-highlight {
        background: #fff6af;
    }


    /* Toolbar Styles */

    .fc-toolbar.fc-header-toolbar {
        margin-bottom: 0em !important;
    }

    .fc-toolbar-title {
        background: #262730;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .fc-header-toolbar {
        padding: 10px;
    }

    .fc-toolbar-title {
        color: #262730;
        font-weight: bold;
    }


    /* Table Body Padding & Styles */
    .fc-timegrid-slot {
        height: 2em;
    }

    .fc-timegrid-axis-cushion {
        text-transform: capitalize;
    }

    .fc-timegrid-axis.fc-scrollgrid-shrink {
    }

    .fc-timegrid-slot-label-cushion {
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .fc-timegrid-slot-label.fc-scrollgrid-shrink {
    }


    /* Scrollbar Styles */
    .fc-scroller-harness > .fc-scroller {
        overflow: auto !important;
    }

    .fc-scroller-liquid-absolute::-webkit-scrollbar-track
    {
        background-color: #fff;
        border-radius: 10px;
    }
}
"""

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
        custom_css=st.session_state.calendar_css,
        callbacks=["eventChange"],
        )
        # print(state)
        
    

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
            