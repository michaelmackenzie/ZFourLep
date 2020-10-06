import ROOT
import math

ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class exampleProducer(Module):
    def __init__(self,runningEra):
        self.runningEra = runningEra
        self.seen = 0
        self.accept = 0
        pass
    def beginJob(self):
        pass
    def endJob(self):
        print "Saw", self.seen, "events, accepted", self.accept, "events"
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("leptonOneFlavor"   , "I")
        self.out.branch("leptonOneIndex"    , "I")
        self.out.branch("leptonTwoFlavor"   , "I")
        self.out.branch("leptonTwoIndex"    , "I")
        self.out.branch("leptonThreeFlavor", "I")
        self.out.branch("leptonThreeIndex" , "I")
        self.out.branch("leptonFourFlavor"  , "I")
        self.out.branch("leptonFourIndex"   , "I")
        
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):

        verbose = 1
        self.seen = self.seen + 1
        
        """process event, return True (go to next module) or False (fail, go to next event)"""
        HLT       = Object(event, "HLT")
        electrons = Collection(event, "Electron")
        muons     = Collection(event, "Muon")
        taus      = Collection(event, "Tau")
        jets      = Collection(event, "Jet")
        PuppiMET  = Object(event, "PuppiMET")

        ## trigger parameter ##
        minmupt     = 25. # muon trigger
        minelept    = 33. # electron trigger
        if self.runningEra == 0 :
            minelept = 28. #lower pT trigger in 2016
        elif self.runningEra == 1 :
            minmupt = 28. #higher pT trigger in 2017

        ## Non-trigger lepton parameters ##
        minmuptlow  = 5.
        mineleptlow = 10.
        mintaupt = 20.
        
        ## jet parameters ##
        jetIdflag   = 1
        jetPUIdflag = 4


        ## muon isolation cut levels ##
        muonIsoVLoose  = 0.4
        muonIsoLoose   = 0.25 #eff ~ 0.98
        muonIsoMedium  = 0.20
        muonIsoTight   = 0.15 #eff ~ 0.95
        muonIsoVTight  = 0.10
        muonIsoVVTight = 0.05

        ## selection parameters ##
        maxMET      = -1. # < 0 to apply no cut
        maxJetPt    = -1. # < 0 to apply no cut

        # switch between tau IDs (deep NN IDs or old MVA IDs)
        useDeepNNTauIDs = True
        
        muonIso    = muonIsoTight
        muonId     = 3 #tight ID
        eleId      = 2 #WP80
        tauAntiEle = 1 # (bitmask) MVA: 8 = tight, 16 = very tight deepNN:  1 = VVVLoose 2 = VVLoose 4 = VLoose   8 = Loose
        #                                                                  16 = Medium  32 = Tight  64 = VTight 128 = VVTight
        tauAntiMu  = 10 # (bitmask) MVA: 1 = loose 2 = tight deepNN: 1 = VLoose 2 = Loose 4 = Medium 8 = Tight
        tauAntiJet = 50 # (bitmask) deepNN: 1 = VVVLoose 2 = VVLoose 4 = VLoose 8 = Loose 16 = Medium 32 = Tight 64 = VTight 128 = VVTight
        tauIso     = 7 
        tauDeltaR  = 0.3                
        tauIdDecay = True
        
        ### initial filtering ###
        if maxMET > 0 and PuppiMET.pt > maxMET : #cut high MET events
            return False

        ### check which triggers are fired ###
        muonTriggered = False
        electronTriggered = False
        if self.runningEra == 0 :
            if HLT.IsoMu24 or HLT.Mu50 :
                muonTriggered = True
            if HLT.Ele27_WPTight_Gsf :
                electronTriggered = True
        elif self.runningEra == 1 :
            if HLT.IsoMu27 or HLT.Mu50 :
                muonTriggered = True
            if HLT.Ele32_WPTight_Gsf_L1DoubleEG and HLT.Ele35_WPTight_GsF_L1EGMT : #seems to be recommended to use L1 seed of HLT_Ele35 as well
                electronTriggered = True
        elif self.runningEra == 2 :
            if HLT.IsoMu24 or HLT.Mu50 :
                muonTriggered = True
            if HLT.Ele32_WPTight_Gsf :
                electronTriggered = True
        if (verbose > 1 and self.seen % 100 == 0) or (verbose > 2 and self.seen % 10 == 0):
            print "muonTriggered =",muonTriggered,"electronTriggered =",electronTriggered
        #require a trigger
        if not muonTriggered and not electronTriggered :
            return False

        ################ count objects ####################
        nElectrons = 0
        nMuons = 0
        nTaus = 0
        elec_dict = dict() # save a dictionary to find the objects again
        muon_dict = dict()
        tau_dict = dict()
        for index in range(len(electrons)) :
            if(verbose > 9 and self.seen % 10 == 0):
                print "Electron", index, "pt =", electrons[index].pt, "WPL =", electrons[index].mvaFall17V2Iso_WPL, "WP80 =", electrons[index].mvaFall17V2Iso_WP80 
            if (electrons[index].pt > mineleptlow and
                ( eleId == 0 or
                  (eleId == 1 and electrons[index].mvaFall17V2Iso_WPL ) or
                  (eleId == 2 and electrons[index].mvaFall17V2Iso_WP80) or
                  (eleId == 3 and electrons[index].mvaFall17V2Iso_WP90))) :
                elec_dict[nElectrons] = index
                nElectrons = nElectrons + 1
        for index in range(len(muons)) :
            if(verbose > 9 and self.seen % 10 == 0):
                print "Muon", index, "pt =", muons[index].pt, "IDL =", muons[index].looseId, "IDM =", muons[index].tightId, "IDT =", muons[index].tightId, "iso = ", muons[index].pfRelIso04_all 
            if (muons[index].pt > minmuptlow and
                ((muonId == 1 and muons[index].looseId) or
                 (muonId == 2 and muons[index].mediumId) or
                 (muonId == 3 and muons[index].tightId)) and
                muons[index].pfRelIso04_all < muonIso) :
                muon_dict[nMuons] = index
                nMuons = nMuons + 1
        for index in range(len(taus)) :
            if(verbose > 9 and self.seen % 10 == 0):
                print "Tau", index, "pt =", taus[index].pt, "AntiMu =", taus[index].idDeepTau2017v2p1VSmu, "AntiEle =", taus[index].idDeepTau2017v2p1VSe, "AntiJet =", taus[index].idDeepTau2017v2p1VSjet
            if taus[index].pt > mintaupt and abs(taus[index].eta) < 2.3:
                if ((useDeepNNTauIDs and
                     taus[index].idDeepTau2017v2p1VSe >= tauAntiEle and
                     taus[index].idDeepTau2017v2p1VSmu >= tauAntiMu and
                     taus[index].idDeepTau2017v2p1VSjet >= tauAntiJet and
                     (taus[index].idDecayModeNewDMs or not tauIdDecay))
                    or (not useDeepNNTauIDs and
                        taus[index].idAntiEle >= tauAntiEle and
                        taus[index].idAntiMu >= tauAntiMu and
                        taus[index].idMVAnewDM2017v2 >= tauIso and
                        (taus[index].idDecayMode or not tauIdDecay))) :
                    deltaRCheck = True
                    if tauDeltaR > 0: #check for overlap with accepted lepton
                        for i_elec in range(nElectrons):
                            deltaRCheck = deltaRCheck and taus[index].p4().DeltaR(electrons[elec_dict[i_elec]].p4()) > tauDeltaR
                            if not deltaRCheck:
                                break
                        for i_muon in range(nMuons):
                            deltaRCheck = deltaRCheck and taus[index].p4().DeltaR(muons[muon_dict[i_muon]].p4()) > tauDeltaR
                            if not deltaRCheck:
                                break
                    if deltaRCheck:
                        tau_dict[nTaus] = index
                        nTaus = nTaus + 1

        if (verbose > 1 and self.seen % 100 == 0) or (verbose > 2 and self.seen % 10 == 0):
            print "seen",self.seen,"ntau (len) =",nTaus,"(", len(taus),") nelectron (len) =",nElectrons,"(", len(electrons),") nmuon (len) =",nMuons,"(",len(muons),") met =",PuppiMET.pt

        #no trigger-able leptons
        if nElectrons == 0 and not muonTriggered:
            return False
        if nMuons == 0 and not electronTriggered:
            return False
        if not (nTaus + nElectrons + nMuons == 4) :
            return False

        passTrigger = False
        if(muonTriggered and nMuons > 0) :
            for i_muon in range(nMuons) :
                passTrigger = passTrigger or muons[muon_dict[i_muon]].pt > minmupt
                if(passTrigger) :
                    break
        if(electronTriggered and not passTrigger and nElectrons > 0) :
            for i_electron in range(nElectrons) :
                passTrigger = passTrigger or electrons[elec_dict[i_electron]].pt > minelept
                if(passTrigger) :
                    break
        
                
        #Accept the event, store the lepton flavors and indices
        lepIndices = dict()
        lepFlavors = dict()
        index = 0
        for i in range(nElectrons) :
            lepIndices[index] = elec_dict[i]
            lepFlavors[index] = -11*electrons[elec_dict[i]].charge
            index = index + 1
        for i in range(nMuons) :
            lepIndices[index] = muon_dict[i]
            lepFlavors[index] = -13*muons[muon_dict[i]].charge
            index = index + 1
        for i in range(nTaus) :
            lepIndices[index] = tau_dict[i]
            lepFlavors[index] = -15*taus[tau_dict[i]].charge
            index = index + 1
        self.out.fillBranch("leptonOneFlavor"   , lepFlavors[0])
        self.out.fillBranch("leptonOneIndex"    , lepIndices[0])
        self.out.fillBranch("leptonTwoFlavor"   , lepFlavors[1])
        self.out.fillBranch("leptonTwoIndex"    , lepIndices[1])
        self.out.fillBranch("leptonThreeeFlavor", lepFlavors[2])
        self.out.fillBranch("leptonThreeeIndex" , lepIndices[2])
        self.out.fillBranch("leptonFourFlavor"  , lepFlavors[3])
        self.out.fillBranch("leptonFourIndex"   , lepIndices[3])
        
        self.accept = self.accept + 1
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
leptonConstr = lambda runningEra : exampleProducer(runningEra)
