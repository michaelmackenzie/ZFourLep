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

if runningEra == 0:
    config.JobType.scriptArgs = ['isData=MC','year=2016']
    config.General.workArea = 'crab_projects/samples_MC_2016/'
if runningEra == 1:
    config.JobType.scriptArgs = ['isData=MC','year=2017']
    config.General.workArea = 'crab_projects/samples_MC_2017/'
if runningEra == 2:
    config.JobType.scriptArgs = ['isData=MC','year=2018']
    config.General.workArea = 'crab_projects/samples_MC_2018/'


config.section_('Data')
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False
config.Data.outLFNDirBase = '/store/user/mimacken/zemu_nanoaod/'

config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'

if __name__ == '__main__':

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

    #################################################
    #                                               #
    #--------------- Running 2016 MC ---------------#
    #                                               #
    #################################################

    if runningEra == 0:

        config.General.requestName = '2016_ZEMuAnalysis_ttbarToSemiLeptonic'
        config.Data.inputDataset = '/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_ttbarlnu'
        config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2016_ZEMuAnalysis_SingleToptW'
        config.Data.inputDataset = '/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_SingleAntiToptW'
        config.Data.inputDataset = '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2016_ZEMuAnalysis_DY50'
        config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2016_ZEMuAnalysis_WW'
        config.Data.inputDataset = '/WWTo2L2Nu_13TeV-powheg/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2016_ZEMuAnalysis_WZ'
        config.Data.inputDataset = '/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2016_ZEMuAnalysis_Wlnu'
        config.Data.inputDataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2016_ZEMuAnalysis_WWW'
        config.Data.inputDataset = '/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()        

        config.General.requestName = '2016_ZEMuAnalysis_QCDDoubleEMEnrich30to40'
        config.Data.inputDataset = '/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2016_ZEMuAnalysis_QCDDoubleEMEnrich30toInf'
        config.Data.inputDataset = '/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2016_ZEMuAnalysis_QCDDoubleEMEnrich40toInf'
        config.Data.inputDataset = '/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2016_ZEMuAnalysis_ZZ'
        config.Data.inputDataset = '/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

    #################################################
    #                                               #
    #--------------- Running 2017 MC ---------------#
    #                                               #
    #################################################

    if runningEra == 1:

        config.General.requestName = '2017_ZEMuAnalysis_ttbarToSemiLeptonic'
        config.Data.inputDataset = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2017_ZEMuAnalysis_ttbarlnu'
        config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2017_ZEMuAnalysis_SingleToptW'
        config.Data.inputDataset = '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2017_ZEMuAnalysis_SingleAntiToptW'
        config.Data.inputDataset = '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2017_ZEMuAnalysis_DY50'
        config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext3-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2017_ZEMuAnalysis_WW'
        config.Data.inputDataset = '/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2017_ZEMuAnalysis_WZ'
        config.Data.inputDataset = '/WZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2017_ZEMuAnalysis_Wlnu'
        config.Data.inputDataset = '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2017_ZEMuAnalysis_WWW'
        config.Data.inputDataset = '/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2017_ZEMuAnalysis_QCDDoubleEMEnrich30to40'
        config.Data.inputDataset = '/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2017_ZEMuAnalysis_QCDDoubleEMEnrich30toInf'
        config.Data.inputDataset = '/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2017_ZEMuAnalysis_QCDDoubleEMEnrich40toInf'
        config.Data.inputDataset = '/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2017_ZEMuAnalysis_ZZ'
        config.Data.inputDataset = '/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

    #################################################
    #                                               #
    #--------------- Running 2018 MC ---------------#
    #                                               #
    #################################################


    if runningEra == 2:

        config.General.requestName = '2018_ZEMuAnalysis_ttbarToSemiLeptonic'
        config.Data.inputDataset = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext3-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_ttbarlnu'
        config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_SingleToptW'
        config.Data.inputDataset = '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2018_ZEMuAnalysis_SingleAntiToptW'
        config.Data.inputDataset = '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
        
        config.General.requestName = '2018_ZEMuAnalysis_DY50'
        config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_WW'
        config.Data.inputDataset = '/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_WZ'
        config.Data.inputDataset = '/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_Wlnu'
        config.Data.inputDataset = '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_WWW'
        config.Data.inputDataset = '/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_QCDDoubleEMEnrich30toInf'
        config.Data.inputDataset = '/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_QCDDoubleEMEnrich40toInf'
        config.Data.inputDataset = '/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

        config.General.requestName = '2018_ZEMuAnalysis_ZZ'
        config.Data.inputDataset = '/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM'
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()
