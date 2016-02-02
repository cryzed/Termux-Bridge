# Termux-Bridge
Simple "bridge" that allows applications not running under Termux to execute shell commands within the Termux environment and getting the stdout and stderr output.

# Usage
Run ``python termux_bridge.py /path/to/some/folder &`` and keep the Termux session running. The script will automatically attempt to execute the contents of any new file created within the folder, write the output to files with the same name and the suffix ".stdout" and ".stderr" respectively and delete the original file after the exection has finished.

The deletion of the original file can be considered a signal to detect if the command has finished running -- simply wait until it is deleted before accessing the resulting output files.

# Requirements
``pip install watchdog``
