"""Run an exercise script with its input prompts silenced.

``input("Enter radius: ")`` writes the prompt to stdout, where it lands in
front of whatever the script prints next. The grader compares printed output,
so the prompt has to go somewhere -- and stripping it afterwards means
guessing its wording. Discarding it at the source instead lets students phrase
prompts however they like, or omit them entirely.

Used by ``ScriptRunner``; not meant to be run by hand.
"""

import builtins
import runpy
import sys
import traceback


def main() -> int:
    script = sys.argv[1]
    sys.argv = sys.argv[1:]

    read_line = builtins.input
    builtins.input = lambda prompt="": read_line()

    try:
        runpy.run_path(script, run_name="__main__")
    except SystemExit as exit_request:
        return exit_request.code or 0
    except BaseException as error:
        # Report the script's own traceback: drop the frames belonging to this
        # runner so a student sees their error, not our plumbing.
        frames = error.__traceback__
        while frames and frames.tb_frame.f_code.co_filename != script:
            frames = frames.tb_next
        traceback.print_exception(type(error), error, frames)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
