import pkg_resources
from pathlib import Path
import subprocess
import sys 

req_path = Path(__file__).with_name("requirements.txt")

def test_requirements():
    reqs = pkg_resources.parse_requirements(req_path.open())
    for req in reqs:
        req = str(req)
        try:
            pkg_resources.require(req)
        except pkg_resources.DistributionNotFound as e:
            print(e)
            print("Missing dependencies, will install the dependencies listed in requirements.txt")
            install()
        except pkg_resources.VersionConflict as e:
            print(e)
            print("Version conflict. Take a look at the dependencies try to find a combination that works")

    print("All dependencies are installed!")

def install():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

test_requirements()