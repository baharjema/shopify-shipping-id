import streamlit as st
import pandas as pd
import numpy as np

st.title('Shopify Shipping Indonesia')

if not hasattr(st, 'already_started_server'):
    st.already_started_server = True

    st.write('''
        The first time this script executes it will run forever because it's
        running a Flask server.

        Just close this browser tab and open a new one to see your Streamlit
        app.
    ''')
    
    from fastapi import FastAPI
    app = FastAPI()

    @app.get('/shipping-rate')
    def shipping_rate():
        return {"item": "Eco bottle"}
    pass

