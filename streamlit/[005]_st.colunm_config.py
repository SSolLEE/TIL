import pandas as pd
import streamlit as st
from datetime import datetime
from datetime import date
from datetime import time

# column
data_df = pd.DataFrame(
    {
        "widgets" : ["st.selectbox", "st.number_input", "st.text_area", "st.button"]
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets" : st.column_config.Column(
            "Streamlit Widgets", 
            help = "Streamlit **widget** commands",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic"
)

# TextColumn
data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.TextColumn(
            "Widgets",
            help="Streamlit **widget** commands 🎈",
            width="large",
            default="st.",
            max_chars=50,
            validate="^st\.[a-z_]+$",
        )
    },
    hide_index=True,
)

# NumberColumn
data_df = pd.DataFrame({
    "price":[20, 950, 250, 500]
})
st.data_editor(
    data_df, 
    column_config={
        "price" : st.column_config.NumberColumn(
            "Price(in USD)",
            help="The price of the product in USD",
            min_value=0,
            max_value=1000,
            step=1,
            format="$%d",
        )
    }, hide_index=True
)

# CheckboxColumn
data_df = pd.DataFrame({
    "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    "favorite" : [True, False, True, False],
})
st.data_editor(
    data_df,
    column_config={
        "favorite": st.column_config.CheckboxColumn(
            "Your favorite?",
            help="Select your **favorite** widgets.",
            default=False,
        )
    }, 
    disabled=['widgets'],
    hide_index=True,
)

# SelectboxColumn
data_df = pd.DataFrame(
    {
        "category": [
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "📊 Data Exploration",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "category": st.column_config.SelectboxColumn(
            "App Category",
            help="The category of the app",
            width="medium",
            options=[
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM",
            ],
        )
    },
    hide_index=True,
)

# DatetimeColumn
data_df = pd.DataFrame({
    "appointment": [datetime(2024, 5, 15, 12, 40), 
                    datetime(2023, 11, 15, 4, 0),
                    datetime(2025, 1, 23, 18, 27),
                    datetime(2024, 10, 22, 22, 20)]
}) 
st.data_editor(
    data_df,
    column_config={
        "appointment":st.column_config.DateColumn(
            "Appointment",
            min_value=datetime(2023, 9, 1),
            max_value=datetime(2025, 2, 1),
            format="D MMM YYYY, h:mm a",
            step=60,
        ),
    },
    hide_index=True
)

# DateColumn
data_df = pd.DataFrame({
    "birthday" : [date(1979, 3, 2),
                  date(1989, 6, 12),
                  date(2002, 10, 30),
                  date(2020, 12, 31),]
})
st.data_editor(
    data_df,
    column_config={
        "birthday": st.column_config.DateColumn(
            "Birthday",
            min_value=date(1970, 1, 1),
            max_value=date(2021, 1, 1),
            format= "DD.MM.YYYY",
            step=1,
        )
    }, hide_index=True,
)

# TimeColumn
data_df = pd.DataFrame(
    {
        "appointment": [
            time(12, 30),
            time(18, 0),
            time(9, 10),
            time(16, 25),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "appointment": st.column_config.TimeColumn(
            "Appointment",
            min_value=time(8, 0, 0),
            max_value=time(19, 0, 0),
            format="hh:mm a",
            step=60,
        ),
    },
    hide_index=True,
)