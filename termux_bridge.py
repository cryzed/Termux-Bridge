import subprocess
import sys

import watchdog.events
import watchdog.observers

ENCODING = 'UTF-8'


class EventHandler(watchdog.events.FileSystemEventHandler):

    def __init__(self):
        self.ignored = set()

    def on_created(self, event):
        if event.src_path in self.ignored:
            self.ignored.remove(event.src_path)
            return

        self.ignored.add(event.src_path)

        with open(event.src_path, encoding=ENCODING) as file:
            command = file.read().strip()

        stdout_file_path = event.src_path + '.stdout'
        stderr_file_path = event.src_path + '.stderr'
        exit_status_path = event.src_path + '.exit_status'
        self.ignored.add(stdout_file_path)
        self.ignored.add(stderr_file_path)
        self.ignored.add(exit_status_path)

        # Write the returned exit status of the command and remove the command
        # file. This signals that the execution has finished, and is easily
        # checkable by either periodically listing the directory contents or
        # using Inotify. There's no need to worry about platform independence,
        # since this is only supposed to be used with Termux.
        command += ';echo $? > "%s";rm "%s"' % (exit_status_path, event.src_path)

        stdout = open(stdout_file_path, 'wb')
        stderr = open(stderr_file_path, 'wb')
        subprocess.Popen(command, shell=True, stdout=stdout, stderr=stderr)

    def on_deleted(self, event):
        # Prevent the set from constantly growing in size
        if event.src_path in self.ignored:
            self.ignored.remove(event.src_path)


def main(path):
    observer = watchdog.observers.Observer()
    observer.schedule(EventHandler(), path)
    observer.start()
    observer.join()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
