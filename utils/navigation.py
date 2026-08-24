from playwright.sync_api import TimeoutError


def open_hrm_menu(page):
    """Expand HRM menu if it is collapsed."""

    department = page.get_by_role(
        "link",
        name="Department"
    )

    try:
        department.wait_for(
            state="visible",
            timeout=1000
        )

    except TimeoutError:
        page.get_by_role(
            "link",
            name="HRM"
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