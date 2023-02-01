# Automating-POV-Processes

## Background

The purpose of the framework is to reduce manual tasks required when going through the process of creating a new Project, or deleting a Project.
There are a number of steps involved when creating or deleting a project, hopefully this framework would serve as a base foundation of a tool that can be shared both internally within the company, but externally as well to customers.

### Setting up a new project

Manually setting up a new project involves a number of steps. Here is an example of the steps:

- Create a Device Group
- Create a Project
  - Assign the Device Group to the Project
  - Configure Project
    - Set resources (number of parallel sessions, cleanup modes, etc.)
    - Upload Native Applications to the Cloud
  - Assign iOS & Android Devices to the Project (_Not yet implemented_)
    - Cleanup Devices (Uninstall apps, clear browser cache, etc.) (_Not yet implemented_)
  - Create & Assign new Users 

### Deleting Project

Deleting the Project involves the following steps:

- Un-assign iOS & Android Mobile Devices from the Device Group
- Delete Users from the Project
- Delete the Device Group
- Delete the Project

## Setup

Open a Terminal window in the project root folder, and run the following commands to set up an enclosed virtual environment that holds all necessary packages required to run the project:

```
python3 -m pip install --user virtualenv
```
```
python3 -m venv env
```
```
source env/bin/activate
```
```
pip3 install -r requirements.txt
```

## Running the tests

### Create a new Project

From the Terminal window, run the following command:

```commandline
paver run setup project_name
```
**project_name** variable should be replaced by the actual Project Name.

### Delete a Project

From the Terminal window, run the following command:

```commandline
paver run teardown project_name
```
**project_name** variable should be replaced by the actual Project Name.
