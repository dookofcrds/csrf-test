from bs4 import BeautifulSoup

# Prompt the user to paste the HTML content
print("Paste the HTML content you want to examine:")
html_content = input()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the title tag content
title_tag = soup.find('title')
if title_tag:
    title_content = title_tag.text
    print(f"Title: {title_content}")
else:
    print("No title tag found.")

# Extract the meta description tag content
meta_description_tag = soup.find('meta', attrs={'name': 'description'})
if meta_description_tag:
    meta_description_content = meta_description_tag.get('content')
    print(f"Meta Description: {meta_description_content}")
else:
    print("No meta description tag found.")

# Extract and print all links
links = soup.find_all('a')
if links:
    print("Links:")
    for link in links:
        link_url = link.get('href')
        print(link_url)
else:
    print("No links found.")

# Extract and print privileged user information
user_info = soup.find('div', class_='user-info')
if user_info:
    user_info_content = user_info.text.strip()
    print(f"User Information: {user_info_content}")
else:
    print("No user information found.")

# Extract and print relevant privileged data based on class names or attributes
privileged_data_elements = soup.find_all(['div', 'span'], class_=['private', 'sensitive', 'confidential'])
for element in privileged_data_elements:
    content = element.text.strip()
    print(f"Privileged Data Element: {content}")

# Extract and print script contents
script_tags = soup.find_all('script')
for script_tag in script_tags:
    script_content = script_tag.text
    print(f"Script Content: {script_content}")

# Extract and print other types of information as needed
# Add more BeautifulSoup parsing here to extract various elements with relevant data

# Extract and print form fields and their names
form_fields = soup.find_all('input')
if form_fields:
    print("Form Fields:")
    for field in form_fields:
        field_name = field.get('name')
        print(f"Form Field Name: {field_name}")

# Extract and print CSS styles
style_tags = soup.find_all('style')
for style_tag in style_tags:
    style_content = style_tag.text
    print(f"CSS Style Content: {style_content}")

# Note: Be cautious while extracting sensitive or privileged information from HTML.
# Ensure you have the legal right to access and process such data.

