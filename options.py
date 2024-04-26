import streamlit as st

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