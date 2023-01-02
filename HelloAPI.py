import ctypes

# create a handle to User32.dll for access to the MessageBoxW function
user_handle = ctypes.WinDLL("User32.dll")
# create a handle to Kernel32.dll for error handling
k_handle = ctypes.WinDLL("Kernel32.dll")
hwnd = None  # Owner window not used
lpText = "Hello World!"  # Message that will be displayed
lpCaption = "Welcome to the the Win API"  # Message Box title
uType = 0x00000001  # Message box type "OK Cancel"

# capture which button the user clicked in a variable named response
# OK = 1, CANCEL = 2
response = user_handle.MessageBoxW(hwnd, lpText, lpCaption, uType)
error = k_handle.GetLastError()
if error != 0:
    print("[-] Error code{0}".format(error))
    exit(1)
if response == 1:
    print("The user clicked OK")
elif response == 2:
    print("The user clicked Cancel")


print("The response was {0}".format(response))
