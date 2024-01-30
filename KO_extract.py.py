import urllib.request

def fetch_data(organism_code):
    """Fetch data from KEGG for a given organism code."""
    url = f'http://rest.kegg.jp/link/ko/{organism_code}'
    try:
        response = urllib.request.urlopen(url, timeout=20)
        return response.read().decode('utf-8')
    except Exception as e:
        print(f"An error occurred while fetching data for {organism_code}: {e}")
        return ''

def read_organism_codes(file_path):
    """Read organism codes from a file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def extract_ko_part(data):
    """Extract the 'ko:' part from the data."""
    return [line.split('\t')[1] for line in data.splitlines() if '\t' in line]

# Prompt the user to enter the path to the file containing organism codes
input_file = input("Enter the path to the file containing organism codes: ")

# Read organism codes from the file
organism_codes = read_organism_codes(input_file)

# Collect and process data for each organism code
all_data = ''
for code in organism_codes:
    data = fetch_data(code)
    if data:
        ko_data = extract_ko_part(data)
        all_data += '\n'.join(ko_data) + '\n'

# Prompt the user to enter the output file path
output_file = input("Enter the output file path: ")

# Save the processed data to the specified file
try:
    with open(output_file, 'w') as file:
        file.write(all_data)
    print(f"Data has been saved to {output_file}")
except Exception as e:
    print(f"An error occurred while saving the file: {e}")

