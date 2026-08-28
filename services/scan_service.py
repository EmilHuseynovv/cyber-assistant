import subprocess


def run_nmap_scan(target: str) -> str:

    result = subprocess.run(
        [
            "nmap",
            "-sV",
            "--open",
            "--version-light",
            target
        ],
        capture_output=True,
        text=True,
        timeout=60
    )

    if result.returncode != 0:
        raise RuntimeError(
            result.stderr.strip()
        )

    return result.stdout
