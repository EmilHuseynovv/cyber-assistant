import ipaddress
import re


def validate_ip(value: str) -> bool:
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


def validate_domain(domain: str) -> bool:
    if len(domain) > 253:
        return False

    pattern = r"^(?=.{1,253}$)(?!-)([a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,63}$"

    return bool(re.match(pattern, domain))
