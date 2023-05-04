import os
from datetime import datetime
import base64

import pandas as pd
import streamlit as st

import time

st.set_page_config(page_title="A Streamlit toy example", page_icon="./icon/fish.ico", layout="wide", initial_sidebar_state="auto", menu_items=None)

download_btn_disable = True

mapping_files = ["Previous Month Mapping", "Current DCM Report", "Current Web Extract", "V-LOOKUP Tables"]
upload_files = []
previous_mapping = None
dcm_report = None
web_extract = None
vLookup_tables = None