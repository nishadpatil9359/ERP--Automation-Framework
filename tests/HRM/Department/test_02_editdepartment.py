import time

from playwright.sync_api import expect

from utils.navigation import open_department
from test_01_department import create_department


def update_department(page):

    print("\nUpdating Department...")

    timestamp = int(time.time())

    updated_department = (
        f"Updated_Department_{timestamp}"
    )

    # Navigate to Department
    open_department(page)

    # Edit latest/first department
    page.get_by_role(
        "button",
        name="Edit"
    ).first.click()

    # Update Name
    page.locator(
        '#edit-department-modal input[name="name"]'
    ).fill(updated_department)

    # Update Description
    page.locator(
        '#edit-department-modal textarea[name="description"]'
    ).fill(
        "Updated by Playwright Automation"
    )

    # Update
    page.get_by_role(
        "button",
        name="Update"
    ).click()

    page.wait_for_timeout(1500)

    # Verify
    expect(
        page.get_by_text(
            updated_department
        ).first
    ).to_be_visible()

    print(
        f"✅ Department Updated : {updated_department}"
    )

    return updated_department


def test_update_department(page):

    create_department(page)
    update_department(page)