import time

from utils.navigation import open_designation


def create_designation(page):

    print("\nCreating Designation...")

    timestamp = int(time.time())

    designation_name = (
        f"Automation_Designation_{timestamp}"
    )

    description = "Created by Playwright Automation"

    # Navigate to Designation
    open_designation(page)

    # Add Designation
    page.locator("a").filter(
        has_text="Add Designation"
    ).click()

    # Name
    page.locator(
        '#create-designation-modal input[name="name"]'
    ).fill(designation_name)

    # Description
    page.locator(
        '#create-designation-modal textarea[name="description"]'
    ).fill(description)

    # Save
    page.get_by_role(
        "button",
        name="Save"
    ).click()

    page.wait_for_timeout(1500)

    print(
        f"✅ Designation Created : {designation_name}"
    )

    return designation_name


def test_create_designation(page):

    create_designation(page)