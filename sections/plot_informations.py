import streamlit as st
import configurations as config


def get_plot_informations():
    plot_informations = {}
    plot_informations['plot'] = st.text_area(
        'Plot', height=200, help='Provide the plot details.',
        max_chars=1000, placeholder=''' Ex. A scientist invents a device that allows people to experience others' memories and emotions, but when it falls into the wrong hands, it's used to manipulate and control, and the scientist must stop it before it's too late. ''')

    col1, col2 = st.columns(2)
    with col1:
        plot_informations['genre'] = st.selectbox(
            'Genre (Optional)', config.GENRES, index=None, placeholder='Choose the Genre.')
    with col2:
        plot_informations['narrative_style'] = st.selectbox(
            'Narrative style (Optional)', config.NARRATIVE_STYLE, index=None, placeholder='Choose the Narrative style')
    return plot_informations
