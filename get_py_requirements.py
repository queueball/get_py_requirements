#!/usr/bin/env python3
import subprocess
import tempfile
import shutil
import sys

import click


@click.command()
@click.argument("modules", nargs=-1)
@click.option("--debug", is_flag=True, default=False)
@click.option("--python", default=None)
def main(modules, python, debug):
    temp_path = None
    result = None
    try:
        temp_path = tempfile.mkdtemp()
        result = subprocess.check_output(
            [
                sys.executable if not python else python,
                "-m",
                "pip",
                "download",
                *modules,
                "-d",
                temp_path,
                "--no-binary",
                ":all:",
            ]
        )
        result = (

            subprocess.check_output(
                [
                    "ls",
                    temp_path,
                ]
            )
            .decode("utf-8")
            .strip()
        )
        if debug:
            print('"""')
            print(result)
            print('"""')
        if result:
            print(f"### { ' '.join(sorted(modules)) }")
        for line in sorted(result.split("\n")):
            if line:
                *req, version = (
                    line.replace(".tar.gz", "").replace(".zip", "").split("-")
                )
                print(f'{ "-".join(req) }=={ version }')
    except Exception as e:
        print(e)
        print(result)
    finally:
        if temp_path:
            shutil.rmtree(temp_path, True)


if __name__ == "__main__":
    main()

# AUTOBIN: get_requirements
