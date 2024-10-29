import pandas as pd
import re
from glob import glob
import csv

def get_unique_student_names(file_list):
    unique_names = set()
    
    for file in file_list:
        # Read each CSV file
        df = pd.read_csv(file)
        # Add names to the set to ensure uniqueness
        print(file)
        unique_names.update(df['Student Name'].dropna().unique())
    
    # Return the unique names as a sorted list
    return sorted(unique_names)

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
    file_paths_appear = []
    
    for file_path in file_paths:
        # Load the current CSV file
        df = pd.read_csv(file_path)
        
        # Check if 'Student Name' column exists in the file
        if 'Student Name' in df.columns:
            # Increment frequency if the student name is in the 'Student Name' column
            if student_name in df['Student Name'].values:
                frequency += 1
                file_paths_appear.append(file_path)
                
                
    return frequency, file_paths_appear

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


#student_list = get_unique_student_names(file_paths)

#for student in student_list:
#    frequency = count_student_frequency(student, file_paths)
#    print(f"The student {student} appears in {frequency} files.")

def generate_student_frequency_csv(file_paths, output_file):
    student_list = get_unique_student_names(file_paths)
    
    # Prepare the output data
    data = []
    for student in student_list:
        frequency, files_appeared_in = count_student_frequency(student, file_paths)
        data.append([student, frequency, "; ".join(files_appeared_in)])
    
    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Student Name", "Frequency", "File Paths Appeared In"])
        writer.writerows(data)

generate_student_frequency_csv(file_paths, "Student_Frequency_Report.csv")