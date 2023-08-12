import pandas as pd

def clean_csv(input_path, output_path):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(input_path)
        
        # Drop duplicate rows
        df_cleaned = df.drop_duplicates()
        
        # Save the cleaned DataFrame to a new CSV file
        df_cleaned.to_csv(output_path, index=False)
        
        print("CSV file cleaned successfully.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    input_file = "input.csv"  # Replace with the path to your input CSV file
    output_file = "cleaned_output.csv"  # Replace with the desired name for the cleaned output file
    
    clean_csv(input_file, output_file)
