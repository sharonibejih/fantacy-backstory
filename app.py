import streamlit as st
from services.backstoryGenerarator import create_backstory_prompt
from services.imageGenerator import create_dalle_prompt
from utils import *


st.set_page_config(page_title="Fantasy Character Backstory Creator", layout="wide")

st.title("🧙 Fantasy Character Backstory Creator")
st.write("Create a unique fantasy character and generate a backstory along with an image!")

# Collect character details from the user
st.sidebar.header("Character Details")
name = st.sidebar.text_input("Character Name", "Elara Windwhisper")
species = st.sidebar.selectbox("Species/Race", ["Elf", "Human", "Dwarf", "Orc", "Dragon", "Other"])
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Non-Binary", "Other"])
age = st.sidebar.text_input("Age", "120 years")

personality_traits = st.sidebar.text_input("Personality Traits (comma-separated)", "brave, compassionate")
strengths = st.sidebar.text_input("Strengths (comma-separated)", "skilled archer")
home_environment = st.sidebar.text_input("Home Environment", "enchanted forest")
occupation = st.sidebar.text_input("Occupation/Role", "Guardian of the Sacred Grove")
magic_abilities = st.sidebar.text_input("Magic or Special Abilities", "Communicates with animals")
fear_secret = st.sidebar.text_area("Fear or Secret", "afraid of failing her people and living in her mother’s shadow")
appearance_details = st.sidebar.text_area("Appearance Details", "long silver hair, bright green eyes, leather armor with leaf patterns")

# Button to generate backstory and image
if st.sidebar.button("Generate Character"):
    character_details = {
        'Name': name,
        'Species/Race': species,
        'Gender': gender,
        'Age': age,
        'Personality Traits': personality_traits.split(', '),
        'Strengths': strengths.split(', '),
        'Home Environment': home_environment,
        'Occupation/Role': occupation,
        'Magic or Special Abilities': magic_abilities,
        'Fear or Secret': fear_secret,
        'Appearance': appearance_details
    }

    # Generate image
    image_prompt = create_dalle_prompt(character_details)
    st.subheader("Character Image")
    image = generate_image(image_prompt)
    st.image(image, caption=f"{name} - {species}", use_column_width=True)

    # Generate backstory
    backstory_prompt = create_backstory_prompt(character_details)
    backstory = generate_backstory(backstory_prompt)
    st.subheader("Character Backstory")
    st.write(backstory)

    # st.success("Character backstory and image generated successfully!")

# Styling the app
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://www.transparenttextures.com/patterns/paper-fibers.png');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
