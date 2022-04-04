import configparser

config = configparser.ConfigParser()
config.read('/Users/RKhan/PycharmProjects/SeeTestCloud_POV_Management/config.properties')


# Ability to create a new .txt file which can be populated by a list of 'items'
def write_to_file(file_name, items):
    with open(file_name, 'w') as f:
        for item in items:
            f.write("%s\n" % item)


def logger(message):
    print(message)


def get_access_key():
    return config.get('seetest_authorization', 'access_key')


# When Base Auth in use as part of Header, the API running against is only designed for Basic Auth
def base_authentication():
    return config.get('seetest_authorization', 'basic_auth')


def get_cloud_url():
    return config.get('seetest_urls', 'cloud_url')


def get_base_endpoint():
    return config.get('end_points', 'base_endpoint')


def get_projects_endpoint():
    return config.get('end_points', 'projects')


def get_device_groups_endpoint():
    return config.get('end_points', 'device_groups')


def get_devices_endpoint():
    return config.get('end_points', 'devices')


def get_reporter_endpoint():
    return config.get('end_points', 'reporter')


def get_users_endpoint():
    return config.get('end_points', 'users')


def get_applications_endpoint():
    return config.get('end_points', 'applications')

