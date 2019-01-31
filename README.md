Auditing for HW as a Service Cloud Project Proposal
===

## Description
At MOC (https://massopen.cloud/) we have a cloud management service known as HIL (https://github.com/CCI-MOC/hil) which provides network isolation. HIL makes changes to network switches to isolate networks and updates its internal database. The Auditing Service will query switch state and then the state of the HIL database and make sure both are the same. Any discrepancies can be immediately detected to make sure isolation is not compromised.

## Background
### Bare Metal Clouds
The use of bare metal clouds is increasing due to a number of factors. Bare metal clouds do not have a huge trusted computing base as the traditional virtualization based clouds, which leads to a smaller attack surface. Since tenants don't have to share machines or networks, this allows for improved security and privacy, as well as network performance guarantees which allows for consistent service and better operations. Mass Open Cloud (MOC) is an example of a bare metal cloud. With the adoption of bare metal clouds, their orchestration or management has become paramount so tenants can easily increase or decrease the number of nodes they use based on demand. Tenants also require network isolation to be simple in order to create or remove networks as needed.

### HIL
Hardware Isolation Layer (HIL) is one of the cloud management services, and is in use at production level in the MOC. HIL is a lightweight exokernel layer for the cloud which makes allocation of nodes and networks extremely easy. Tenants can use HIL to get free nodes and connect these nodes into isolated networks. VLANs is one of the ways in which HIL can implement isolation using commodity network switches. HIL works through a REST API and operates on behalf of the cloud provider, servicing tenant requests by making changes to network switches. HIL also has an internal database which keeps track of nodes and networks. At this time HIL’s database only reflects the actual state of network switches if there is no outside interaction by cloud providers or network administrator.

### Need for an Auditing Service
HIL’s operations can be compromised if the internal database and switch state do not match. There can be multiple reasons for this. A network administrator might update or change the network switch out of band and forget to update HIL. Or a malicious entity or network administrator can change the network switch state on purpose. Since HIL doesn’t constantly poll the network state (this would add network congestion), it becomes extremely hard for it to detect such discrepancies. Even if everything runs smooth, a tenant still has to trust HIL for complete isolation and no unauthorized nodes are attached to the network. There must be a service which can detect and report any discrepancy in the HIL database and network switch state. This is why the auditing service is necessary for the current MOC cloud infrastructure.

## Why is this important?
From the point of view of a network administrator, is it important that errors can be detected easily and instantly. Without an auditing service, the admin may have to spend hours troubleshooting. From the point of view of a tenant, it is critical that isolation is provided, and there is a way for the tenant to verify private network isolation. The auditing service will execute these important features.

## Vision and Goals Of The Project:
This project intends to do the following.
1. Create an Auditing Service totally independent of HIL which can query network switches and the HIL database.
2. Make a REST API for easy use of the service.
3. Make the least number of changes to HIL in order to export the internal database to the Auditing Service or find another way to do that.
4. Allow the auditing service to run in a privileged mode so it can query the network switches but with a read-only access. This way the Auditing Service won’t be used as a corrective mechanism (HIL is there to do that), just a reporting solution.
5. Create a general architecture which might also be used with cloud management services other than HIL through different implementations.
Other goals will be added to this list as scope becomes more clear.

## Users/Personas Of The Project:
We envision two main users for the Auditing Service.
1. Cloud administrators - for troubleshooting purposes.
2. Tenants - for guarantee of isolation purposes.

## Solution Concept:
![HIL plus Auditing Block Diagram](/ReadmeImage.jpg)

1. REST API based service
    1. Base layer of the system will list all functionality of the REST API.
        1. Using base layer, all functionality will be implemented here.
            1. Connect to network switches using appropriate “read-only” credentials
            2. Poll switch configuration and maintain a short term database of information.
            3. Send data back to user with requested information
        2. Future / Long term goals
            1. Have a on going service which performs checks on network switch for mismatched information
            2. Notify users of altered isolated network automatically
2. CLI interface
    1. Create a simple CLI interface using REST calls to perform user tasks.
    2. Mainly used for debug purposes and simple testing of main code during development

## Minimum Viable Product:
### Description

The first iteration of the design will contain a simple current state information tracking and reporting. This can be useful for a user which wants to check if the HIL database is up to date with the current state of the switch. This also gives us a base product to demonstrate all the functionality that can be reported by an audit system.

### Back-end (Base layer - Python)

This will be the layer which contains the functions of communicating with the network switches and HIL database. Information will be obtained by a user through the use of a REST API which allows for an easy method of accessing this data.

#### Network functions

* Most of this code will be reused from the HIL source code available
* Basic functions will include polling the switch for parameters about all clients connected to the system and maintaining a database of the current state before sending this information to the user.
* The network driver should have an abstract class with function headers
    * The functions should be generic and listed in API for future use
    * The abstract class is useful to adapt any network switch driver to function with audit system
    * Currently we are planning to have functionality for Open vSwitch, Dell Powerconnect 5500, and Brocade (Taken from HIL)

#### REST API

* Well defined API for using REST calls
* All user functions will be processed through REST calls (no outside calls)

### CLI

* Created to use REST calls as communication to user
* Must contain 'help' section to teach about how to use CLI

#### Solution Concept:
![MVP Workflow from Sprint 3 presentation](/MVP_Workflow_diagram.png)

## Acceptance criteria
The auditing service should at minimum allow for manual calls to verify the HIL database against the states of the network switches. Once this feature is implemented, there are services like crontab for automation that may be feasible for small scale projects. Automation of this process is a secondary concern, but will still be important to include for the future development of this application.

The first CLI interface will be mandatory for interacting with the Auditing Service within the local machine.



#### Client Database to check changes on HIL

In the new_hil folder, run hil_update_checker.py on the background to query hil non-stop, this will pull the information regarding changes in your local DB, and run check_hil.py to see your local DB



