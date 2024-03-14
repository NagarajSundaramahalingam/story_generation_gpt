import streamlit as st
import configurations as config
from sections import plot_informations, character_informations, chapter_informations
import utils
import model_operations
import glob
from pathlib import Path
import os
import datetime

st.set_page_config(layout='wide')


FIRST_CHAPTER_FILE = '1_CHAPTER.txt'


def main():
    st.title('Story Generation', help='Generating a novel using LLM-GW')

    plot_details_expander = st.expander('Plot Details', expanded=False)
    with plot_details_expander:
        plot_details = plot_informations.get_plot_informations()

    character_details_expander = st.expander(
        'Character Details', expanded=False)
    with character_details_expander:
        character_details = character_informations.get_character_informations()

    chapter_details_expander = st.expander(
        'Chapter Details', expanded=False)
    with chapter_details_expander:
        chapter_details = chapter_informations.get_chapter_informations()

        if st.button('Generate'):

            STORY_FOLDER = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

            plot_details['characters_count'] = len(character_details)

            character_descriptions = ''
            for character_detail in character_details:
                for key, value in character_detail.items():
                    character_descriptions += f'{key.capitalize()} is {value}. '

            character_descriptions = character_descriptions.rstrip(' and ')

            st.write('Novel is generating...')

            plot_details['character_descriptions'] = character_descriptions
            system_prompt = utils.get_system_prompt(plot_details)

            user_prompt = f'''Generate the chapter for the title {chapter_details[0].get('title')} with the dialogue proportion of {chapter_details[0].get('dialogue_proportion')} %'''
            chapter_text = model_operations.get_output_from_model(
                system_prompt, user_prompt)

            st.write('Chapter 1 is generated.')

            Path(f'{config.OUTPUT_FOLDER}{STORY_FOLDER}').mkdir(
                parents=True, exist_ok=True)

            with open(f'{config.OUTPUT_FOLDER}{STORY_FOLDER}/{FIRST_CHAPTER_FILE}', 'w') as f:
                f.write(chapter_text)

            for index, chapter in enumerate(chapter_details[1:], start=2):
                chapter_files = glob.glob(
                    f'{config.OUTPUT_FOLDER}{STORY_FOLDER}/*.txt')

                chapter_content = ''
                for chapter_file in chapter_files:

                    with open(chapter_file) as f:
                        chapter_content += f.read()

                user_prompt = f''' Summarize the chapter content {chapter_content} with 2000 words max'''

                prev_chapter_summarize = model_operations.get_output_from_model(
                    system_prompt, user_prompt)

                summarize_file = f'{index-1}_summarize.log'
                with open(f'{config.OUTPUT_FOLDER}{STORY_FOLDER}/{summarize_file}', 'w') as f:
                    f.write(prev_chapter_summarize)

                user_prompt = f'''Prev Chapter summarize {prev_chapter_summarize}. Generate the chapter for the title CHAPTER {index}. {chapter.get('title')} with the dialogue proportion of {chapter.get('dialogue_proportion')} % and more description as a paragraph'''

                chapter_text = model_operations.get_output_from_model(
                    system_prompt, user_prompt)

                st.write(f'Chapter {index} is generated.')

                chapter_file = f'{index}_CHAPTER.txt'

                with open(f'{config.OUTPUT_FOLDER}{STORY_FOLDER}/{chapter_file}', 'w') as f:
                    f.write(chapter_text)

            chapter_files = glob.glob(
                f'{config.OUTPUT_FOLDER}{STORY_FOLDER}/*.txt')

            chapter_files.sort(key=lambda x: os.path.getctime(x))

            novel_content = ''
            for chapter_file in chapter_files:

                with open(chapter_file) as f:
                    novel_content += f.read()
                    novel_content += '\n'
                    novel_content += '___'
                    novel_content += '\n'

            st.markdown(novel_content)
            utils.text_to_pdf(
                novel_content, f'{config.OUTPUT_FOLDER}{STORY_FOLDER}/story.pdf')


if __name__ == '__main__':
    main()
