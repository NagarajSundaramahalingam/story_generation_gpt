import streamlit as st
import configurations as config
from sections import plot_informations, character_informations

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


if __name__ == '__main__':
    main()
