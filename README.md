# LSST_OpSim
### << **This branch is archived. The `rubin_sim` branch is not the default.** <<

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

- [Introduction.ipynb](./Scripts_NBs/00_Introduction.ipynb): A notebook providing a brief overview about how to use MAF.
- [Multiple_Opsims.ipynb](./Scripts_NBs/01_Multiple_Opsims.ipynb): A notebook showing how to run some metrics on multiple (all) opsims. 
- [View_Results.ipynb](./Scripts_NBs/02_View_Results.ipynb): A notebook showing how to read in the result produced in the notebook above.
- [wfdFootPrint.ipynb](./Scripts_NBs/04_wfdFootPrint.ipynb): A notebook showing how to use a custom healpix slicer to run metrics on WFD observations only. Since the Feature-based opsims no longer use fixed tiles, we have get WFD observations through some tricks. For more discussions on this topic, please see [this thread on LSST community.com](https://community.lsst.org/t/wfd-metrics-with-the-fbs-output/3970/7)
- [DDF_Other_FootPrint.ipynb](./Scripts_NBs/03_DDF_Other_FootPrint.ipynb): A notebook showing how to run metrics on DDF only or areas that are outside DDF and WFD.

**Note:** The `opsimUtils.py` script must be kept in the same directory in which you want to run the notebooks.

Once you are a MAF pro, you can learn more about MAF from [sims_maf_contrib github repo](https://github.com/LSST-nonproject/sims_maf_contrib). For details on the most recent release of LSST cadence simulation, please refer to the [FBS_1.4 thread](https://community.lsst.org/t/january-2020-update-fbs-1-4-runs/4006/6), [FBS_1.5 thread](https://community.lsst.org/t/may-update-bonus-fbs-1-5-release/4139), [FBS_1.6 thread](https://community.lsst.org/t/fbs-1-6-release-august-2020/4423) and [FBS_1.7 thread](https://community.lsst.org/t/survey-simulations-v1-7-release-january-2021/4660) on LSST Community page. (Note that FBS 1.4 simulations have been superceded by runs in 1.5, 1.6 or 1.7, the link above is only for reference purpose.)

__Other useful resources:__
- A [summary/cheetsheet](https://github.com/lsst-pst/pstn-051/blob/master/Cheat_Sheet.md) (by Lynne Jones) of cadence simulations that are currently available.
- Columns in the OpSim databas -> [here](https://github.com/lsst/sims_featureScheduler)
- A high-level comparison/description of various simulation groups/families (across FBS 1.5, 1.6 and 1.7)-> [here](https://github.com/lsst-pst/survey_strategy/blob/master/fbs_1.7/SummaryInfo.ipynb)

<br>

__Pro tip:__ If you have already walked through all of the notebooks provided above and realize 
that some code might take forever to run, you can experiment with the SciServer Jobs 
(which can give you the access to more computing power and memory), here is how to 
do it -> [SciServer_Jobs](./SciServer_Jobs.pdf). 
