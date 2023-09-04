<div align="center">
  <img src="pics/logo.jpg" alt="Logo Pic" width="1000" height="250"/>
  <h1>👨‍💻 Modbus Protocol Data Injection Project 💻</h1>
  <p>Exploiting Modbus protocol vulnerabilities with a focus on data integrity and ethical principles</p>
</div>

---

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Modbus Protocol](#modbus-protocol)
- [Exfiltration Techniques](#exfiltration-techniques)
- [Project Objectives](#project-objectives)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Creating a pcap](#creating-a-pcap)
  - [Investigating the Protocol](#investigating-the-protocol)
  - [Demonstration Video](#demonstration-video)
- [License](#license)

## Introduction

This README provides an overview of the Modbus Protocol Data Exfiltration Project. The project focuses on successfully exfiltrating sensitive information from a critical facility while avoiding suspicion and notifications in the Human-Machine Interface (HMI).

## Project Overview

- Modbus TCP is a widely used communication protocol in industrial automation and control systems, facilitating seamless data exchange over Ethernet networks.
- The project explores the Modbus communication protocol, which involves query/response (master/slave) and broadcast methods.
- Exfiltration techniques are employed to manipulate Modbus packets while maintaining data integrity and avoiding errors.

## Modbus Protocol

- Modbus communication involves query/response frames, comprising recipient addresses, commands, and data.
- The master-slave technique is used, with the master initiating queries and slaves responding.
- Slaves are external devices processing and sending data to the master.

## Exfiltration Techniques

### "Rocks otorio" (50 times)

- This task involves modifying Modbus packets to exfiltrate data while avoiding errors.
- Adjustments are made to the fields' length and byte count to align with updated data.

### Leaking a Cat Picture

- This task involves modifying packets to exfiltrate an image.
- The image is segmented into portions matching the protocol's prescribed length and byte count fields.
- Fields' length and byte count are precisely adjusted to match the updated data.

## Project Objectives

The primary objectives of this project include:
- Demonstrating successful data exfiltration from a critical facility.
- Evading suspicion and alerts in the Human-Machine Interface (HMI).
- Maintaining data integrity while skillfully manipulating Modbus packets.

## Getting Started

### Prerequisites

Before starting, ensure you have the following prerequisites:
- [List any necessary software, hardware, or permissions here.]


### Installation

1. Clone this repository to your local machine:

 ```sh
   git clone https://github.com/annapinchuk/Otorio_task.git
 ```

3. [Include any specific installation instructions here.]

## Usage

### Creating a pcap

[Explain how to create a pcap file using your project.]

### Investigating the Protocol

[Provide instructions on how to investigate the Modbus protocol using your project.]

### Demonstration Video

Watch the project in action by viewing our [demonstration video](https://clipchamp.com/watch/Q5udOQY7X2p).

## License

[Specify the license under which your project is distributed.]
