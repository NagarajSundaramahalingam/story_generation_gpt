import streamlit as st
import configurations as config


NO_OF_CHARACTERS_IN_ROW = 3


def create_characters(characters, character_informations):
    rows = (characters + 2) // NO_OF_CHARACTERS_IN_ROW

    for i in range(rows):
        row = st.empty()
        start_index = i * NO_OF_CHARACTERS_IN_ROW
        end_index = min((i + 1) * NO_OF_CHARACTERS_IN_ROW, characters)

        with row:

            columns = st.columns(NO_OF_CHARACTERS_IN_ROW)

            for i, column in enumerate(columns):
                character_information = {}
                st.subheader(f'Character {start_index+i+1} Details')
                character_information['name'] = st.text_input(
                    f'''Character {start_index+i+1}'s Name''', key=f'character_{start_index+i+1}_name')
                character_information['gender'] = st.selectbox(
                    f'''Character {start_index+i+1}'s Gender''', config.GENDER, key=f'character_{start_index+i+1}_gender')
                character_information['age'] = st.number_input(
                    f'''Character {start_index+i+1}'s Age''', min_value=1, step=1, key=f'character_{start_index+i+1}_age')
                character_information['appearance'] = st.text_area(f'''Character {start_index+i+1}'s Appearance (Optional)''',
                                                                   key=f'character_{start_index+i+1}_appearance')
                character_information['personality'] = st.text_area(f'''Character {start_index+i+1}'s Personality (Optional)''',
                                                                    key=f'character_{start_index+i+1}_personality')
                character_information['others'] = st.text_area(f'''Character {start_index+i+1}'s Other details (Optional)''',
                                                               key=f'character_{start_index+i+1}_other_details')

                character_informations.append(character_information)

    return character_informations


def character_details(cols, character_informations, start_index=0):

    if not cols:
        return

    for i, col in enumerate(cols[:5], start=start_index):
        character_information = {}
        col.subheader(f'Character {i+1} Details')
        character_information['name'] = col.text_input(
            f'''Character {i+1}'s Name''', key=f'character_{i+1}_name')
        character_information['gender'] = col.selectbox(
            f'''Character {i+1}'s Gender''', config.GENDER, key=f'character_{i+1}_gender')
        character_information['age'] = col.number_input(
            f'''Character {i+1}'s Age''', min_value=1, step=1, key=f'character_{i+1}_age')
        character_information['appearance'] = col.text_area(f'''Character {i+1}'s Appearance (Optional)''',
                                                            key=f'character_{i+1}_appearance')
        character_information['personality'] = col.text_area(f'''Character {i+1}'s Personality (Optional)''',
                                                             key=f'character_{i+1}_personality')
        character_information['others'] = col.text_area(f'''Character {i+1}'s Other details (Optional)''',
                                                        key=f'character_{i+1}_other_details')

        character_informations.append(character_information)

    st.divider()

    character_details(cols[5:], character_informations, start_index+5)


def get_character_informations():
    character_informations = []
    characters = st.number_input(
        'Number of Characters', min_value=1, max_value=10, step=1)
    # character_informations = create_characters(
    #     characters, character_informations)

    cols = st.columns(characters)

    for i, col in enumerate(cols):
        character_information = {}
        col.subheader(f'Character {i+1} Details')
        character_information['name'] = col.text_input(
            f'''Character {i+1}'s Name''', key=f'character_{i+1}_name')
        character_information['gender'] = col.selectbox(
            f'''Character {i+1}'s Gender''', config.GENDER, key=f'character_{i+1}_gender')
        character_information['age'] = col.number_input(
            f'''Character {i+1}'s Age''', min_value=1, step=1, key=f'character_{i+1}_age')
        character_information['appearance'] = col.text_area(f'''Character {i+1}'s Appearance (Optional)''',
                                                            key=f'character_{i+1}_appearance')
        character_information['personality'] = col.text_area(f'''Character {i+1}'s Personality (Optional)''',
                                                             key=f'character_{i+1}_personality')
        character_information['others'] = col.text_area(f'''Character {i+1}'s Other details (Optional)''',
                                                        key=f'character_{i+1}_other_details')

        character_informations.append(character_information)


    return character_informations
