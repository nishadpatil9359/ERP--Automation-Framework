from utils.navigation import open_leave_request


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


def create_leave(page):

    close_open_modals(page)

    open_leave_request(page)

    page.locator("a").filter(
        has_text="Add Leave"
    ).click()

    # Employee
    page.locator(
        "#create-leave-modal select[name='employee_id']"
    ).select_option(
        label="Nishad Patil"
    )

    # Month
    page.locator(
        "#create-leave-modal input[name='month']"
    ).fill("8")

    # Leave Type
    page.locator(
        "#create-leave-modal select[name='leave_type_id']"
    ).select_option(
        label="Sick Leave"
    )

    # Start Date
    page.locator(
        "#create-leave-modal input[name='start_date']"
    ).fill("08/20/2026")

    # End Date
    page.locator(
        "#create-leave-modal input[name='end_date']"
    ).fill("08/21/2026")

    # Duration
    page.locator(
        "#create-leave-modal input[name='duration']"
    ).fill("2")

    # Description
    page.locator(
        "#create-leave-modal textarea[name='description']"
    ).fill(
        "Created by Playwright Automation"
    )

    # Save
    page.locator(
        "#create-leave-modal"
    ).get_by_role(
        "button",
        name="Save"
    ).click()

    page.wait_for_timeout(1500)


def test_create_leave(page):

    create_leave(page)