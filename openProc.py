# This script illustates a method of gaining a handle to a Windows process
# via the Windows API
import ctypes

# creat a handle to Kernel32.DLL for access to extended error codes
k_handle = ctypes.WinDLL("Kernel32.dll")

# setting process access rights and required parameters for the OpenProcess function
PROCESS_ALL_ACCESS = 0x000F0000 | 0x00010000 | 0xFFFF
dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False

# Have the user enter a process ID. Since input returns a string. I will have to
# convert the input value to hex so that it can be used as the dwProcessId parameter
user_pid_requested = input(
    "Enter the process ID of the process you want to connect to: "
)
# convert the user input from string to int
user_pid_requested_int = int(user_pid_requested)
# Now convert hex
user_pid_requested_hex = hex(user_pid_requested_int)
# convert the hex value to a base 16 int so that the final input value
# is a valid type for the dwProcessId parameter
user_pid_requested_hex_int = int(user_pid_requested_hex, 16)
dwProcessId = user_pid_requested_hex_int
response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)
error = k_handle.GetLastError()
if response <= 0:
    print(
        f"[-] Unable to create handle to dwProcessId {dwProcessId}. Error code: {error}"
    )
    exit(1)
else:
    print(
        f"[+] The dwProcessId is {dwProcessId} The process handle that we created is {response}"
    )
