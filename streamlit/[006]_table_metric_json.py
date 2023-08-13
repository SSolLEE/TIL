import streamlit as st
import pandas as pd
import numpy as np

# table
df = pd.DataFrame({
    'Apple' : [2, 2, 3], 
    'Lemon' : [4, 7, 1]})
st.table(df)

# metric
st.metric(label="Temperature", value="70 °F", delta="+1.2 °F")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "32℃", '2℃')
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")

# json
st.json({
    'foo':'bar',
    'baz':'boz',
    'stuff': [
        'stuff 1',
        'stuff 3',
        'stuff 6',
        'stuff 8',
    ]
})