import re


__product__ = "Bekchy (WAF)"


def detect(content, **kwargs):
    detection_schema = (
        re.compile("bekchy.(-.)?access.denied", re.I),
        re.compile("(http(s)?://)(www.)?bekchy.com(/report)?", re.I)
    )
    for detection in detection_schema:
        if detection.search(content) is not None:
            return True
