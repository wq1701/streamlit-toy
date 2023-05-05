import streamlit as st


# based on template_pages.py

def after_login():
    from header import show_header

    # st.set_page_config(page_title="TEMPLATE_LAYOUT", page_icon="./icon/fish.ico", layout="wide",
    #                    initial_sidebar_state="auto", menu_items=None)

    # Show the header on the main page
    show_header()

    # Add content to the main page
    # st.write("Welcome to my app!")

    # Create a sidebar with navigation links
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("About", "Data Transfer", "Data Upload", "Automation", "Team Q&A", "Contact"))

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
        st.markdown("- Team knowledge / bugs / resources index")
        st.markdown("- ...and?")

        st.markdown("## To-Do list")
        st.markdown("---")
        st.markdown(
            "- Add login credentials [ref](https://blog.streamlit.io/streamlit-authenticator-part-1-adding-an-authentication-component-to-your-app/)")
        st.markdown("- Make sure the app is compatible with the new clusters")
        st.markdown("- Make sure there are showcases for users and well tested before publishing")

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

    elif page == "Automation":
        col1, col2 = st.columns(2)

        with col1:

            st.subheader("A type of Automation: X")
            st.write("This is for X")

            study_x_name = st.text_input("Study X name", value="study_x_name")
            x_param1 = st.text_input("Paramater 1", value="202201")
            x_param2 = st.text_input("Paramater 2", value="202212")

            if st.button("Start: X Automation"):
                # print(f"transferring {src_hdfs} to {tgt_orac}") # not gonna work
                st.write(f"Running {study_x_name} based on {x_param1} and {x_param2}")

        with col2:

            st.subheader("Another type of Automation: Y")
            st.write("This is for Y")

            study_y_name = st.text_input("Study Y name", value="study_y_name")
            y_param1 = st.text_input("Paramater 1", value="Channel")
            y_param2 = st.text_input("Paramater 2", value="Source")
            y_param3 = st.text_input("Paramater 3", value="Date")

            if st.button("Start: Y Automation"):
                # print(f"transferring {src_hdfs} to {tgt_orac}") # not gonna work
                st.write(f"Running {study_y_name} based on {y_param1}, {y_param2} and {y_param3}")

    elif page == "Team Q&A":
        st.title("Team knowledge index")
        st.write("Common Q&A of Team projects")

    else:
        st.title("Contact Page")
        st.write("You can contact me at weiwei.qi@iqvia.com")
