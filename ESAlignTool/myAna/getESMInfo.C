#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include "TF1.h"
#include "TFile.h"
#include "TH1.h"
#include "TH1D.h"
#include "TH2F.h"
#include "TGraph.h"
#include "TCanvas.h"
#include "TTree.h"
#include "TLegend.h"
#include "TStyle.h"
#include "TString.h"
#include "TROOT.h"
#include "CalIter_wRotation.h"
using namespace std;

// Change the number for this iteration 
//const int iterN=2;

void getESMInfo(int iterN, TString rootfile){

    printf("iterN = %d\n", iterN);

	TFile* f;	
	TTree* t;
	//f=new TFile("/afs/cern.ch/work/j/jtsai/ESAlignment/CMSSW_8_0_8/src/AlignmentTool/ESAlignTool/test/OnLxplus/24May_Run2016B_iter1/HLTPhysics.root");
	//f=new TFile("/afs/cern.ch/work/j/jtsai/ESAlignment/CMSSW_8_0_8/src/AlignmentTool/ESAlignTool/test/OnLxplus/24May_Run2016B_iter2/HLTPhysics.root");
	//f=new TFile("/afs/cern.ch/work/j/jtsai/ESAlignment/CMSSW_8_0_8/src/AlignmentTool/ESAlignTool/test/OnLxplus/24May_Run2016B_iter3/HLTPhysics.root");
	//f=new TFile("/afs/cern.ch/work/j/jtsai/ESAlignment/CMSSW_8_0_8/src/AlignmentTool/ESAlignTool/test/OnLxplus/24May_Run2016B_iter4/HLTPhysics.root");
	//f=new TFile("/afs/cern.ch/work/j/jtsai/ESAlignment/CMSSW_8_0_8/src/AlignmentTool/ESAlignTool/test/OnLxplus/24May_Run2016B_iter5/HLTPhysics.root");
	//f=new TFile("/afs/cern.ch/work/j/jtsai/ESAlignment/CMSSW_8_0_8/src/AlignmentTool/ESAlignTool/test/OnLxplus/24May_Run2016B_iter6/HLTPhysics.root");
	//f=new TFile("/afs/cern.ch/work/j/jtsai/ESAlignment/CMSSW_8_0_8/src/AlignmentTool/ESAlignTool/test/OnLxplus/24May_Run2016B_iter7/HLTPhysics.root");
	//f=new TFile("/afs/cern.ch/work/j/jtsai/ESAlignment/CMSSW_8_0_8/src/AlignmentTool/ESAlignTool/test/OnLxplus/24May_Run2016B_iter8/HLTPhysics.root");
	//f=new TFile("/afs/cern.ch/work/j/jtsai/ESAlignment/CMSSW_8_0_8/src/AlignmentTool/ESAlignTool/test/OnLxplus/24May_Run2016B_iter9/HLTPhysics.root");
	//f=new TFile("/afs/cern.ch/work/j/jtsai/ESAlignment/CMSSW_8_0_8/src/AlignmentTool/ESAlignTool/test/OnLxplus/24May_Run2016B_iter10/HLTPhysics.root");
    
	f=new TFile(rootfile);

	t=(TTree*)f->Get("ESAlignmentTool/tree");
  	CalIter_wRotation caculate;
	caculate.registerESMatrix(t);
	caculate.iterN=iterN;
    // Change for the file name 
	caculate.run("test");
}
