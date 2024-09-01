def create_backstory_prompt(character_details):
    name = character_details.get('Name')
    species = character_details.get('Species/Race')
    gender = character_details.get('Gender')
    age = character_details.get('Age')
    personality_traits = ', '.join(character_details.get('Personality Traits', []))
    strengths = ', '.join(character_details.get('Strengths', []))
    home_environment = character_details.get('Home Environment')
    occupation = character_details.get('Occupation/Role')
    magic_abilities = character_details.get('Magic or Special Abilities')
    fear_secret = character_details.get('Fear or Secret', 'a deep fear of the dark forests that surround their village')

    backstory_prompt = (
        f"You are a creative writer for a fantasy world-building app. Based on the following details, generate a rich and engaging backstory for a fantasy character, using less than 500 words.\n\n"
        f"Character Details:\n"
        f"- Name: {name}\n"
        f"- Species/Race: {species}\n"
        f"- Gender: {gender}\n"
        f"- Age: {age}\n\n"
        f"Personality and Traits:\n"
        f"- Personality Traits: {personality_traits}\n"
        f"- Strengths: {strengths}\n"
        f"- Home Environment: {home_environment}\n"
        f"- Occupation/Role: {occupation}\n"
        f"- Magic or Special Abilities: {magic_abilities}\n"
        f"- Fear or Secret: {fear_secret}\n\n"
        f"Using these details, craft a detailed backstory that explains the character's origins, significant life events, relationships, and motivations. Be sure to highlight their unique traits and how they have shaped the character’s journey so far. The backstory should be imaginative, engaging, and consistent with the fantasy setting."
    )
    
    return backstory_prompt
