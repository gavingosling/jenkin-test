import pkg_resources
from pathlib import Path
import subprocess
import sys 
import argparse
import os

def test_requirements():
    parser = argparse.ArgumentParser(description="""
                                            Checks whether all dependencies are installed.
                                            """)
    parser.add_argument('--path', type=str,
                        help="""
                        Path of parent folder of requirements.txt
                        """)
    args = parser.parse_args()
    parent = Path(__file__).with_name(args.path)
    parent_abs = str(parent.resolve())
    parent_dir_name = parent_abs.split("/")[-1]

    req_path = Path(os.path.join(parent.resolve(), "requirements.txt"))
    reqs = pkg_resources.parse_requirements(req_path.open())
    for req in reqs:
        req = str(req)
        try:
            pkg_resources.require(req)
        except pkg_resources.DistributionNotFound as e:
            print(e)
            print("Missing dependencies, will install the dependencies listed in requirements.txt")
            install(parent_dir_name)
        except pkg_resources.VersionConflict as e:
            print(e)
            print("Version conflict. Take a look at the dependencies try to find a combination that works")

    print("All dependencies are installed!")

def install(dirname):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", f"{dirname}/requirements.txt"])

test_requirements()