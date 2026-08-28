import dns.resolver


RECORD_TYPES = [
    "A",
    "AAAA",
    "MX",
    "NS",
    "TXT"
]


def lookup_dns(domain: str) -> dict:

    results = {}

    for record_type in RECORD_TYPES:

        results[record_type] = []

        try:
            answers = dns.resolver.resolve(
                domain,
                record_type,
                lifetime=5
            )

            for answer in answers:
                results[record_type].append(
                    str(answer)
                )

        except (
            dns.resolver.NoAnswer,
            dns.resolver.NXDOMAIN,
            dns.resolver.NoNameservers,
            dns.exception.Timeout
        ):
            pass

    return results
