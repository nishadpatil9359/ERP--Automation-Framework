import time

from utils.navigation import open_leave_type


def close_open_modals(page):

    modal = page.locator(
        "#create-leave-modal"
    )

    if modal.is_visible():

        cancel_button = modal.get_by_role(
            "button",
            name="Cancel"
        )

        if cancel_button.is_visible():
            cancel_button.click()

        else:
            page.keyboard.press("Escape")


def create_leave_type(page):

    print("\nCreating Leave Type...")

    close_open_modals(page)

    open_leave_type(page)

    timestamp = int(time.time())

    leave_type_name = (
        f"Automation_Leave_Type_{timestamp}"
    )

    # Add Leave Type
    page.locator("a").filter(
        has_text="Add Leave Type"
    ).click()

    # Name
    page.locator(
        "#create-leave-type-modal input[name='name']"
    ).fill(
        leave_type_name
    )

    # Description
    page.locator(
        "#create-leave-type-modal textarea[name='description']"
    ).fill(
        "Created by Playwright Automation"
    )

    # Save
    page.locator(
        "#create-leave-type-modal"
    ).get_by_role(
        "button",
        name="Save"
    ).click()

    page.wait_for_timeout(1500)

    print(
        f"✅ Leave Type Created: {leave_type_name}"
    )

    return leave_type_name


def test_create_leave_type(page):

    create_leave_type(page)