def create_bins(remote_ratios):
    bins = {}
    for value in remote_ratios:
        bin = str(value)
        bins[bin] = bins.get(bin, 0) + 1
    sorted_bins = sorted(bins.items(), key=lambda x: int(x[0]))
    return [{"bin": bin, "amount": amount} for bin, amount in sorted_bins]


def calculate_average_salary(data):
    salary_counts = {}
    salary_sums = {}

    for doc in data:
        job_title = doc["job_title"]
        company_size = doc["company_size"]
        salary = doc["salary_in_usd"]

        if job_title not in salary_counts:
            salary_counts[job_title] = {}
            salary_sums[job_title] = {}

        size_counts = salary_counts[job_title]
        size_sums = salary_sums[job_title]

        if company_size not in size_counts:
            size_counts[company_size] = 0
            size_sums[company_size] = 0

        size_counts[company_size] += 1
        size_sums[company_size] += salary

    average_salaries = []
    for job_title, size_counts in salary_counts.items():
        salary_entry = {"job_title": job_title}

        for company_size, count in size_counts.items():
            average_salary = salary_sums[job_title][company_size] / count
            salary_entry[f"salary_{company_size}"] = average_salary

        average_salaries.append(salary_entry)

    return average_salaries