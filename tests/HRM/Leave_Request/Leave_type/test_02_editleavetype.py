import time

from utils.navigation import open_leave_type
from test_01_leavetype import create_leave_type


def update_leave_type(page):

    print("\nUpdating Leave Type...")

    timestamp = int(time.time())

    updated_leave_type = (
        f"Updated_Leave_Type_{timestamp}"
    )

    # Open Leave Type
    open_leave_type(page)

    # Latest entry = first entry
    page.get_by_role(
        "button",
        name="Edit"
    ).first.click()

    # Leave Type Name
    page.locator(
        '#edit-leave-type-modal input[name="name"]'
    ).fill(updated_leave_type)

    # Description
    page.locator(
        '#edit-leave-type-modal textarea[name="description"]'
    ).fill(
        "Updated by Playwright Automation"
    )

    # Paid Leave remains Yes
    # Status remains Active

    # Update
    page.get_by_role(
        "button",
        name="Update"
    ).click()

    page.wait_for_timeout(1500)

    print(
        f"✅ Leave Type Updated : {updated_leave_type}"
    )

    return updated_leave_type


def test_update_leave_type(page):

    # Create a new Leave Type
    create_leave_type(page)

    # Edit the latest entry
    update_leave_type(page)