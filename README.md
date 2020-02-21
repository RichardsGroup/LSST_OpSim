# LSST_OpSim 
The repo provides instructions, notebooks, and scripts to help people
getting started with testing LSST cadence simulations hosted on
[SciServer](http://www.sciserver.org/). This work was initiated to
encourage LSST AGN SC members to design and run metrics on simulated
LSST cadences, to enable selection of cadences that are best for AGN
science in LSST. However, since the data and notebooks are all public,
anyone interested in testing the cadences is welcome to use the tools
provided here within the infrastructure provided by the SciServer
team. This project is led by Weixiang Yu and Dr. Gordon Richards at
Drexel University, with extensive help from the SciServer team.

### Setup
The instructions on how to create an account on
[SciServer](http://www.sciserver.org/), create a container with the
necessary software installed and the cadence volume mounted can be
found in [sciserver_opsim.pdf](./sciserver_opsim.pdf)

### Getting Started
Once you have finished the setup, clone this repo to your "persistent"
folder. You can begin exploring the simulated cadences using the
notebooks and scripts provided here. We would suggest following the
order listed below:

- [Introduction.ipynb](./Scripts_NBs/Introduction.ipynb): A notebook providing a brief overview about how to use MAF.
- [Multiple_Opsims.ipynb](./Scripts_NBs/Multiple_Opsims.ipynb): A notebook showing how to run some metrics on multiple (all) opsims. 
- [View_Results.ipynb](./Scripts_NBs/View_Results.ipynb): A notebook showing how to read in the result produced in the notebook above.
- [wfdFootPrint.ipynb](./Scripts_NBs/wfdFootPrint.ipynb): A notebook showing how to use a custom healpix slicer to run metrics on WFD observations only. Since the Feature-based opsims no longer use fixed tiles, we have get WFD observations through some tricks. For more discussions on this topic, please see [this thread on LSST community.com](https://community.lsst.org/t/wfd-metrics-with-the-fbs-output/3970/7)

**Note:** The `opsimUtils.py` script must be kept in the same directory in which you want to run the notebooks.

Once you are a MAF pro, you can learn more about MAF from [sims_maf_contrib github repo](https://github.com/LSST-nonproject/sims_maf_contrib). For details on the most recent release of LSST cadence simulation, please refer to the [FBS_1.4 thread](https://community.lsst.org/t/january-2020-update-fbs-1-4-runs/4006/6) on LSST Community page. 


