import pandas as pd

def count_student_frequency(student_name, file_paths):
    """
    Counts the frequency of a student's name across multiple CSV files.
    
    Parameters:
    - student_name: str, the student name in the format "Last, First".
    - file_paths: list of str, file paths to the CSV files to search through.
    
    Returns:
    - int, the frequency of the student name across the provided CSV files.
    """
    frequency = 0
    
    for file_path in file_paths:
        # Load the current CSV file
        df = pd.read_csv(file_path)
        
        # Check if 'Student Name' column exists in the file
        if 'Student Name' in df.columns:
            # Increment frequency if the student name is in the 'Student Name' column
            if student_name in df['Student Name'].values:
                frequency += 1
                
    return frequency

# Example usage:
# Define the paths to your CSV files
file_paths = [
    "Modified_5%_PHS_STUDENTS_TIER_3_Nurse_Log.csv",
    "Modified_5%_PHS_STUDENTS_TIER_3_Truancies_25+.csv",
    "Modified_5%_PHS_STUDENTS_TIER_3_Credit_Deficiency.csv",
    "5% PHS STUDENTS TIER 3 - McKinney Vento.csv",
    "5% PHS STUDENTS TIER 3 - Foster Youth (Current_Fomer).csv",
    "5% PHS STUDENTS TIER 3 - 3 or more Fs.csv"
]

# Count frequency of a student
student_name = "Marquez Garnica, Angie"
frequency = count_student_frequency(student_name, file_paths)
print(f"The student {student_name} appears in {frequency} files.")
