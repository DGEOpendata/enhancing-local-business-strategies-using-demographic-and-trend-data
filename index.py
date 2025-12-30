python
import pandas as pd

# Load the dataset
file_path = 'Local_Business_Demographics_2023.csv'
dataset = pd.read_csv(file_path)

# Display the first few rows of the dataset
dataset.head()

# Analyze the number of businesses by type
business_type_counts = dataset['business_type'].value_counts()
print("Business Type Distribution:")
print(business_type_counts)

# Analyze the distribution of businesses by area
business_by_area = dataset.groupby('area')['business_type'].count()
print("Business Distribution by Area:")
print(business_by_area)

# Calculate the average number of employees per business type
average_employees = dataset.groupby('business_type')['number_of_employees'].mean()
print("Average Number of Employees by Business Type:")
print(average_employees)

# Export analysis results to a new CSV file
output_path = 'Business_Analysis_Results_2023.csv'
business_type_counts.to_csv(output_path, header=['Count'])
print(f"Analysis results saved to {output_path}")
