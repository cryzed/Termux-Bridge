# Termux-Bridge
Simple "bridge" that allows applications not running under [Termux](https://play.google.com/store/apps/details?id=com.termux) to execute shell commands within the Termux environment and getting their output.

# Usage
Run ``python termux_bridge.py /path/to/some/folder &`` and keep the Termux session running. The script will automatically attempt to execute the contents of any new file created within the folder and write the stdout output, stderr output and exit status respectively to files with the same path and the suffixes ".stdout", ".stderr" and ".exit_status". The original file will be deleted after the execution has finished.

The deletion of the original file signals if the command has finished running: simply wait until it is deleted before accessing the resulting output files.

A flow to easily run commands in the Termux Bridge for [Automate](https://play.google.com/store/apps/details?id=com.llamalab.automate) is available [here](http://llamalab.com/automate/community/flows/2957).

# Requirements
``pip install watchdog``
