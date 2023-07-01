salary_schema = {
          "work_year": int,
          "experience_level": str,
          "employment_type": str,
          "job_title": str,
          "salary": int,
          "salary_currency": str,
          "salary_in_usd": int,
          "employee_residence": str,
          "remote_ratio": int,
          "company_location": str,
          "company_size": str
}

### This Was Used to generate data into mongodb collection named Salaries
# csv_file = './ds_salaries.csv'
# with open(csv_file, 'r') as file:
#     reader = csv.reader(file)
#     next(reader)  # Skip header row
#     for row in reader:
#         obj = {}
#         for field, field_type in schema.items():
#             value = row.pop(0)  # Take the first value from the row
#             obj[field] = field_type(value)  # Convert value to the specified type
#         collection.insert_one(obj)
