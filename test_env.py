import platform
import sys


def check_environment():
    print("=" * 40)
    print("PYTHON ENVIRONMENT CHECK")
    print("=" * 40)

    # 1. Version Check
    major, minor, micro = sys.version_info[:3]
    print(f"Python Version: {major}.{minor}.{micro}")

    if (major, minor) >= (3, 11):
        print("-> Status: PASS (Meets the Python 3.11+ requirement)")
    else:
        print("-> Status: FAIL (You must upgrade to Python 3.11 or newer)")

    # 2. Executable & OS Details
    print(f"Executable Path: {sys.executable}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print("=" * 40)


if __name__ == "__main__":
    check_environment()