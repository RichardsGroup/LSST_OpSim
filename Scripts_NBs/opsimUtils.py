import glob
import os

# import lsst.sims.maf python modules
import lsst.sims.maf.db as db
import lsst.sims.maf.metrics as metrics
import lsst.sims.maf.slicers as slicers
import lsst.sims.maf.stackers as stackers
import lsst.sims.maf.plots as plots
import lsst.sims.maf.metricBundles as metricBundles


def show_opsims(dbDir):
    '''Show available opsim databases in the provided directory.'''

    dbDir = os.path.abspath(dbDir)
    db_list = glob.glob(dbDir+'/*.db')
    runNames = [os.path.basename(x) for x in db_list]

    return runNames


def connect_dbs(dbDir, outDir):
    """
    Initiate database objects to all opSim databases in the provided directory.
    Returns a dictionary consisting all database connections and a dictionary holding
    the resultsDb objects.
    """
    opSimDbs = {}
    resultDbs = {}
    dbDir = os.path.abspath(dbDir)
    db_list = glob.glob(dbDir+'/*.db')

    for dbPath in db_list:
        dbName = os.path.basename(dbPath)
        opSimDbs[os.path.splitext(dbName)[0]] = db.OpsimDatabase(dbPath)
        resultDbs[os.path.splitext(dbName)[0]] = db.ResultsDb(outDir=outDir,
                                                              database=os.path.splitext(dbName)[0]+'_result.db')
    return (opSimDbs, resultDbs)


def getResultsDbs(resultDbPath):
    """Create a dictionary of resultDb from paths"""

    resultDbs = {}
    resultDbList = glob.glob(os.path.join(resultDbPath, '*_result.db'))
    for resultDb in resultDbList:
        runName = os.path.basename(resultDb).rsplit('_', 1)[0]
        resultDbs[runName] = db.ResultsDb(database=resultDb)
    return resultDbs


def bundleDictFromDisk(resultDb, runName, metricDataPath):
    """
    Read metric data from disk and import them into metricBundles.
    """

    bundleDict = {}
    displayInfo = resultDb.getMetricDisplayInfo()
    for item in displayInfo:
        metricName = item['metricName']
        metricFileName = item['metricDataFile']
        newbundle = metricBundles.createEmptyMetricBundle()
        newbundle.read(os.path.join(metricDataPath, metricFileName))
        newbundle.setRunName(runName)

        bundleDict[metricName] = newbundle
    return bundleDict


def getSummary(resultDbs, metricName, summaryStatName, **kwargs):
    '''
    Return one summary statstic for all opsims on a particualr metric given some constraints.

    Args:
        resultDbs(dict): A dictionary of resultDb, keys are run names.
        metricName(str): The name of the metric to get summary statistic for.
        summaryStatName(str): The name of the summary statistic get (e.g., Median)

    Returns:
        stats(dict): Each element is a list of summary stats for the corresponding 
            opSim run indicated by the key. This list could has a size > 1, given 
            that we can run one metric with different sql constraints.  
    '''
    stats = {}
    for run in resultDbs:
        mIds = resultDbs[run].getMetricId(metricName=metricName, **kwargs)
        stats[run] = resultDbs[run].getSummaryStats(
            mIds, summaryName=summaryStatName)
    return stats


def plotSummaryBar(resultDbs, metricName, summaryStatName, **kwargs):
    '''
    Generate bar plot using summary statistics for comparison between opSims.

    Args:
        resultDbs(dict): A dictionary of resultDb, keys are run names.
        metricName(str): The name of the metric to get summary statistic for.
        summaryStatName(str): The name of the summary statistic get (e.g., Median)
    '''
    stats = getSummary(resultDbs, metricName, summaryStatName, **kwargs)

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    runNames = list(resultDbs.keys())
    summaryValues = []
    for key in stats:
        summaryValues.append(stats[key]['summaryValue'][0])
    ax.bar(runNames, summaryValues)
    plt.xticks(rotation=80)
    plt.title('Bar Chart for Summary Stat: {} of Metric: {}'.format(
        summaryStatName, metricName))
    plt.ylabel('Summary Values')


def plotHist(bundleDicts, metricName):
    '''
    Plot histogram of evaluated metrics for all opSims on one figure.

    Args:
        bundleDicts(dict): A dictionary of bundleDict, keys are run names.
        metricName(str): The metric to plot histograms for.
    '''
    # init handler
    ph = plots.PlotHandler(savefig=False)

    # init plot
    healpixhist = plots.HealpixHistogram()
    plotDictTemp = {'figsize': (8, 6), 'fontsize': 15, 'labelsize': 13}
    plotDicts = []
    bundleList = []

    for runName in bundleDicts:
        plotDict = plotDictTemp.copy()
        plotDict.update({'label': runName})
        plotDicts.append(plotDict)
        bundleList.append(bundleDicts[runName][metricName])

    # set metrics to plot togehter
    ph.setMetricBundles(bundleList)
    ph.plot(plotFunc=healpixhist, plotDicts=plotDicts)


def plotSky(bundleDicts, metricName):
    '''
    Plot healpix skymap for each opSim given a metric. One figure per opSim.

    Args:
        bundleDicts(dict): A dictionary of bundleDict, keys are run names.
        metricName(str): The metric to plot histograms for.
    '''

    healpixSky = plots.HealpixSkyMap()
    for run in bundleDicts:
        bundleDicts[run][metricName].plot(plotFunc=healpixSky, savefig=False)
