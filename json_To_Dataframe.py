import json
import pandas as pd
from pandas import json_normalize

# Open the JSON file and load the data
with open('./taylor_swift_original.json', 'r') as file:
    data = json.load(file)

def transformation_Json_To_Dataframe():
    """
    Converts a JSON file into a DataFrame and saves it as a CSV file.

    Loads a JSON file, transforms it into a DataFrame, normalizing
    its structure. Then, saves the resulting DataFrame to a CSV file.

    Args:
        json_file_path (str): Path to the input JSON file.
        csv_file_path (str): Path where the output CSV file will be saved.
    """
    # Load the JSON directly into a DataFrame
    df = pd.read_json('taylor_swift_original.json')

    # Print the first 5 rows of the DataFrame
    print(df.head(5))

    # Get and display the column names
    df_c = df.columns
    print(df_c)

    # Normalize the structure of the JSON data
    tracks_normalized = json_normalize(
        data,
        record_path=['albums', 'tracks'],  # Path to the records
        meta=[
            'artist_id',  # Artist metadata
            'artist_name',
            'artist_popularity',
            ['albums', 'album_id'],  # Album metadata
            ['albums', 'album_name'],
            ['albums', 'album_release_date'],
            ['albums', 'album_total_tracks']
        ]
    )
    
    # Print the normalized DataFrame
    print(tracks_normalized)
    print(tracks_normalized.columns)

    # Replace the prefix 'albums.' with 'album_' in the column names
    tracks_normalized.columns = tracks_normalized.columns.str.replace('albums.', 'album_', regex=False)
    
    # Print the DataFrame after renaming columns
    print(tracks_normalized)
    print(tracks_normalized.columns)

    # Rename specific columns directly
    tracks_normalized.rename(columns={
        'album_album_id': 'album_id',
        'album_album_name': 'album_name',
        'album_album_release_date': 'album_release_date',
        'album_album_total_tracks': 'album_total_tracks'
    }, inplace=True)

    # Show the final result of the DataFrame
    print(tracks_normalized)
    print(tracks_normalized.columns)

    # Save the DataFrame as a CSV file
    csv_file_path = './tracks_data.csv'  
    tracks_normalized.to_csv(csv_file_path, index=False)  
    print(f"DataFrame saved as CSV at: {csv_file_path}")

if __name__ == "__main__":
    transformation_Json_To_Dataframe()  
