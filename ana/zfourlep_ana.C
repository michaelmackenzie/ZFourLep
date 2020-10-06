
#include "Tree_t.hh"
#include "Hist_t.hh"

//fields for carrying information around
namespace {
  Tree_t vars_; //variables read in
  bool debug_ = false;
  Long64_t debugMax_ = 1000;
  const static Int_t fn = 100; //possible selections
  TFile*        fOut;
  TDirectory*   fTopDir;
  TDirectory*   fDirectories[fn];
  Hist_t* fHist[fn];
  Bool_t fSelections[fn]; //whether or not to book a histogram set

  TLorentzVector* lepOneP4   = new TLorentzVector();
  TLorentzVector* lepTwoP4   = new TLorentzVector();
  TLorentzVector* lepThreeP4 = new TLorentzVector();
  TLorentzVector* lepFourP4  = new TLorentzVector();
  Int_t charges[4];
  TLorentzVector* leptons[4]; //paired leptons
  Int_t paircharges[4];
  Int_t pairflavors[4];
}

//decide which leptons pair
Int_t decide_pairings() {
  if(charges[0] + charges[1] + charges[2] + charges[3] != 0) return 1;
  //input flavors are in increasing order (so if one != two, one != three, four)
  Int_t onef(abs(vars_.leptonOneFlavor)), twof(abs(vars_.leptonTwoFlavor)),
    threef(abs(vars_.leptonThreeFlavor)), fourf(abs(vars_.leptonFourFlavor));
  bool anymatching = true; //FIXME: add in same flavor considerations over just best z mass 
  bool xxxx = onef == fourf;
  // bool xxxz = !xxxx && onef == threef;
  // bool xxyz = onef == twof && charges[0] != charges[1] && onef != threef;
  // //e+mumu+tau
  // bool xyyz = onef != twof && twof == threef && threef != fourf && charges[1] != charges[2];
  // //mumutautau or eexy
  // if(xxyz) {
  //   leptons[0] = lepOneP4; leptons[1] = lepTwoP4; leptons[2] = lepThreeP4; leptons[3] = lepFourP4;
  //   paircharges[0] = charges[0]; paircharges[1] = charges[1]; paircharges[2] = charges[2]; paircharges[3] = charges[3];
  //   pairflavors[0] = onef; pairflavors[1] = twof; pairflavors[2] = threef; pairflavors[3] = fourf;
  //   //emumutau
  // } if(xyyz) {
  //   leptons[0] = lepTwoP4; leptons[1] = lepThreeP4; leptons[2] = lepOneP4; leptons[3] = lepFourP4;
  //   paircharges[0] = charges[1]; paircharges[1] = charges[2]; paircharges[2] = charges[0]; paircharges[3] = charges[3];
  //   pairflavors[0] = twof; pairflavors[1] = threef; pairflavors[2] = onef; pairflavors[3] = fourf;
  // } 
  if(anymatching || xxxx) {//any lepton can pair with any lepton
    //check each opposite pair for highest masses
    bool charge12 = charges[0] != charges[1];
    bool charge13 = charges[0] != charges[2];
    //four opposite charged masses, mass1+mass3 pair and mass2+mass4 pair
    double mass1 = (charge12) ? (*lepOneP4+*lepTwoP4).M() : (*lepOneP4+*lepThreeP4).M();
    double mass2 = (charge13&&charge12) ? (*lepOneP4+*lepThreeP4).M() : (*lepOneP4+*lepFourP4).M();
    double mass3 = (charge12) ? (*lepThreeP4+*lepFourP4).M() : (*lepTwoP4+*lepFourP4).M();
    double mass4 = (charge13&&charge12) ? (*lepTwoP4+*lepFourP4).M() : (*lepTwoP4+*lepThreeP4).M();
    //accept the pairing with both masses closest to the Z mass
    double zmass = 91.2;
    if(abs(mass1-zmass)+abs(mass3-zmass) < abs(mass2-zmass) + abs(mass4-zmass)) {
      if(charge12) {
	leptons[0] = lepOneP4; leptons[1] = lepTwoP4; leptons[2] = lepThreeP4; leptons[3] = lepFourP4;
	paircharges[0] = charges[0]; paircharges[1] = charges[1]; paircharges[2] = charges[2]; paircharges[3] = charges[3];
	pairflavors[0] = onef; pairflavors[1] = twof; pairflavors[2] = threef; pairflavors[3] = fourf;
      } else  {
	leptons[0] = lepOneP4; leptons[1] = lepThreeP4; leptons[2] = lepTwoP4; leptons[3] = lepFourP4;
	paircharges[0] = charges[0]; paircharges[1] = charges[2]; paircharges[2] = charges[1]; paircharges[3] = charges[3];
	pairflavors[0] = onef; pairflavors[1] = threef; pairflavors[2] = twof; pairflavors[3] = fourf;
      }
    } else {
      if(charge12&&charge12) {
	leptons[0] = lepOneP4; leptons[1] = lepThreeP4; leptons[2] = lepTwoP4; leptons[3] = lepFourP4;
	paircharges[0] = charges[0]; paircharges[1] = charges[2]; paircharges[2] = charges[1]; paircharges[3] = charges[3];
	pairflavors[0] = onef; pairflavors[1] = threef; pairflavors[2] = twof; pairflavors[3] = fourf;
      } else  {
	leptons[0] = lepOneP4; leptons[1] = lepFourP4; leptons[2] = lepTwoP4; leptons[3] = lepThreeP4;
	paircharges[0] = charges[0]; paircharges[1] = charges[3]; paircharges[2] = charges[1]; paircharges[3] = charges[2];
	pairflavors[0] = onef; pairflavors[1] = fourf; pairflavors[2] = twof; pairflavors[3] = threef;
      }
    }
  }
  return 0;
}

//initialize a lorentz vector
Int_t initialize_lepton(Int_t index, Int_t flavor, TLorentzVector* lep, int number) {
  if(abs(flavor) == 11)     {
    lep->SetPtEtaPhiM(vars_.ElectronPt[index],
		      vars_.ElectronEta[index],
		      vars_.ElectronPhi[index],
		      vars_.ElectronMass[index]);
    charges[number] = vars_.ElectronQ[index];
  }
  else if(abs(flavor) == 13) {
    lep->SetPtEtaPhiM(vars_.MuonPt[index],
		      vars_.MuonEta[index],
		      vars_.MuonPhi[index],
		      vars_.MuonMass[index]);
    charges[number] = vars_.MuonQ[index];
  }
  else if(abs(flavor) == 15) {
    lep->SetPtEtaPhiM(vars_.TauPt[index],
		      vars_.TauEta[index],
		      vars_.TauPhi[index],
		      vars_.TauMass[index]);
    charges[number] = vars_.TauQ[index];
  }

  return 0;
}

//initialize the lepton lorentz vectors and pairings
Int_t initialize_leptons() {
  initialize_lepton(vars_.leptonOneIndex,   vars_.leptonOneFlavor,   lepOneP4  , 0);
  initialize_lepton(vars_.leptonTwoIndex,   vars_.leptonTwoFlavor,   lepTwoP4  , 1);
  initialize_lepton(vars_.leptonThreeIndex, vars_.leptonThreeFlavor, lepThreeP4, 2);
  initialize_lepton(vars_.leptonFourIndex,  vars_.leptonFourFlavor,  lepFourP4 , 3);
  decide_pairings();
  return 0;
}

//logic to fill the histograms
Int_t fill_histograms(Hist_t* hist) {
  TLorentzVector lv1 = (*leptons[0] + *leptons[1]);
  TLorentzVector lv2 = (*leptons[2] + *leptons[3]);
  TLorentzVector lv3 = (paircharges[0] != paircharges[2]) ? (*leptons[0]+*leptons[2]) : (*leptons[0]+*leptons[3]);
  TLorentzVector lv4 = (paircharges[0] != paircharges[2]) ? (*leptons[1]+*leptons[3]) : (*leptons[1]+*leptons[2]);
  hist->hDiLeptonMass[0]->Fill(lv1.M());
  hist->hDiLeptonMass[1]->Fill(lv2.M());
  hist->hQuadLeptonMass->Fill((lv1+lv2).M());
  hist->hOtherPairMass[0]->Fill(lv3.M());
  hist->hOtherPairMass[1]->Fill(lv4.M());
  for(int i = 0; i < 4; ++i)
    hist->hLepPt[i]->Fill(leptons[i]->Pt());
  hist->hDiLepPt[0]->Fill(lv1.Pt());
  hist->hDiLepPt[1]->Fill(lv2.Pt());
  hist->hQuadLepPt->Fill((lv1+lv2).Pt());
  for(int i = 0; i < 4; ++i)
    hist->hLepFlavor[i]->Fill(pairflavors[i]);
  return 0;
}

//set addresses for the input tree
Int_t set_branch_addresses(TTree* t) {
  if(!t) return 1;
  t->SetBranchAddress("nElectron"    ,&vars_.nElectron);
  t->SetBranchAddress("Electron_pt"  ,&vars_.ElectronPt);
  t->SetBranchAddress("Electron_eta" ,&vars_.ElectronEta);
  t->SetBranchAddress("Electron_phi" ,&vars_.ElectronPhi);
  t->SetBranchAddress("Electron_mass",&vars_.ElectronMass);
  t->SetBranchAddress("Electron_charge",&vars_.ElectronQ);
  t->SetBranchAddress("Electron_deltaEtaSC" ,&vars_.ElectronDeltaEtaSC);
  t->SetBranchAddress("Electron_mvaFall17V2Iso_WP80" ,&vars_.ElectronWP80);

  t->SetBranchAddress("nMuon"    ,&vars_.nMuon);
  t->SetBranchAddress("Muon_pt"  ,&vars_.MuonPt);
  t->SetBranchAddress("Muon_eta" ,&vars_.MuonEta);
  t->SetBranchAddress("Muon_phi" ,&vars_.MuonPhi);
  t->SetBranchAddress("Muon_mass",&vars_.MuonMass);
  t->SetBranchAddress("Muon_charge",&vars_.MuonQ);
  t->SetBranchAddress("Muon_pfRelIso04_all",&vars_.MuonIso);
  t->SetBranchAddress("Muon_tightId",&vars_.MuonTightID);

  t->SetBranchAddress("nTau"    ,&vars_.nTau);
  t->SetBranchAddress("Tau_pt"  ,&vars_.TauPt);
  t->SetBranchAddress("Tau_eta" ,&vars_.TauEta);
  t->SetBranchAddress("Tau_phi" ,&vars_.TauPhi);
  t->SetBranchAddress("Tau_mass",&vars_.TauMass);
  t->SetBranchAddress("Tau_charge",&vars_.TauQ);
  t->SetBranchAddress("Tau_idDeepTau2017v2p1VSe",&vars_.TauAntiEleID);
  t->SetBranchAddress("Tau_idDeepTau2017v2p1VSmu",&vars_.TauAntiMuID);
  t->SetBranchAddress("Tau_idDeepTau2017v2p1VSjet",&vars_.TauAntiJetID);

  t->SetBranchAddress("HLT_Ele27_WPTight_Gsf",&vars_.HLT_IsoEle27);
  t->SetBranchAddress("HLT_IsoMu24",&vars_.HLT_IsoMu24);
  t->SetBranchAddress("HLT_Mu50",&vars_.HLT_Mu50);

  t->SetBranchAddress("leptonOneIndex", &vars_.leptonOneIndex);
  t->SetBranchAddress("leptonTwoIndex", &vars_.leptonTwoIndex);
  t->SetBranchAddress("leptonThreeeIndex", &vars_.leptonThreeIndex);
  t->SetBranchAddress("leptonFourIndex", &vars_.leptonFourIndex);
  t->SetBranchAddress("leptonOneFlavor", &vars_.leptonOneFlavor);
  t->SetBranchAddress("leptonTwoFlavor", &vars_.leptonTwoFlavor);
  t->SetBranchAddress("leptonThreeeFlavor", &vars_.leptonThreeFlavor);
  t->SetBranchAddress("leptonFourFlavor", &vars_.leptonFourFlavor);
  
  return 0;
}

//initialize sets of histograms
Int_t book_histograms() {
  for(Int_t i = 0; i < fn; ++i) fSelections[i] = false;
  fSelections[0] = true; //all events
  fSelections[1] = true; //passes base mass test
  fSelections[2] = true; //passes extra mass test
  fSelections[3] = true; //passes 4l mass test
  fSelections[4] = true; //mumutautau
  fSelections[5] = true; //mumuetau
  fSelections[6] = true; //eemutau
  fSelections[7] = true; //muetautau

  for(Int_t i = 0; i < fn; ++i) {
    if(fSelections[i]) {
      fDirectories[i] = fTopDir->mkdir(Form("hist_%i", i));
      fDirectories[i]->cd();
      fHist[i] = new Hist_t;
      BookHistograms(fHist[i]);
    }
  }
  return 0;
}

//main function
Int_t zfourlep_ana(TString name = "Z4L_ZFourLepAnalysis_merged.root") {
  //open the file and retrieve the relevant TTree
  TFile* f = TFile::Open(name.Data(), ((debug_) ? "READ" : "UPDATE"));
  if(!f) return 1;
  TTree* t = (TTree*) f->Get("Events");
  if(!t) return 2;
  if(set_branch_addresses(t)) return 3;
  Long64_t nentries = t->GetEntriesFast();
  std::cout << "Given tree has " << nentries << " entries to process!\n";
  if(debug_) std::cout << "In debug mode, won't update the given tree and will only process first "
		       << debugMax_ << " entries!\n";
  nentries = (debug_ && debugMax_ < nentries) ? debugMax_ : nentries;

  //initialize out file structure
  fOut = new TFile("zfourlep_ana.root", "RECREATE");
  fTopDir = fOut->mkdir("Data");
  fTopDir->cd();
  std::cout << "Initializing selection histograms...\n";
  book_histograms();

  //Processing loop
  for(Long64_t entry = 0; entry < nentries; ++entry) {
    if((debug_ && entry%100 == 0) || entry%50000 == 0)
      std::cout << "Processing entry " << entry << "...\n";
    t->GetEntry(entry);
    //set lorentz vectors
    initialize_leptons();
    //require two opposite charge pairs
    if(charges[0] + charges[1] + charges[2] + charges[3] != 0) {
      if(debug_) std::cout << "Warning! Event " << entry << " has inequal charge balance!\n";
      continue;
    }
    //basic selection
    fill_histograms(fHist[0]);
    double mass1 = (*(leptons[0])+*(leptons[1])).M();
    double mass2 = (*(leptons[2])+*(leptons[3])).M();
    double zmass(91.2);
    bool accept = mass1 < 120. && mass2 < 120. && (mass2 > 40. || mass1 > 40.);
    //mass requirement
    if(accept) fill_histograms(fHist[1]);
    double mass3 = (paircharges[0] != paircharges[2]) ? (*(leptons[0])+*(leptons[2])).M() : (*(leptons[0])+*(leptons[3])).M();
    double mass4 = (paircharges[1] != paircharges[3]) ? (*(leptons[1])+*(leptons[3])).M() : (*(leptons[1])+*(leptons[2])).M();
    accept &= mass3 > 4. && mass4 > 4.;
    //opposite pair mass requirement
    if(accept) fill_histograms(fHist[2]);
    //4 lepton mass requirement
    double masssys = (*leptons[0]+*leptons[1]+*leptons[2]+*leptons[3]).M();
    accept &= masssys > 80. && masssys < 100.;
    if(accept) fill_histograms(fHist[3]);
    //different final state selections
    bool mumutautau = pairflavors[0] == 13 && pairflavors[1] == 13 && pairflavors[2] == 15 && pairflavors[3] == 15;
    if(accept && mumutautau) fill_histograms(fHist[4]);
    bool mumuetau = pairflavors[0] == 11 && pairflavors[1] == 15 && pairflavors[2] == 13 && pairflavors[3] == 13;
    if(accept && mumuetau) fill_histograms(fHist[5]);
    bool eemutau = pairflavors[0] == 11 && pairflavors[1] == 11 && (pairflavors[2] + pairflavors[3] == 13+15);
    if(accept && eemutau) fill_histograms(fHist[6]);
    bool muetautau = pairflavors[0] == 11 && (pairflavors[1]+pairflavors[2]+pairflavors[3] == 13+15+15);
    if(accept && muetautau) fill_histograms(fHist[7]);

  }
  //close files
  f->Close();
  fOut->Write();
  delete fOut;
  return 0;					       
}
