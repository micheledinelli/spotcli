from halo import Halo

import modules.utils as utils

def get_devices(sp, show=False):
    '''
    Command to retrieve and optionally display information about available Spotify devices.

    Parameters:
    - show (bool): A flag to indicate whether to display the available devices in a table format.

    Returns:
    - device_list (list): List of available devices.
    '''
    with Halo(text='Fetching devices', spinner='dots'):
        # Retrieve information about available devices from Spotify API
        devices_dict = sp.devices()

    device_list = devices_dict["devices"]
    if show:
        # Display the JSON
        utils.pretty_print_json(device_list)

    # Return the list of available devices
    return device_list