import time

from utils.navigation import open_department


def create_department(page):

    print("\nCreating Department...")

    timestamp = int(time.time())

    department_name = f"Automation_Department_{timestamp}"
    description = "Created by Playwright Automation"

    # Navigate to Department
    open_department(page)

    # Add Department
    page.locator("a").filter(
        has_text="Add Department"
    ).click()

    # Department Name
    page.locator(
        '#create-department-modal input[name="name"]'
    ).fill(department_name)

    # Description
    page.locator(
        '#create-department-modal textarea[name="description"]'
    ).fill(description)

    # Save
    page.get_by_role(
        "button",
        name="Save"
    ).click()

    page.wait_for_timeout(1500)

    print(
        f"✅ Department Created : {department_name}"
    )

    return department_name


def test_create_department(page):

    create_department(page)