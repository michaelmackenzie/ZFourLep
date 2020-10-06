
  
enum {kMaxParticles = 30};
struct Tree_t {
  UInt_t nElectron;
  Float_t ElectronDeltaEtaSC[kMaxParticles];
  Float_t ElectronEta[kMaxParticles];
  Float_t ElectronPt[kMaxParticles];
  Float_t ElectronPhi[kMaxParticles];
  Float_t ElectronMass[kMaxParticles];
  Bool_t  ElectronWP80[kMaxParticles];
  Int_t   ElectronQ[kMaxParticles];
  
  UInt_t nMuon;
  Float_t MuonEta[kMaxParticles];
  Float_t MuonPt[kMaxParticles];
  Float_t MuonPhi[kMaxParticles];
  Float_t MuonMass[kMaxParticles];
  Float_t MuonIso[kMaxParticles];
  Bool_t  MuonTightID[kMaxParticles];
  Int_t   MuonQ[kMaxParticles];

  UInt_t nTau;
  Float_t TauEta[kMaxParticles];
  Float_t TauPt[kMaxParticles];
  Float_t TauPhi[kMaxParticles];
  Float_t TauMass[kMaxParticles];
  Bool_t  TauDecayID[kMaxParticles];
  UChar_t TauAntiEleID[kMaxParticles];
  UChar_t TauAntiMuID[kMaxParticles];
  UChar_t TauAntiJetID[kMaxParticles];
  Int_t   TauQ[kMaxParticles];

  Bool_t HLT_IsoEle27;
  Bool_t HLT_IsoMu24;
  Bool_t HLT_Mu50;

  //indexes/flavor of identified leptons
  Int_t leptonOneIndex;
  Int_t leptonTwoIndex;
  Int_t leptonThreeIndex;
  Int_t leptonFourIndex;
  Int_t  leptonOneFlavor;
  Int_t  leptonTwoFlavor;
  Int_t  leptonThreeFlavor;
  Int_t  leptonFourFlavor;
  
};
