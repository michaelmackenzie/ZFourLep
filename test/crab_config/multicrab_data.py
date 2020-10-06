from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config
from WMCore.Configuration import Configuration
config = Configuration()

runningEra = 0 # 0 = 2016, 1 = 2017, 2 = 2018

config.section_('General')
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_config/crab_script.sh'
config.JobType.inputFiles = ['crab_config/crab_script.py','../scripts/haddnano.py','cmssw_config/keep_and_drop.txt']
config.JobType.sendPythonFolder	 = True

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')

if runningEra == 0:
    config.General.workArea = 'crab_projects/samples_data_2016/'
    config.JobType.scriptArgs = ['isData=data','year=2016']
    config.Data.lumiMask = 'json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'

if runningEra == 1:
    config.General.workArea = 'crab_projects/samples_data_2017/'
    config.JobType.scriptArgs = ['isData=data','year=2017']
    config.Data.lumiMask = 'json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'

if runningEra == 2:
    config.General.workArea = 'crab_projects/samples_data_2018/'
    config.JobType.scriptArgs = ['isData=data','year=2018']
    config.Data.lumiMask = 'json/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt'

config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False
config.Data.outLFNDirBase = '/store/user/mimacken/zemu_nanoaod/'

config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC' # Choose your site. 
config.Site.blacklist = ['T2_DE_DESY']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    from multiprocessing import Process

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    #First the muon datasets


    ################################################
    #                                              #
    #----------------- Muons 2016 -----------------#
    #                                              #
    ################################################

    if runningEra == 0:

        config.General.requestName = '2016_ZEMuAnalysis_SingleMu_B'
        config.Data.inputDataset = '/SingleMuon/Run2016B-02Apr2020_ver2-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_SingleMu_C'
        config.Data.inputDataset = '/SingleMuon/Run2016C-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_SingleMu_D'
        config.Data.inputDataset = '/SingleMuon/Run2016D-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_SingleMu_E'
        config.Data.inputDataset = '/SingleMuon/Run2016E-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_SingleMu_F'
        config.Data.inputDataset = '/SingleMuon/Run2016F-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_SingleMu_G'
        config.Data.inputDataset = '/SingleMuon/Run2016G-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_SingleMu_H'
        config.Data.inputDataset = '/SingleMuon/Run2016H-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()


    ################################################
    #                                              #
    #----------------- Muons 2017 -----------------#
    #                                              #
    ################################################

    if runningEra == 1:

        config.General.requestName = '2017_ZEMuAnalysis_SingleMu_B'
        config.Data.inputDataset = '/SingleMuon/Run2017B-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2017_ZEMuAnalysis_SingleMu_C'
        config.Data.inputDataset = '/SingleMuon/Run2017C-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2017_ZEMuAnalysis_SingleMu_D'
        config.Data.inputDataset = '/SingleMuon/Run2017D-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2017_ZEMuAnalysis_SingleMu_E'
        config.Data.inputDataset = '/SingleMuon/Run2017E-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2017_ZEMuAnalysis_SingleMu_F'
        config.Data.inputDataset = '/SingleMuon/Run2017F-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        """

        config.General.requestName = '2017_ZEMuAnalysis_SingleMu_B'
        config.Data.inputDataset = '/SingleMuon/Run2017B-UL2017_02Dec2019-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2017_ZEMuAnalysis_SingleMu_C'
        config.Data.inputDataset = '/SingleMuon/Run2017C-UL2017_02Dec2019-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2017_ZEMuAnalysis_SingleMu_D'
        config.Data.inputDataset = '/SingleMuon/Run2017D-UL2017_02Dec2019-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2017_ZEMuAnalysis_SingleMu_E'
        config.Data.inputDataset = '/SingleMuon/Run2017E-UL2017_02Dec2019-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2017_ZEMuAnalysis_SingleMu_F'
        config.Data.inputDataset = '/SingleMuon/Run2017F-UL2017_02Dec2019-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        """

    ################################################
    #                                              #
    #----------------- Muons 2018 -----------------#
    #                                              #
    ################################################

    if runningEra == 2: 

        config.General.requestName = '2018_ZEMuAnalysis_SingleMu_A'
        config.Data.inputDataset = '/SingleMuon/Run2018A-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_SingleMu_B'
        config.Data.inputDataset = '/SingleMuon/Run2018B-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_SingleMu_C'
        config.Data.inputDataset = '/SingleMuon/Run2018C-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        #Muons 2018 - Era D
        config.General.requestName = '2018_ZEMuAnalysis_SingleMu_D'
        config.Data.inputDataset = '/SingleMuon/Run2018D-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()


    ################################################
    #                                              #
    #--------------- Electrons 2016 ---------------#
    #                                              #
    ################################################

    if runningEra == 0:

        config.General.requestName = '2016_ZEMuAnalysis_SingleEle_B'
        config.Data.inputDataset = '/SingleElectron/Run2016B-02Apr2020_ver2-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_SingleEle_C'
        config.Data.inputDataset = '/SingleElectron/Run2016C-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_SingleEle_D'
        config.Data.inputDataset = '/SingleElectron/Run2016D-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_SingleEle_E'
        config.Data.inputDataset = '/SingleElectron/Run2016E-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_SingleEle_F'
        config.Data.inputDataset = '/SingleElectron/Run2016F-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_SingleEle_G'
        config.Data.inputDataset = '/SingleElectron/Run2016G-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_SingleEle_H'
        config.Data.inputDataset = '/SingleElectron/Run2016H-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()


    ################################################
    #                                              #
    #--------------- Electrons 2017 ---------------#
    #                                              #
    ################################################

    if runningEra == 1:

        config.General.requestName = '2017_ZEMuAnalysis_SingleEle_B'
        config.Data.inputDataset = '/SingleElectron/Run2017B-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2017_ZEMuAnalysis_SingleEle_C'
        config.Data.inputDataset = '/SingleElectron/Run2017C-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2017_ZEMuAnalysis_SingleEle_D'
        config.Data.inputDataset = '/SingleElectron/Run2017D-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2017_ZEMuAnalysis_SingleEle_E'
        config.Data.inputDataset = '/SingleElectron/Run2017E-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2017_ZEMuAnalysis_SingleEle_F'
        config.Data.inputDataset = '/SingleElectron/Run2017F-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()


    ################################################
    #                                              #
    #--------------- Electrons 2018 ---------------#
    #                                              #
    ################################################

    if runningEra == 2: 

        config.General.requestName = '2018_ZEMuAnalysis_SingleEle_A'
        config.Data.inputDataset = '/EGamma/Run2018A-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_SingleEle_B'
        config.Data.inputDataset = '/EGamma/Run2018B-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_SingleEle_C'
        config.Data.inputDataset = '/EGamma/Run2018C-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        #Electrons 2018 - Era D
        config.General.requestName = '2018_ZEMuAnalysis_SingleEle_D'
        config.Data.inputDataset = '/EGamma/Run2018D-02Apr2020-v1/NANOAOD'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
