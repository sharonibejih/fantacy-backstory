def create_dalle_prompt(character_details):
    
    name = character_details.get('Name')
    species = character_details.get('Species/Race')
    gender = character_details.get('Gender')
    age = character_details.get('Age')
    personality_traits = ', '.join(character_details.get('Personality Traits', []))
    strengths = ', '.join(character_details.get('Strengths', []))
    home_environment = character_details.get('Home Environment')
    occupation = character_details.get('Occupation/Role')
    magic_abilities = character_details.get('Magic or Special Abilities')
    appearance_details = character_details.get('Appearance', '')

    prompt = (
        f"A {gender} {species} named {name}, "
        f"aged {age}, known for being {personality_traits}. "
        f"They have strengths such as {strengths} and are often seen in their "
        f"{home_environment}. {name} works as a {occupation}. "
        f"{magic_abilities} are among their special abilities. "
        f"Appearance details: {appearance_details}."
    )
    
    return prompt