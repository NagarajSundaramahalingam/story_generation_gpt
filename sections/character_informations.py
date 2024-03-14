import streamlit as st
import configurations as config


def get_character_informations():
    character_informations = []
    characters = st.number_input(
        'Number of Characters', min_value=1, max_value=10, step=1)

    cols = st.columns(characters)

    for i, col in enumerate(cols):
        character_information = {}
        col.subheader(f'Character {i+1} Details')
        character_information[f'character {i+1} name'] = col.text_input(
            f'''Character {i+1}'s Name''', key=f'character_{i+1}_name')
        character_information[f'character {i+1} gender'] = col.selectbox(
            f'''Character {i+1}'s Gender''', config.GENDER, key=f'character_{i+1}_gender')
        character_information[f'character {i+1} age'] = col.number_input(
            f'''Character {i+1}'s Age''', min_value=1, step=1, key=f'character_{i+1}_age')
        # character_information[f'character {i+1} appearance'] = col.text_area(f'''Character {i+1}'s Appearance (Optional)''',
        #                                                                     key=f'character_{i+1}_appearance')
        character_information[f'character {i+1} details'] = col.text_area(f'''Character {i+1}'s Details (Optional)''',
                                                                          key=f'character_{i+1}_details')
        # character_information['others'] = col.text_area(f'''Character {i+1}'s Other details (Optional)''',
        #                                                 key=f'character_{i+1}_other_details')

        character_informations.append(character_information)

    return character_informations
