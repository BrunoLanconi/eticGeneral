import csv
import random
import string


def create_sample_csv(filename: str, rows: int = 12):
    """
    Creates a sample CSV file with random data.

    Args:
        filename (str): The path and name of the CSV file to be created.
    """
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        HEADER = [
            "Name",
            "Age",
            "Gender",
            "Department",
            "Salary",
            "Email",
            "Phone",
            "Address",
            "City",
            "State",
            "Country",
            "Postal Code",
        ]

        writer.writerow(HEADER)

        for _ in range(rows):
            name = "".join(random.choices(string.ascii_uppercase, k=5))
            age = random.randint(20, 60)
            gender = random.choice(["Male", "Female"])
            department = random.choice(["Sales", "Marketing", "Finance", "IT"])
            salary = random.randint(30000, 80000)
            email = f"{name.lower()}@company.com"
            phone = "".join(random.choices(string.digits, k=10))
            address = "".join(
                random.choices(string.ascii_uppercase + string.digits, k=10)
            )
            city = random.choice(["New York", "London", "Paris", "Tokyo"])
            state = random.choice(["NY", "CA", "TX", "FL"])
            country = random.choice(["USA", "UK", "France", "Japan"])
            postal_code = "".join(random.choices(string.digits, k=5))
            row = [
                name,
                age,
                gender,
                department,
                salary,
                email,
                phone,
                address,
                city,
                state,
                country,
                postal_code,
            ]

            writer.writerow(row)


def main():
    create_sample_csv("inputs/employees.csv", 10000)


if __name__ == "__main__":
    main()
