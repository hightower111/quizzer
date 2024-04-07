import streamlit as st

st.set_page_config(initial_sidebar_state='collapsed')

st.markdown(
    '''
<style>
    [data-testid='collapsedControl'] {
        display: none
    }
</style>
    ''',
    unsafe_allow_html = True
)

st.write("Welcome home traveller, have a seat and prepare for the treacherous journey ahead")

st.write('rules')

if st.button("START ", use_container_width=True):
    st.switch_page("pages/0439403.py")
