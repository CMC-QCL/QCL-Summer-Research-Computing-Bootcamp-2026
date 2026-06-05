## Getting Ready for Hands-On

First of all, you will add your public key to the Laguna user portal. This is to get ready for hands-on activities using Laguna's shell (command line) interface.

1. Open Terminal (Mac) or Windows Subsystem for Linux (Windows)
2. Generate an RSA key pair:

   <code>ssh-keygen -t rsa -b 4096</code>

3. Open your public key, id_rsa.pub from ~/.ssh folder.
4. Log in to the Laguna User Portal.
5. Open the User Profile page.
6. Copy and paste the public key in to the Public SSH Key (Regional cluster users only) field.

  _Note that it may take 1 to 2 hours to get the public key updated to your account_

### Data Encryption and Decryption

<img width="824" height="275" alt="image" src="https://github.com/user-attachments/assets/c41f8b2d-4690-419e-a160-3a9932e6acc7" />


## Introduction: HPC Resources (20 min)
Students may need high-performance computing (HPC) resources when their research or coursework involves computational tasks that exceed the capacity of a regular laptop or desktop. For example, if you’re analyzing or loading a 1–5 GB dataset in-memory (e.g., with pandas in Python), you may hit memory limits. Some empirical tests show pandas can use 2×–4× the memory compared to raw CSV size.

               ┌──────────────────────────────┐
               │ Do you work with large data? │
               │ (>1 GB or slow to process)   │
               └─────────────┬────────────────┘
                             │Yes
                             ▼
               ┌─────────────────────────────┐
               │ Does your code take >1 hour │
               │ or need many iterations?    │
               └─────────────┬───────────────┘
                             │Yes
                             ▼
               ┌─────────────────────────────┐
               │ Are you using ML, AI,       │
               │ simulations, or GPUs?       │
               └─────────────┬───────────────┘
                             │Yes
                             ▼
               ┌─────────────────────────────┐
               │      Request HPC Access     │
               └─────────────────────────────┘
                             │
                             ▼
           ┌────────────────────────────────────────────┐
           │ If no to any: Can your work finish         │
           │ faster, more efficiently, or more robustly │
           │ on HPC?                                    │
           └─────────────┬────────────────────────┬─────┘
                         │Yes                     │No
                         ▼                        ▼
           ┌──────────────────────────┐     ┌──────────────────────┐
           │     Consider HPC         │     │  Regular Computer OK │
           └──────────────────────────┘     └──────────────────────┘

- Local HPC: [QCL GPU and Dell Server] [QCL Computing Resources](https://www.cmc.edu/qcl/computational-resources)
- Regional HPC Cluster: USC Laguna - https://uschpc.github.io/regional-computing-website/ (Slide #1)
- National Supercomputers: [ACCESS](https://github.com/CMC-QCL/HPC-research-computing/blob/main/Introduction.md#national-supercomputers-access)

### HPC Structure (10 min)
<img width="1125" height="718" alt="image" src="https://github.com/user-attachments/assets/137f86b6-495d-4226-8959-0dd06eb8ff73" />


### What is ACCESS?
ACCESS is the NSF Advanced Cyberinfrastructure Coordination Ecosystem:
Services & Support.
ACCESS is the follow-up program to NSF’s Extreme Science and Engineering
Discovery Environment (XSEDE).
ACCESS aims to be a center point for making use of NSF-funded computational,
storage, and network resources for the U.S. national cyberinfrastrucutre research
ecosystem.

### ACCESS User Interfaces (aka Portals) include:

- Allocations Support: awards time on cyberinfrastructure
- User Support: answers user questions/tickets, provides documentation, works directly with researchers
- Operations Support: helps with user account creation/ management, login to/access to cyberinfrastructure
- Monitoring/Accounting Support: tracks and reports on usage – e.g., by project or by resource
  
### What is an Allocation?
An Allocation Request is a proposal in which
you describe:

- Project Title and Abstract
- Project Category (Explore, Discover, Accelerate, Maximize)
- The number of Credits you wish to request for your project

An Allocation is an active Allocation Request

### Understanding the Systems You Can Use
LAGUNA Cluster system spec
- 16 compute nodes (128 cores, 365 GB/node)
- 8 GPU nodes (2× NVIDIA L40S, 735 GB/node)
- Storage: 100 GB/user, 5 TB/project (+5 TB on request)
- 1 login node

SDSC Expanse system spec
- 728 compute nodes (128 cores/node)
- 52 GPU nodes (4× V100 GPUs/node)
- 93K+ CPU cores, 200+ GPUs
- ~247 TB memory, 19 PB storage
- High-speed InfiniBand network
  
## How to get started with the Laguna cluster (10 min)
To get allocations from Laguna, your faculty advisor and you will be working together for the following steps.

1. Your professor (Principal Investigator, PI) requests a PI account and project on Laguna: Contact local administrator (qcl@cmc.edu) or submit a ticket to laguna-support@usc.edu to request access to Laguna. USC's CARC team will send PI a Google form to collect information for research.
2. Once USC CARC approves and provisions a PI account, PI can access the user portal at https://hpcaccount.usc.edu/
3. PI cretes a new project in the user portal if it has not created. 
4. Research Assistants find the EPPN value from https://hpcaccount.usc.edu/static/secure/incommon.php (this is your Laguna user name.)
5. PI adds student (Research Assistnat, RA) accounts to the project in the Project page.
6. Once USC CARC provisions RA accounts, RAs can access the user portal as well.
  
## (Remote) Research Computing Workflow
The workflow for using Laguna typically consists of the following steps:

1. Connecting to the Internet
2. Logging in to the Laguna login node
3. Organizing files
4. Transferring files
5. Installing and running software
6. Testing your job interactively on a compute node
7. Submitting your job to the job scheduler to run it remotely on a compute node
8. Monitoring your job and checking the results when it has completed


## Prerequisites for Laguna (30 min and break)
All participants should login and check their user account on the Laguna cluster.

- CARC Accoount and EPPN (user name)
 https://uschpc.github.io/regional-computing-website/user-guides/get-started-laguna.html
- Check if everybody has access SSH +OOD
  - verify key (add manually)

## Interactive Computing (30 min)
- OnDemand Apps: JupyterLab, RStudio, Code Server.
- Web Interface: [https://www.carc.usc.edu/user-guides/carc-ondemand/ondemand-overview](https://uschpc.github.io/regional-computing-website/user-guides/get-started-laguna/laguna-ondemand.html)
- Interactive Session via Shell

## Computing Environment (20 min) Repdoducibility in mind
- modules
- virtual environment (conda)
- Advanced use such as Shell, container/docker, cron jobs, etc.

## Batch Computing (30 min)
- OnDemand Job Composer
- Shell Script
- SLURM

## Data Management (30 min)
- Data Storages
- Data Transfer
https://uschpc.github.io/regional-computing-website/user-guides/get-started-laguna/file-systems-overview
