import streamlit as st
import configurations as config


def get_chapter_informations():
    chapter_informations = []
    chapters = st.number_input(
        'Number of Chapters', min_value=1, max_value=20, step=1)

    cols = st.columns(chapters)

    for i, col in enumerate(cols):
        chapter_information = {}
        col.subheader(f'Chapter {i+1} Details')
        chapter_information['title'] = col.text_input(
            f'''Chapter {i+1}'s title''', key=f'chapter_{i+1}_title')
        chapter_information['dialogue_proportion'] = col.number_input(
            f'''Chapter {i+1}'s dialogue proportion''', key=f'chapter_{i+1}_dialogue')
        # chapter_information['details'] = col.text_area(
        #     f'''Chapter {i+1}'s details''', key=f'chapter_{i+1}_detail')

        chapter_informations.append(chapter_information)

    return chapter_informations
