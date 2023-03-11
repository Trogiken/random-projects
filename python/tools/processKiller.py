import os
import sys
import subprocess
import time
import signal


def list_processes(requested_process=None):
    """List all processes or those that contain requested_process in their name"""
    all_processes = subprocess.check_output('tasklist /fo csv /nh', shell=True).splitlines()

    process_list = []
    for process in all_processes:
        prs = str(process, 'utf-8')
        image_name = prs.split(',')[0]
        pid = prs.split(',')[1]
        if requested_process is None:
            process_list.append({'image_name': image_name, 'pid': pid})
        elif requested_process.lower() in image_name.lower():
            process_list.append({'image_name': image_name, 'pid': pid})
        else:
            continue

    return process_list


def kill_processes(processes: list):
    """Kill a list of processes by pid"""
    for pid in processes:
        try:
            pid = int(pid)
        except (ValueError, TypeError):
            raise f"failed to make pid an integer | {type(pid)}: {pid}"

        try:
            os.kill(pid, signal.SIGTERM)
            time.sleep(0.5)
        except Exception:
            continue


def q_prompt(question: str):
    """Prompt the user with a yes/no question"""
    print()

    print(question + " (y/n)")
    user = input("> ").lower()

    if user == 'y':
        return True
    elif user == 'n':
        return False
    else:
        q_prompt(question)


def is_admin():
    try:
        # assuming powershell is installed and set to PATH
        result = subprocess.check_output(['powershell', '-Command', '([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)'])
        return result.decode().strip() == 'True'
    except subprocess.CalledProcessError:
        return False


def close(exit_code: int=0):
    """Close the script"""
    print("Exiting...")
    sys.exit(exit_code)


def main():
    if not is_admin():  # check if script is running as admin
        input("You must run this script as an administrator\n[Press any key to exit]")
        close(1)

    while True:
        os.system('cls')  # clear terminal

        user_query = input("Enter a process name (leave blank to list all processes)\n[0 to Exit]> ")
        if user_query == '0':
            close(0)

        print()  # print empty line

        # list processes
        print("Searching for processes...")
        listed_processes = list_processes(user_query)
        if listed_processes:  # if process_list is not empty
            for prs in listed_processes:  # print processes that will be killed
                print(f'{prs["image_name"]}: {prs["pid"]}')
        else:
            reload = q_prompt('No processes found - Try Again?')
            if reload:
                continue
            else:
                close(0)

        # ask before killing
        user_verify = q_prompt('[WARNING] Kill the following processes?')
        if user_verify:  # kill processes in processes_to_kill list
            os.system('cls')
            print('Killing processes...')
            pid_kill_list = [process['pid'] for process in listed_processes]  # extract pid's from processes
            kill_processes([pid.strip('"') for pid in pid_kill_list])  # pass pid's with internal double quotes removed
            time.sleep(3)  # delay for processes to clean up
        else:
            continue

        # query again and examine if there are process left
        new_query = list_processes(user_query)
        if new_query:  # print any processes remaining after the killing using same query
            print(f'Failed to kill the following processes:')
            for prs in new_query:
                print(f'{prs["image_name"]}: {prs["pid"]}')
        else:
            print(f'Successfully killed all {len(listed_processes)} processes')

        print()  # print empty line

        # ask to kill more processes
        restart = q_prompt('Kill more processes?')
        if restart:
            continue
        else:
            close(0)


if __name__ == "__main__":
    main()
