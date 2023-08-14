from collections import defaultdict


class SalaryService:
    def calculate_average_salary_by_company_size(self, data):
        salary_counts = defaultdict(lambda: defaultdict(int))
        salary_sums = defaultdict(lambda: defaultdict(int))

        for salary_data in data:
            salary_counts[salary_data.job_title][salary_data.company_size] += 1
            salary_sums[salary_data.job_title][salary_data.company_size] += salary_data.salary

        average_salaries = []
        for job_title, size_counts in salary_counts.items():
            salary_entry = {"job_title": job_title}
            for company_size, count in size_counts.items():
                average_salary = salary_sums[job_title][company_size] / count
                salary_entry[f"average_salary_{company_size}"] = int(
                    average_salary)

            average_salaries.append(salary_entry)

        return average_salaries

    def calculate_average_salary_by_experience(self, data):
        salary_counts = defaultdict(lambda: defaultdict(int))
        salary_sums = defaultdict(lambda: defaultdict(int))

        for salary_data in data:
            job_title = salary_data.job_title
            experience_level = salary_data.experience_level
            salary = salary_data.salary

            salary_counts[job_title][experience_level] += 1
            salary_sums[job_title][experience_level] += salary

        average_salaries = []
        for job_title, size_counts in salary_counts.items():
            salary_entry = {"job_title": job_title}
            for experience_level, count in size_counts.items():
                average_salary = salary_sums[job_title][experience_level] / count
                salary_entry[f"average_salary_{experience_level}"] = int(
                    average_salary)

            average_salaries.append(salary_entry)

        return average_salaries
