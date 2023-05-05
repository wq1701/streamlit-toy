import streamlit as st

def data_transfer():
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