#! /usr/bin/env python
import os
import sys
import json
from pathlib import Path


def read_credentials(file_path: Path) -> dict | None:
    """
    Read credentials from a provided file path. If the file doesn't exists, return None
    """
    if not file_path.exists():
        return None

    print(file_path)

    try:
        with file_path.open("r") as file:
            return json.load(file)

    except json.JSONDecodeError as exc:
        print(exc)

        return None
    

def main(file_path):
    file_path = Path(args[1])
    creds = read_credentials(file_path)

    if not creds:
        return
    

    with open('binfile', 'wb') as out:
        out.write(os.urandom(256))

        for env, cred in creds.items():
            out.writelines([f"AWS: {env}".encode()])
            out.writelines(
                list(f"{k} = {v}".encode() for k, v in cred.items())
            )

        out.write(os.urandom(256))


if __name__ == "__main__":
    args = sys.argv


    if not args:
        print("You must provide the file path as argument")

    elif len(args) != 2:
        print("You must provide only one argument: the file path ")

    else:
        main(args[1])
        
import os
