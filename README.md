# ZFourLepAnalysis

This package allows you to create and analyze rootuples from NANOAOD for the Z(Z)->4l analysis

# How to compile and run
    cmsrel CMSSW_10_2_18
    cd CMSSW_10_2_18/src
    cmsenv
    git clone https://github.com/michaelmackenzie/ZFourLep.git StandardModel/ZFourLep
    git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
    scram b
  
This code runs on crab with the postprocessor given by nanoAOD-Tools

    cd StandardModel/ZFourLep/test
    <set the crab environment>
    python crab_config/multicrab_signal.py
  
 
 A basic analysis script is defined
    
    cd StandardModel/ZFourLep/ana
    xrdcp root://cmseos.fnal.gov//store/user/mmackenz/zfourlep/merged/ZFourLepAnalysis_merged.root ./
    root.exe zfourlep_ana.C
    
The output of the anaysis is histograms in `zfourlep_ana.root`
  
