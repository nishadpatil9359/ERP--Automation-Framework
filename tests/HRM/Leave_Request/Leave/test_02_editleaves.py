import time

from utils.navigation import open_leave
from test_01_leave import create_leave


def update_leave(page):

    print("\nUpdating Leave...")

    timestamp = int(time.time())

    # Open Leave page
    open_leave(page)

    # Latest entry is at the top
    page.get_by_role(
        "button",
        name="Edit"
    ).first.click()

    # Employee
    page.locator(
        'select[name="employee_id"]'
    ).select_option(label="Nishad Patil")

    # Month
    page.locator(
        'input[name="month"]'
    ).fill("9")

    # Change Leave Type
    page.locator(
        'select[name="leave_type_id"]'
    ).select_option(label="Casual Leave")

    # Change Start Date
    page.locator(
        'input[name="start_date"]'
    ).fill("2026-09-10")

    # Change End Date
    page.locator(
        'input[name="end_date"]'
    ).fill("2026-09-12")

    # Change Duration
    page.locator(
        'input[name="duration"]'
    ).fill("3")

    # Keep status Approved
    page.locator(
        'select[name="status"]'
    ).select_option(label="Approved")

    # Change Description
    page.locator(
        'textarea[name="description"]'
    ).fill(
        f"Leave updated by Playwright Automation {timestamp}"
    )

    # Update
    page.get_by_role(
        "button",
        name="Update"
    ).click()

    page.wait_for_timeout(1500)

    print("✅ Leave Updated Successfully")


def test_update_leave(page):

    # Create a fresh leave first
    create_leave(page)

    # Edit the latest entry
    update_leave(page)