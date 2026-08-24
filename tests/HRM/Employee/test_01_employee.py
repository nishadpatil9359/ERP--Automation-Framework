import time

from utils.navigation import open_employee


def create_employee(page):

    print("\nCreating Employee...")

    timestamp = int(time.time())

    employee_name = f"Employee_{timestamp}"

    # Navigate to Employee
    open_employee(page)

    # Add Employee
    page.locator("a").filter(
        has_text="Add Employee"
    ).click()

    # Name
    page.locator(
        'input[name="name"]'
    ).fill(employee_name)

    # Gender
    page.locator(
        'input[name="gender"]'
    ).fill("Male")

    # Phone
    page.locator(
        'input[name="phone"]'
    ).fill(
        f"98{timestamp}"[-10:]
    )

    # Salary
    page.get_by_role(
        "spinbutton"
    ).fill("30000")

    # Email
    page.locator(
        'input[name="email"]'
    ).fill(
        f"employee{timestamp}@gmail.com"
    )

    # Country
    page.locator(
        'input[name="country"]'
    ).fill("India")

    # Birth Date
    page.locator(
        'input[name="birth_date"]'
    ).fill("2004-06-23")

    # Join Date
    page.locator(
        'input[name="join_date"]'
    ).fill("2026-07-08")

    # Department
    page.locator(
        'select[name="department_id"]'
    ).select_option("44")

    # Designation
    page.locator(
        'select[name="designation_id"]'
    ).select_option("33")

    # Shift
    page.locator(
        'select[name="shift_id"]'
    ).select_option("8")

    # DO NOT upload employee image

    # Save
    page.get_by_role(
        "button",
        name="Save"
    ).click()

    page.wait_for_timeout(1500)

    print(
        f"✅ Employee Created : {employee_name}"
    )

    return employee_name


def test_create_employee(page):

    create_employee(page)