# OUTSTANDING ACTION POINTS from this project
Having worked on system test a bit more. Have gain little progress. Following points need to be worked:  

Pt1> The communication protocol sequence of python sockets between server and client need to be better understood.

Pt2> Although Python threading seems to work in server.py, client_id it generate to be used on command, 'explore client_id path' is not used properly.

Pt3> there are error handling issues need to be further worked on    

PS. I will be overseas for two weeks starting 24/5/2024 and be back on 7/6/2024 inclusively.

# ASD demo project - a novel server-and-client design implemntation
Build a software system composed of client and server Python application where the server and client roles flipped: connected clients act as nodes in a distributed directory structure which the server can explore by issuing navigation commands. When interrogated, a client sends file structure information back to the server for display.

## Design and Communication Protocol
All source code modules are written in Python (version 3.9.0). Only standard Python modules are used. Software can be run in the containerised Docker environment from a host PC. Code modules: 'server.py' and 'client.py' are run in separate docker containers and communicate to each other via a docker network bridge using TCP protocol. Run time configuration data is placed in config file to facilitate deployment and operation security.

## Caveats and assumption
Directory structure is as below:

prjASD  -- submission.md

        -- server -- Dockerfile, server.py, server_config.json
                  -- unit_tests --__init__.py, test_server.py  
        -- client -- Dockerfile, client.py, client_config.json
                  -- unit_tests --__init__.py, test_client.py  
        -- system_tests -- test_system.py

Respective Unittest test modules assume this directory structure to locate modules and function to test. 

## Project setup
The project is developed in Winodws PC environment using Windows 10 (version 22H2, OS build 19045.4). Docker Desktop (version 4.30.0) is installed to manage docker containerization. VS Code editor is used for Python source coding editing. PowerShell (run as adminstrator) in Windows 10 for terminal interaction with the software applications.  

NOTE: When running docker containers: 'server-container' and 'client-container', 'server-container' should be first to run before 'client-container' so that 'client-container' can identify itself to 'server-container' of it being instantiated. 

## Design consideration
After decided to use Windows10 and docker containerization, the corresponding tools such as Docker Desktop, python version are installed and checked. Python unittest framework is adopted. 
The next step is to work on the directory structure for the project then source code writing in respective directories. 
Source code modules have been commented. Getting the coding working in a bigger picture and test aspect, then later ironing out the details and error handling.
Understood the telecom communication protocol as a telecom engineer, working on programming level need some polishing. There are more automation can be added for example, using docker-compose script to build images and bring up the environment 

## Usage instructions 
### Docker commands to bring up the containerised environment
After debugging Python source code in the code editor, they are ready to be built into docker images to be run as containers.
To build image at respective directories: 'server' and 'client' (refer to the directory structure above):
> docker build --no-cache -t server-image:latest . 
> docker build --no-cache -t client-image:latest .

To create a network bridge for containers to communicate:
> docker network create my_network

To run server container with attached terminal as the FIRST step:
> docker run -it --network my_network --name server-container server-image

To run client container in detached mode as the SECOND step:
> docker run -d --network my_network --name client-container client-image

### Unittest commands to run test modules under respective directories
To run unittest test modules using Python commands, run them at directory level 'prjASD' (refer to directory structure)
For unittest test module 'test_server.py':
> python -m unittest discover -s server/unit_tests

For unittest test module 'test_client.py':
> python -m unittest discover -s client/unit_tests 

For system test module 'test_system.py':
> python -m unittest discover -s system_tests

### application terminal command examples
Generic syntax: explore <client_id> <path>
> explore 172.18.0.3 /  ( private ip_address within docker network bridge showing root directory in container )


