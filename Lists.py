def parse_csv_line(line):
    fields = []
    field = ''
    in_quotes = False
    for char in line:
        if char == '"' and not in_quotes:
            in_quotes = True
        elif char == '"' and in_quotes:
            in_quotes = False
        elif char == ',' and not in_quotes:
            fields.append(field)
            field = ''
        else:
            field += char
    fields.append(field)
    return fields

def get_movies_by_genre(file_path, genre):
    movies = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
        headers = parse_csv_line(lines[0].strip())
        print(f"Headers: {headers}")  # Debugging line to check headers
        if 'Genre' not in headers or 'Title' not in headers or 'Duration (min)' not in headers:
            print("Error: Required columns are missing in the CSV file.")
            return movies
        
        genre_index = headers.index('Genre')
        title_index = headers.index('Title')
        duration_index = headers.index('Duration (min)')
        
        for line in lines[1:]:
            row = parse_csv_line(line.strip())
            if len(row) > max(genre_index, title_index, duration_index):
                if genre.lower() in row[genre_index].lower():
                    movies[row[title_index]] = row[duration_index]
            else:
                print(f"Skipping malformed line: {line.strip()}")
    return movies

def export_movies_to_file(movies, output_file):
    with open(output_file, mode='w', encoding='utf-8') as file:
        for title, duration in movies.items():
            file.write(f"{title}: {duration} min\n")

def main():
    file_path = r'C:/Users/sharo/OneDrive/Documents/Intro to informatics/imdb-movies-dataset.csv'
    genre = "Action"  # Example genre input
    movies = get_movies_by_genre(file_path, genre)
    if movies:
        output_file = f"{genre}_movies.txt"
        export_movies_to_file(movies, output_file)
        print(f"Movies of genre '{genre}' have been exported to {output_file}")
    else:
        print(f"No movies found for genre '{genre}'")

if __name__ == "__main__":
    main()