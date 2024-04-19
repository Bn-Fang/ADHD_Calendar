import streamlit as st
from streamlit_calendar import calendar
from Cal import *
from datetime import datetime, timedelta, time
import base64
import plotly.express as px

st.sidebar.title("Google Authentication")
login()

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
viewer, maker = st.tabs(["View Calendar", "Make Events"])

with maker:
    if st.session_state.loggedIn == True:
        st.session_state.description = st.selectbox(
        "Describe the event",
        options,
        index=0,
        placeholder="Eating",
        )
        print (st.session_state.description, Presets[st.session_state.description])
        date, time= st.columns(2)
        submit_button = st.button(label='Submit')
        customSettings = st.empty()
        
        
        
        
        
        with date:
            startDate = st.date_input("Select Date", key="startDate", value=Presets[st.session_state.description][0])
            endDate = st.date_input("Select endDate", key="endDate", value=Presets[st.session_state.description][1] )
        with time:
            startTime = st.time_input("Select Time", key="startTime", value=Presets[st.session_state.description][2], step=timedelta(minutes=5))
            endTime = st.time_input("Select endTime" , key="endTime", value= Presets[st.session_state.description][3], step=timedelta(minutes=5))
        startDate = datetime.combine(startDate, startTime)
        start = startDate.isoformat()
        endDate = datetime.combine(endDate, endTime)
        end = endDate.isoformat()

        if submit_button:
            print(st.session_state.description, start, end)
            create_event(st.session_state.calendarID,st.session_state.description, start, end)    
            st.write("Event Created")
    else:
        st.write("Please login to create events")
        if st.button("Login with Google"):
            get_calendar_service()

# Custom CSS For Calendar
calendar_css = """
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
    border-top-left-radius: 10px; /* 10px radius on the top left corner */
    border-top-right-radius: 10px; /* 10px radius on the top right corner */
    border-bottom-left-radius: 0; /* No radius on the bottom left corner */
    border-bottom-right-radius: 0; /* No radius on the bottom right corner */
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
    .fc-header-toolbar {
        border-radius: 10px;
        background-color: rgb(255, 255, 225) !important;
    }

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
        background-color: #f0f0f0;
        border-radius: 10px;
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

with viewer:
    if st.session_state.loggedIn == True:
        selected_view = st.selectbox(
        "Select Calendar View:",
        ["dayGridMonth", "timeGridWeek", "timeGridDay", "listMonth"],
        format_func=format_option,
        index=1,
        )
        st.session_state.calendar_options["initialView"] = selected_view
        state = calendar(
        events=st.session_state.events,
        options=st.session_state.calendar_options,
        custom_css=calendar_css,
        )
    
    # Adding Different Calendar Views
    
    # Add Custom Options



df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("img.jpg")

# Custom CSS For Page
page_css = f"""
    <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("data:image/png;base64,{img}");
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

# Render Custom CSS
st.markdown(page_css, unsafe_allow_html=True)
