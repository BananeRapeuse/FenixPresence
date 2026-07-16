from pathlib import Path
import sys
import subprocess



TASK_NAME = "FenixPresence"



def get_program_command():

    if getattr(
        sys,
        "frozen",
        False
    ):

        return str(
            Path(sys.executable)
        )


    else:

        python = str(
            Path(sys.executable)
        )


        script = str(
            Path(__file__).parent.parent / "main.py"
        )


        return f'{python} "{script}"'



def enable_startup():

    command = get_program_command()


    task_command = [
        "schtasks",
        "/create",
        "/tn",
        TASK_NAME,
        "/tr",
        f'"{command}"',
        "/sc",
        "onlogon",
        "/f"
    ]


    result = subprocess.run(
        task_command,
        capture_output=True,
        text=True
    )


    if result.returncode != 0:

        raise Exception(
            result.stderr
        )



def disable_startup():

    subprocess.run(
        [
            "schtasks",
            "/delete",
            "/tn",
            TASK_NAME,
            "/f"
        ],
        capture_output=True,
        text=True
    )



def is_startup_enabled():

    result = subprocess.run(
        [
            "schtasks",
            "/query",
            "/tn",
            TASK_NAME
        ],
        capture_output=True,
        text=True
    )


    return result.returncode == 0