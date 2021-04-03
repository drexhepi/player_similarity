import streamlit as st
import pandas as pd
import numpy as np

df = st.cache(pd.read_csv)('players_list.csv')

players = st.multiselect('Top 10 players', df['player'].unique())

st.title('10 players similar to: {}'.format(players[0]))
new_df = df[df['player'].isin(players)]

st.write(new_df[['similar_player','rank']])