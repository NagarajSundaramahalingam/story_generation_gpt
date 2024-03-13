import streamlit as st
import configurations as config
from sections import plot_informations, character_informations, chapter_informations
import utils
import model_operations
import glob
from pathlib import Path


st.set_page_config(layout='wide')


def main():
    st.title('Story Generation', help='Generating a novel using LLM-GW')

    plot_details_expander = st.expander('Plot Details', expanded=False)
    with plot_details_expander:
        plot_details = plot_informations.get_plot_informations()

        st.write(plot_details)

    character_details_expander = st.expander(
        'Character Details', expanded=False)
    with character_details_expander:
        character_details = character_informations.get_character_informations()

        st.write(character_details)

    chapter_details_expander = st.expander(
        'Chapeter Details', expanded=False)
    with chapter_details_expander:
        chapter_details = chapter_informations.get_chapter_informations()

        st.write(chapter_details)

        if st.button('Generate'):
            plot_details['characters_count'] = len(character_details)

            character_descriptions = ''
            for character_detail in character_details:
                for key, value in character_detail.items():
                    character_descriptions += f'{key.capitalize()} is {value}. '

            character_descriptions = character_descriptions.rstrip(' and ')

            plot_details['character_descriptions'] = character_descriptions
            system_prompt = utils.get_system_prompt(plot_details)

            st.write(system_prompt)

            user_prompt = f'''Generate the chapter for the title {chapter_details[0].get('title')} with the dialogue proportion of {chapter_details[0].get('dialogue_proportion')} %'''
            chapter_text = model_operations.get_output_from_model(
                system_prompt, user_prompt)

            st.write(chapter_text)

            st.write('---------')

            Path(f'''{config.OUTPUT_FOLDER}{plot_details['plot']}''').mkdir(
                parents=True, exist_ok=True)

            chapter_file = f'''{chapter_details[0].get('title')}.txt'''

            with open(f'''{config.OUTPUT_FOLDER}{plot_details['plot']}/{chapter_file}''', 'w') as f:
                f.write(chapter_text)

            for index, chapter in enumerate(chapter_details[1:], start=2):
                chapter_files = glob.glob(
                    f'''{config.OUTPUT_FOLDER}{plot_details['plot']}/*.txt''')

                # st.write(chapter_files)
                chapter_content = ''
                for chapter_file in chapter_files:

                    with open(chapter_file) as f:
                        chapter_content += f.read()

                user_prompt = f''' Summarize the chapter content {chapter_content} with 2000 words max'''

                prev_chapter_summarize = model_operations.get_output_from_model(
                    system_prompt, user_prompt)

                user_prompt = f'''Prev Chapter summarize {prev_chapter_summarize}. Generate the chapter for the title CHAPTER {index}. {chapter.get('title')} with the dialogue proportion of {chapter.get('dialogue_proportion')} %'''
                st.write(user_prompt)

                chapter_text = model_operations.get_output_from_model(
                    system_prompt, user_prompt)

                chapter_file = f'''{chapter.get('title')}.txt'''

                with open(f'''{config.OUTPUT_FOLDER}{plot_details['plot']}/{chapter_file}''', 'w') as f:
                    f.write(chapter_text)

                st.write(chapter_text)

                st.write('---------')

    chapter_files = glob.glob(
        f'''{config.OUTPUT_FOLDER}{plot_details['plot']}/*.txt''')

    novel_content = ''
    for chapter_file in chapter_files:

        with open(chapter_file) as f:
            novel_content += f.read()

    st.markdown(novel_content)


if __name__ == '__main__':
    main()
