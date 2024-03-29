import streamlit as st
import pandas as pd
import numpy as np
from streamlit_calendar import calendar

import time



# Sidebar settings
st.sidebar.title("Settings")
st.sidebar.write("---")

TimeSetting = st.sidebar.radio(
    "How do you want to subdivide your time?",
    ["1 Minute", "5 Minutes" , "15 Minutes", "30 Minutes", "1 Hour"],
    index=None,
)
st.sidebar.write(":", TimeSetting)
#  end of sidebar settings

st.title('Time Table')

# st.sidebar.time_input("Meeting time")

day1, day2, day3, day4, day5, day6, day7 = st.columns(7)


#     elif mode == "timegrid":
        # calendar_options = {
        #     **calendar_options,
        #     "initialView": "timeGridWeek",
        #     "slotDuration": "00:01",
        #     "slotLabelInterval": "00:01:00",
        # }
        


calendar_options = {
    "editable": "true",
    "navLinks": "true",
    "selectable": "true",
}

if (TimeSetting == "1 Minute"):
    calendar_options = {
        **calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "00:01",
        "slotLabelInterval": "00:01:00",
    }
elif (TimeSetting == "5 Minutes"):
    calendar_options = {
        **calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "00:05",
        "slotLabelInterval": "00:01:00",
    }
elif (TimeSetting == "15 Minutes"):
    calendar_options = {
    **calendar_options,
    "initialView": "timeGridWeek",
    "slotDuration": "00:15",
    "slotLabelInterval": "00:01:00",
}
elif (TimeSetting == "30 Minutes"):
    calendar_options = {
        **calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "00:30",
        "slotLabelInterval": "00:01:00",
    }
elif (TimeSetting == "1 Hour"):
    calendar_options = {
        **calendar_options,
        "initialView": "timeGridWeek",
        "slotDuration": "01:00",
        "slotLabelInterval": "00:01:00",
    }
else:
    calendar_options = {
    **calendar_options,
    "initialView": "timeGridWeek",
    "slotDuration": "00:15",
    "slotLabelInterval": "00:01:00",
}   
state = calendar(
    options=calendar_options,
    custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
    """,
)






