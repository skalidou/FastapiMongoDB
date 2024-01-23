import pandas as pd

import streamlit as st
import altair as alt
from insert_mongo import *

myCollection = mydb['vinylcol']
st.write('Vinyle Soul&RNB')
df = pd.DataFrame(list(myCollection.find({}, {"_id":0})))
edited_df = st.experimental_data_editor(df, num_rows="dynamic")



df_barplot = pd.DataFrame(df, columns=["titre", "prix"]) 

if st.button('supprimer'):
    mydb.myCollection.delete_one('')
    st.write('done') 
chart = alt.Chart(df_barplot).mark_bar().encode(
    x='titre',
    y='prix'
).properties(
    width=alt.Step(6) 
)

st.write(chart)
