import streamlit as st
from streamlit_calendar import calendar
from auth import *
from Cal import get_calendar_service
from datetime import datetime, timedelta


# making seperate tabs
viewer, maker = st.tabs(["View Calendar", "Make Events"])


# Start Sidebar Settings
st.sidebar.title("Settings")
st.sidebar.write("---")

TimeSetting = st.sidebar.radio(
    "How do you want to subdivide your time?",
    ["1 Minute", "5 Minutes", "15 Minutes", "30 Minutes", "1 Hour"],
    index=None,
)
st.sidebar.write("You selected:", TimeSetting)
# End Sidebar Settings




def create_event(eventDiscription, start, end ):
    # date = datetime.now().date()
    # today = datetime(date.year, date.month, date.day, 10) + timedelta(days=0)
    # start = today.isoformat()
    # end = (today + timedelta(hours=1)).isoformat()
    service = get_calendar_service()
    event_result = service.events().insert(calendarId='primary',
                                           body={
                                               "summary": 'Automated Event '+ eventDiscription,
                                               "description": eventDiscription,
                                               "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
                                               "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
                                           }
                                           ).execute()

    st.write("Calendar Automation has created an event")
    st.write("Id: ", event_result['id'])
    st.write("Summary: ", event_result['summary'])
    st.write("Starts At: ", event_result['start']['dateTime'])
    st.write("Ends At: ", event_result['end']['dateTime'])
   
    
with maker:
    st.title("Streamlit Oauth Login")
    loggedIn = False
    if st.button("Login with Google"):
        get_calendar_service()

    if os.path.exists('token.pickle'):
        st.write("You're logged in as []")
        loggedIn = True
    else:
        st.write("You're not logged in")
        loggedIn = False
    
    
    if loggedIn == True:
        with st.form(key='my_form'):
            description = st.text_input("Describe the event: ")
            date, time= st.columns(2)
            submit_button = st.form_submit_button(label='Submit')
            
            with date:
                startDate = st.date_input("Select Date", key=10)
                endDate = st.date_input("Select endDate")
            with time:
                startTime = st.time_input("Select Time", key=11)
                endTime = st.time_input("Select endTime")
            startDate = datetime.combine(startDate, startTime)
            start = startDate.isoformat()
            endDate = datetime.combine(endDate, endTime)
            end = endDate.isoformat()
            
            
            
            if submit_button:
                print(description, start, end)
                create_event(description, start, end)    
                st.write("Event Created")
        
 

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
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background-color: #FEF5F3;

    /* Table Header Padding */
    .fc-col-header-cell {
        padding: 2px 20px;
    }


    /* Today's Date Color */
    .fc-col-header-cell.fc-day-today {
        color: #fff;
        background-color: #FEECD2;
    }

    .fc-day-today {
        background-color: #FEECD2;
    }

    .fc-highlight {
        background: #FDDBA9;
    }


    /* Toolbar Styles */
    .fc-header-toolbar {
        background-color: #FEF5F3 !important;
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



# Custom CSS For Page
page_css = """
.st-c3 > .st-co {
    cursor: pointer;
}
"""


with viewer:
    st.title("Calandar Viewer")
    calendar_options = {
        "editable": "true",
        "navLinks": "true",
        "selectable": "true",
    }
    if TimeSetting == "1 Minute":
        calendar_options = {
            **calendar_options,
            "initialView": "timeGridWeek",
            "slotDuration": "00:01",
            "slotLabelInterval": "00:01:00",
        }
    elif TimeSetting == "5 Minutes":
        calendar_options = {
            **calendar_options,
            "initialView": "timeGridWeek",
            "slotDuration": "00:05",
            "slotLabelInterval": "00:01:00",
        }
    elif TimeSetting == "15 Minutes":
        calendar_options = {
            **calendar_options,
            "initialView": "timeGridWeek",
            "slotDuration": "00:15",
            "slotLabelInterval": "00:01:00",
        }
    elif TimeSetting == "30 Minutes":
        calendar_options = {
            **calendar_options,
            "initialView": "timeGridWeek",
            "slotDuration": "00:30",
            "slotLabelInterval": "00:01:00",
        }
    elif TimeSetting == "1 Hour":
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
            "slotDuration": "01:00",
            "slotLabelInterval": "00:01:00",
        }
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
    # Adding Different Calendar Views
    selected_view = st.selectbox(
        "Select Calendar View:",
        ["dayGridMonth", "timeGridWeek", "timeGridDay", "listMonth"],
        format_func=format_option,
        index=1,
    )
    calendar_options["initialView"] = selected_view
    # Add Custom Options
    state = calendar(
        options=calendar_options,
        custom_css=calendar_css,
    )

# Render Custom CSS
st.markdown(f"<style>{page_css}</style>", unsafe_allow_html=True)
