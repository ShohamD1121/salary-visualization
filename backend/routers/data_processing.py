from fastapi import APIRouter
from utils.data_processing import create_bins, calculate_average_salary_by_company_size, calculate_average_salary_by_experience
from db import salaries

router = APIRouter()


@router.get("/remote-ratios")
def get_remote_ratios():
    pipeline = [
        # Include only the remote_ratio field
        {"$project": {"remote_ratio": 1}},
        {
            "$group": {"_id": None, "remote_ratios": {"$push": "$remote_ratio"}}
        },  # Group all remote_ratio values into an array
        {
            "$project": {"_id": 0, "remote_ratios": 1}
        },  # Exclude the _id field from the response
    ]

    result = list(salaries.aggregate(pipeline))
    if result:
        remote_ratios = result[0]["remote_ratios"]
        remote_ratios_json = create_bins(remote_ratios)
        return remote_ratios_json


@router.get("/average-salary-by-company-size")
def get_remote_ratios():
    data = salaries.find()
    return calculate_average_salary_by_company_size(data)


@router.get("/average-salary-by-experience-level")
def get_average_salary_by_experience():
    data = salaries.find()
    return calculate_average_salary_by_experience(data)
