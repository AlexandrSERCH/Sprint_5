import base64

import allure
from allure_commons.types import AttachmentType


def attach_screenshot(driver, *, name: str = "screenshot_before_quit") -> None:
    try:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=name,
            attachment_type=AttachmentType.PNG,
        )
    except Exception:
        pass


def attach_full_page_screenshot(driver, *, name: str = "screenshot_full_page_before_quit") -> None:
    try:
        metrics = driver.execute_cdp_cmd("Page.getLayoutMetrics", {})
        width = metrics["contentSize"]["width"]
        height = metrics["contentSize"]["height"]
        screenshot = driver.execute_cdp_cmd(
            "Page.captureScreenshot",
            {
                "format": "png",
                "captureBeyondViewport": True,
                "clip": {"x": 0, "y": 0, "width": width, "height": height, "scale": 1},
            },
        )
        allure.attach(
            base64.b64decode(screenshot["data"]),
            name=name,
            attachment_type=AttachmentType.PNG,
        )
    except Exception:
        pass
