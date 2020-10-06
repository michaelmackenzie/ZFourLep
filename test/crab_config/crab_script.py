#!/usr/bin/env python
import os
import sys

# for local testing
doLocal = False
# Take input parameters
isData = False
if sys.argv[2].split('=')[1] == "data":
    isData = True

year = sys.argv[3].split('=')[1]

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
if not doLocal :
    from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

from StandardModel.ZFourLep.runSkimModule import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *

if doLocal:
    # inputfile = ['/afs/cern.ch/user/p/pellicci/cernbox/ROOT/ZEMuAnalysis/NANOAOD/191120_10218V1/ZEMuAnalysis_pythia8_NANOAOD_2018_1.root']
    inputfile = ['/eos/uscms/store/user/mmackenz/LFVAnalysis_ZMuTau_2016_8028V1/LFVAnalysis_NANOAOD_8028V1/200716_213639/0000/ZEMuAnalysis_pythia8_NANOAOD_2016_1.root']
    # inputfile = ['/eos/uscms/store/user/mmackenz/LFVAnalysis_HEMu_2016_8028V1/LFVAnalysis_NANOAOD_8028V1/200708_163332/0000/ZEMuAnalysis_pythia8_NANOAOD_2016_1.root']
    # inputfile = ['/eos/uscms/store/user/mmackenz/LFVAnalysis_HMuTau_2016_8028V1/LFVAnalysis_NANOAOD_8028V1/200716_180028/0000/ZEMuAnalysis_pythia8_NANOAOD_2016_1.root']
    p=PostProcessor(".",inputfile,"",modules=[leptonConstr(0)],provenance=True,fwkJobReport=True,outputbranchsel="cmssw_config/keep_and_drop.txt")

else:
    if isData :
        if year == "2016" :
            p=PostProcessor(".",inputFiles(),modules=[leptonConstr(0)],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")
        elif year == "2017" :
            p=PostProcessor(".",inputFiles(),modules=[leptonConstr(1)],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")
        elif year == "2018" :
            p=PostProcessor(".",inputFiles(),modules=[leptonConstr(2)],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")
    else :
        if year == "2016" :
            p=PostProcessor(".",inputFiles(),modules=[leptonConstr(0),puAutoWeight_2016()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")
        elif year == "2017" :
            p=PostProcessor(".",inputFiles(),modules=[leptonConstr(1),puAutoWeight_2017()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")
        elif year == "2018" :
            p=PostProcessor(".",inputFiles(),modules=[leptonConstr(2),puAutoWeight_2018()],provenance=True,fwkJobReport=True,jsonInput=runsAndLumis(),outputbranchsel="cmssw_config/keep_and_drop.txt")

p.run()

print "DONE"
