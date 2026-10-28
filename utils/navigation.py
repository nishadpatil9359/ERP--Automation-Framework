
from playwright.sync_api import TimeoutError


def close_open_modal(page):
    """Close an open modal before navigating to another module."""

    modal_ids = [
        "#create-employee-modal",
        "#edit-employee-modal",
        "#create-leave-modal",
        "#create-leave-type-modal",
        "#create-shift-modal",
        "#edit-shift-modal",
    ]

    for modal_id in modal_ids:
        modal = page.locator(modal_id)

        try:
            if modal.is_visible():
                cancel_button = modal.get_by_role(
                    "button",
                    name="Cancel",
                    exact=True
                )

                if cancel_button.is_visible():
                    cancel_button.click()
                else:
                    page.keyboard.press("Escape")

                modal.wait_for(
                    state="hidden",
                    timeout=5000
                )

        except TimeoutError:
            print(f"Warning: Could not close modal {modal_id}")

def open_leave(page):
    """Open the Leave page under HRM > Leave Request."""

    if "/hrm/leaves" in page.url:
        return

    open_hrm_menu(page)

    leave_request = page.get_by_role(
        "link",
        name="Leave Request",
        exact=True
    )

    leave_request.wait_for(state="visible")

    leave_link = page.get_by_role(
        "link",
        name="Leave",
        exact=True
    )

    try:
        leave_link.wait_for(state="visible", timeout=2000)
    except TimeoutError:
        leave_request.click()
        leave_link.wait_for(state="visible", timeout=10000)

    leave_link.click()

    page.wait_for_url(
        "**/hrm/leaves",
        timeout=15000
    )


def open_hrm_menu(page):
    """Expand HRM menu if it is collapsed."""

    close_open_modal(page)

    department = page.get_by_role(
        "link",
        name="Department",
        exact=True
    )

    try:
        department.wait_for(
            state="visible",
            timeout=1000
        )

    except TimeoutError:
        page.get_by_role(
            "link",
            name="HRM",
            exact=True
        ).click()

        department.wait_for(
            state="visible"
        )

def open_department(page):

    if "/hrm/department" in page.url:
        return

    open_hrm_menu(page)

    page.get_by_role(
        "link",
        name="Department"
    ).click()

    page.wait_for_load_state("networkidle")


def open_designation(page):

    if "/hrm/designations" in page.url:
        return

    open_hrm_menu(page)

    page.get_by_role(
        "link",
        name="Designation"
    ).click()

    page.wait_for_load_state("networkidle")


def open_shift(page):

    if "/hrm/shifts" in page.url:
        return

    open_hrm_menu(page)

    page.get_by_role(
        "link",
        name="Shift"
    ).click()

    page.wait_for_load_state("networkidle")


def open_employee(page):

    if "/hrm/employees" in page.url:
        return

    open_hrm_menu(page)

    page.get_by_role(
        "link",
        name="Employee"
    ).click()

    page.wait_for_load_state("networkidle")


def open_leave_request(page):
    """Open Leave Request section."""

    if "/hrm/leaves" in page.url:
        return

    open_hrm_menu(page)

    leave_request = page.get_by_role(
        "link",
        name="Leave Request"
    )

    leave_request.wait_for(
        state="visible"
    )

    leave_request.click()

    page.wait_for_load_state("networkidle")


def open_leave_type(page):
    """Open Leave Type under Leave Request."""

    if "/hrm/leave-types" in page.url:
        return

    open_hrm_menu(page)

    leave_request = page.get_by_role(
        "link",
        name="Leave Request"
    )

    leave_request.wait_for(
        state="visible"
    )

    # Check whether Leave Type is already visible
    leave_type = page.get_by_role(
        "link",
        name="Leave Type",
        exact=True
    )

    try:
        leave_type.wait_for(
            state="visible",
            timeout=1000
        )

    except TimeoutError:
        # Expand Leave Request
        leave_request.click()

        leave_type.wait_for(
            state="visible"
        )

    leave_type.click()

    page.wait_for_load_state("networkidle")