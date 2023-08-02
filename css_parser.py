import re

def populate_css_with_character_data(css_file_path, character_data):
	# Read the CSS script
	with open(css_file_path, 'r') as file:
		css_content = file.read()
		
	# Define the placeholder tags and their corresponding data keys
	placeholder_tags = {
		'{character_name}': 'name',
		'{character_stats}': 'stats',
		# Add more placeholder tags for other character data elements
	}
	
	# Replace the placeholder tags with the character data
	for tag, data_key in placeholder_tags.items():
		if tag in css_content:
			replacement_data = character_data.get(data_key, '')
			css_content = css_content.replace(tag, str(replacement_data))
			
	# Write the updated CSS content back to the file
	with open(css_file_path, 'w') as file:
		file.write(css_content)
		
# Example usage
css_file_path = 'path/to/your/css_script.css'
character_data = {
	'name': 'John Doe',
	'stats': 'Strength: 10, Agility: 8, Intelligence: 12',
	# Add more character data elements as needed
}

populate_css_with_character_data(css_file_path, character_data)
