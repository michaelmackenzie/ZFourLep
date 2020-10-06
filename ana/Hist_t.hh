
struct Hist_t {
  TH1F* hDiLeptonMass[2];
  TH1F* hQuadLeptonMass;
  TH1F* hOtherPairMass[2];
  TH1F* hLepPt[4];
  TH1F* hDiLepPt[2];
  TH1F* hQuadLepPt;
  TH1F* hLepFlavor[4];
};

void BookHistograms(Hist_t* hist) {
  hist->hDiLeptonMass[0]  = new TH1F("dileptonmass0"  , "DileptonMass[0]" , 200, 0., 400.);
  hist->hDiLeptonMass[1]  = new TH1F("dileptonmass1"  , "DileptonMass[1]" , 200, 0., 400.);
  hist->hQuadLeptonMass   = new TH1F("quadleptonmass" , "QuadleptonMass"  , 200, 0., 400.);
  hist->hOtherPairMass[0] = new TH1F("otherpairmass0" , "OtherPairMass[0]", 200, 0., 400.);
  hist->hOtherPairMass[1] = new TH1F("otherpairmass1" , "OtherPairMass[1]", 200, 0., 400.);
  for(int i = 0; i < 4; ++i)
    hist->hLepPt[i] = new TH1F(Form("leppt%i",i), Form("LepPt[%i]", i), 150., 0., 150.);
  hist->hDiLepPt[0] = new TH1F("dileppt0", "DiLepPt[0]", 150., 0., 150.);
  hist->hDiLepPt[1] = new TH1F("dileppt1", "DiLepPt[1]", 150., 0., 150.);
  hist->hQuadLepPt  = new TH1F("quadleppt", "QuadLepPt", 150., 0., 150.);
  for(int i = 0; i < 4; ++i)
    hist->hLepFlavor[i] = new TH1F(Form("lepflavor%i",i), Form("LepFlavor[%i]", i), 6, 10, 16);
}
