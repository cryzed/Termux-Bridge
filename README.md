# Termux-Bridge
Simple "bridge" that allows applications not running under Termux to execute shell commands within the Termux environment and getting the stdout and stderr output.

# Usage
Run ``python termux_bridge.py /path/to/some/folder &`` and keep the Termux session running. The script will automatically attempt to execute the contents of any new file created within the folder and write the stdout and stderr output respectively to files with the same name and the suffixes ".stdout" and ".stderr". The original file will be deleted after the execution has finished.

The deletion of the original file signals if the command has finished running: simply wait until it is deleted before accessing the resulting output files.

A flow to easily run commands in the Termux Brdige for the [Automate application](https://play.google.com/store/apps/details?id=com.llamalab.automate) is available [here](http://llamalab.com/automate/community/flows/2957).

# Requirements
``pip install watchdog``
