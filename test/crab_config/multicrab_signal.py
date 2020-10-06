from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config
from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_config/crab_script.sh'
config.JobType.inputFiles = ['crab_config/crab_script.py','../scripts/haddnano.py','cmssw_config/keep_and_drop.txt']
config.JobType.sendPythonFolder	 = True
config.JobType.maxJobRuntimeMin = 2000 #2750 guaranteed by crab

config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False
# config.Data.outputDatasetTag = None
config.Data.outLFNDirBase = '/store/user/mimacken/zfourlep/'

config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC' # Choose your site. 

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

    ################### 2016 Samples #########################

    ##### Z samples #####
    
    config.JobType.scriptArgs = ['isData=MC','year=2016']
    config.General.workArea = 'crab_projects/samples_MC_2016/'
    config.General.requestName = '2016_ZFourLepAnalysis_Signal'
    config.Data.inputDataset = '/ZZTo4L_13TeV_powheg_pythia8_ext1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM'
    crabCommand('submit', config = config)

    # config.JobType.scriptArgs = ['isData=MC','year=2016']
    # config.General.workArea = 'crab_projects/samples_MC_2016/'
    # config.General.requestName = '2016_LFVAnalysis_ZETau'
    # config.Data.inputDataset =  '/LFVAnalysis_ZETau_2016_8028V1/mimacken-LFVAnalysis_NANOAOD_8028V1-d11e799790792310589ef5ee63b17d7a/USER'
    # p = Process(target=submit, args=(config,))
    # p.start()
    # p.join()

