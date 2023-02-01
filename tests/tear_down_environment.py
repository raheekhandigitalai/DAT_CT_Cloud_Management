import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from api import device_groups
from api import projects
from api import applications
from api import devices
from api import users


def tear_down_environment_test(project_name):
    # device_group_id = 3488932
    # project_id = 3488933
    device_id = 4840738

    device_group_id = device_groups.get_device_group_id(project_name)
    device_group_id = str(device_group_id)
    project_id = projects.get_project_id(project_name)

    device_groups.remove_devices_from_device_group(device_id, device_group_id)
    users.get_users_from_project_and_delete(project_id)

    device_groups.delete_device_group(device_group_id)
    projects.delete_project(project_id)


if __name__ == "__main__":
    tear_down_environment_test(sys.argv[1])
