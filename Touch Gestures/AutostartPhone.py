#!/usr/bin/python
import subprocess
import os

#Command that runs when we don't have a specific command for a given device
DEFAULT_SCRCPY_COMMAND = "scrcpy -m 1400 --turn-screen-off --stay-awake"

#Custom scrcpy command that runs for given devices
CUSTOM_DEVICE_COMMANDS = {
	"device1-serial" : "scrcpy  -m 1084 --turn-screen-off --stay-awake",
}

open_scrcpy_instances = []

#Starts scrcpy for the given device if the device is ready and scrcpy is not already running
def start_scrcpy(adb_device_item):
	#adb connection state can be device or offline (or no-device)
	is_online = "\tdevice".encode(encoding='UTF-8') in adb_device_item
	device_serial = adb_device_item.split()[0]
	#Device is connected and scrcpy is not connected, run new scrcpy instance
	if is_online and not device_serial in open_scrcpy_instances:
		open_scrcpy_instances.append(device_serial)

		device_command = CUSTOM_DEVICE_COMMANDS.get(device_serial, DEFAULT_SCRCPY_COMMAND)
		subprocess_command_list = device_command.split()

		#run scrcpy for this device specifically
		subprocess_command_list.append("--serial")
		subprocess_command_list.append(device_serial)
		os.system("printf '\e[2t'")
		print("Running Command:")


		print(subprocess_command_list)

		#start scrcpy
		subprocess.Popen(subprocess_command_list)

	#the device is now offline, so we should remove it from the list of active scrcpy instnaces
	elif not is_online and device_serial in open_scrcpy_instances:
		open_scrcpy_instances.remove(device_serial)


#Get notified of adb device changes using the adb track-devices command
track_devices = subprocess.Popen(["adb", "track-devices"], stdout=subprocess.PIPE)

while track_devices.poll() is None:
	#wait for an entire line of input
	track_devices.stdout.readline()

	#When track devices gives us new output, explicitly get the list of devices in total
	adb_device_list = subprocess.check_output(["adb", "devices"]).splitlines()

	#Remove the text header : "List of devices attached"
	adb_device_list.pop(0)

	#Start scrcpy for each device if necessary
	for adb_device_item in adb_device_list:
		if adb_device_item:
			start_scrcpy(adb_device_item)

	#Remove obselete scrcpy instances, i.e. items for which we had started scrcpy but
	#no longer appear to be actually connected via adb
	adb_device_list = filter(None, adb_device_list)
	adb_device_list = [item.split()[0] for item in adb_device_list]
	for scrcpy_item in open_scrcpy_instances:
		if scrcpy_item not in adb_device_list and scrcpy_item in open_scrcpy_instances:
			open_scrcpy_instances.remove(scrcpy_item)

	#Print current status of connected scrcpy items
	print("auto-scrcpy: Currently connected devices : ", open_scrcpy_instances)
