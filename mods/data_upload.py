import streamlit as st

def data_upload():
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