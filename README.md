# ZEMuAnalysis

This package allows you to create and analyze rootuples from NANOAOD for the Z->emu analysis

# How to compile and run
    cmsrel CMSSW_10_2_18
    cd CMSSW_10_2_18/src
    cmsenv
    git checkout https://github.com/pellicci/ZEMuAnalysis.git StandardModel/ZEMuAnalysis
    git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
    scram b
  
This code runs on crab with the postprocessor given by nanoAOD-Tools

    cd StandardModel/ZEMuAnalysis/test
    <set the crab environment>
    python crab_config/multicrab_data.py
  
  
