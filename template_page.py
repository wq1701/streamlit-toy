# streamlit run template_page.py

import os
from datetime import datetime
import base64

import pandas as pd
import streamlit as st
from PIL import Image
import time

import streamlit as st
from header import show_header

st.set_page_config(page_title="TEMPLATE_LAYOUT", page_icon="./icon/fish.ico", layout="wide",
                   initial_sidebar_state="auto", menu_items=None)


# Show the header on the main page
show_header()

# Add content to the main page
# st.write("Welcome to my app!")




# col1, col2, col3, col4 = st.columns(4)

# Create a sidebar with navigation links
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("About", "Data Transfer", "Data Upload", "CIME Q&A", "Contact"))

# Define the pages to display based on the selected link
if page == "About":
    st.title("A template layout for designing the application")
    st.markdown("Made with :heart: by **Weiwei**")

    st.image("./icon/fish.png", caption="This is a fish, I dunno why it is here")

    st.write("Below are the things you could do with this application: (maybe try markdown here later)")

    # Display some markdown text
    # st.markdown("# Welcome to my app!")
    # st.markdown("This is a demo of how to use `st.markdown()` in Streamlit.")
    st.markdown("---")
    st.markdown("## Features")
    st.markdown("- Data Transfer")
    st.markdown("- Data Upload")
    st.markdown("- CIME knowledge / bugs / resources index")
    st.markdown("- ...and?")

elif page == "Data Transfer":
    st.title("Data Transfer")
    st.write("This is the template layout for data transfer tool on CDSW")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("HDFS to ORACLE")
        st.write("This is for HDFS2ORACLE")

        src_hdfs = st.text_input("HDFS Source table", value="prod.dummy_source")
        tgt_orac = st.text_input("ORACLE Target table", value="oracle_dummy_target")

        if st.button("Transfer: HDFS2ORACLE"):
            # print(f"transferring {src_hdfs} to {tgt_orac}") # not gonna work
            st.write(f"transferring {src_hdfs} to {tgt_orac}")

    with col2:

        st.subheader("ORACLE to HDFS")
        st.write("This is for ORACLE2HDFS")

        src_orac = st.text_input("ORACLE Source table", value="oracle_dummy_source")
        tgt_hdfs = st.text_input("HDFS Target table", value="prod.dummy_target")

        if st.button("Transfer: ORACLE2HDFS"):
            # print("transferring from ")
            st.write(f"transferring {src_orac} to {tgt_hdfs}")


elif page == "Data Upload":
    st.title("BDF Data Loading Wizard")
    st.write("Upload your data to BDF directly, no FileZilla or Oracle needed!")

    st.markdown("Typical usage are")
    st.markdown("---")
    st.markdown("- WebMD data upload (potential large files)")
    st.markdown("- Switching group data upload (small files)")
    st.markdown("- and?")

    file_loc = st.text_input("file location on the server", value="file location")
    file_nm = st.text_input("file name on the server", value="file name")
    tgt_table_nm = st.text_input("target table name", value="prod.dummy_target")

    if st.button("Upload to BDF"):
        # print("transferring from ")
        st.write(f"Uploading {file_nm} to BDF table: {tgt_table_nm}")

elif page == "CIME Q&A":
    st.title("CIME knowledge index")
    st.write("Common Q&A of CIME projects")

else:
    st.title("Contact Page")
    st.write("You can contact us at contact@example.com.")





# with col3:
#     st.header("Section 3")
#     st.write("This is the content for Section 3.")
#
# with col4:
#     st.header("Section 4")
#     st.write("This is the content for Section 4.")
