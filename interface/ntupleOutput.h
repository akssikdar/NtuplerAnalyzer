//#ifndef NTUPLEOUTPUT_INTERFACE_H
//#define NTUPLEOUTPUT_INTERFACE_H
// hemmm... it's for the sake of redefining the macro.. kind of messy and will through warnings
// if necessary to not redefine them -- need to split class declaration and initialization in different files, which I don't do at the moment

/*
 * Useful info
 *
 * TNtuple is:
 *   branches of Float_t parameters, named somehow
 *
 * TTree is:
 *   branches of simple Float_t, Int_t parameters or complex classes, known to ROOT
 *   (new classes are given to ROOT by call gROOT->ProcessLine("#include <vector>"))
 *   the creation method for these 2 types is different,
 *   also these methods are different from from TNtuple ones (in better way)
 *
 */

/*
 * What is wanted:
 *   keep the output TTree interface (i.e. the definitions of Branches, their classes and names) in 1 file
 *   easily create or open TTree of this interface in main process
 *   loop over Entires
 *   and have full access to all the branches
 *
 * To do it:
 *   there are macro creating this interface
 *   and the list of them with current definition of the interface is in this file
 *   there are 2 bunches of macro -- for creating Branches of new TTree or for opening existing one
 *   which unfold into commands like
 *      Class_X NT_branchFoo; outputTTreeObject.Branch("branchFoo", "Class_X", &NT_branchFoo);
 *      or
 *      Class_X NT_branchFoo; outputTTreeObject.SetBranchAddress("branchFoo", &NT_branchFoo);
 *
 * the outputTTreeObject is defined in OUTNTUPLE
 * the mode of the interface (create or open ttree) is defined with NTUPLE_INTERFACE_CREATE or NTUPLE_INTERFACE_OPEN
 *
 * there are also a bunch of convenience macro for handling the TNtuple legacy bunches of Float_t parameters
 * -- they mostly should go away when propper objects are used
 *  and there is a macro reseting all the branch parameters -- it's ad-hoc, TODO: do it somehow in more automated, convenient way
 *
 * branch object names are prepended with NT_
 * so a branch named "foo" in the program namespace will have the object named NT_foo
 *
 * also default name of the TTree is NT_output_ttree
 *
 * there is a usage example in a comment further
 */

// default name of the output
#ifndef OUTNTUPLE
	#define OUTNTUPLE NT_output_ttree
#endif

#ifndef DEFAULT_PARAMETER
#define DEFAULT_PARAMETER -111
#endif

/* macro declaring the object and setting a branch with its' pointer --- all in current, __not_global__ space (in main space)
 *
 * Notice the protocol:
 *    1) the object name in current namespace is `NT_Name`
 *    2) the branch name in the ntuple is `Name`
 */
#if defined(NTUPLE_INTERFACE_CLASS_DECLARE) // ALSO: in EDM Classes NTuple is pointer to TFile Service!
	// to declare vector of types (int/float etc): declate just vector
	#define VECTOR_PARAMs_in_NTuple(NTuple, TYPE, Name)   std::vector<TYPE> NT_##Name;
	// to declare vector of objects: declate vector and a pointer to it
	#define VECTOR_OBJECTs_in_NTuple(NTuple, VECTOR_CLASS, Name)   VECTOR_CLASS NT_##Name; VECTOR_CLASS* pt_NT_##Name;
	// objects and types (simple parameters)
	#define OBJECT_in_NTuple(NTuple, CLASS, Name)   CLASS   NT_##Name;
	#define Float_t_in_NTuple(NTuple, Name)         Float_t NT_##Name;
	#define Int_t_in_NTuple(NTuple, Name)           Int_t   NT_##Name;
	#define Bool_t_in_NTuple(NTuple, Name)          Bool_t  NT_##Name;
#elif defined(NTUPLE_INTERFACE_CLASS_INITIALIZE)
	// hook up branch
	#define VECTOR_PARAMs_in_NTuple(NTuple, TYPE, Name)   NTuple->Branch(#Name, &NT_##Name);
	// hook up pointer for vectors of objects
	#define VECTOR_OBJECTs_in_NTuple(NTuple, VECTOR_CLASS, Name)   pt_NT_##Name = & NT_##Name; NTuple->Branch(#Name, #VECTOR_CLASS, &pt_NT_##Name);
	// objects and types (simple parameters)
	#define OBJECT_in_NTuple(NTuple, CLASS, Name)   NTuple->Branch(#Name, #CLASS, &NT_##Name);
	#define Float_t_in_NTuple(NTuple, Name)         NTuple->Branch(#Name, &NT_##Name, #Name "/F");
	#define Int_t_in_NTuple(NTuple, Name)           NTuple->Branch(#Name, &NT_##Name, #Name "/I");
	#define Bool_t_in_NTuple(NTuple, Name)          NTuple->Branch(#Name, &NT_##Name, #Name "/O");
#elif defined(NTUPLE_INTERFACE_CLASS_RESET)
	#define VECTOR_PARAMs_in_NTuple(NTuple, TYPE, Name)            NT_##Name.clear();
	#define VECTOR_OBJECTs_in_NTuple(NTuple, VECTOR_CLASS, Name)   NT_##Name.clear();
	// objects and types (simple parameters)
	//#define OBJECT_in_NTuple(NTuple, CLASS, Name)   CLASS   NT_##Name; NTuple.Branch(#Name, #CLASS, &NT_##Name);
	#define OBJECT_in_NTuple(NTuple, CLASS, Name)
	// WARNING: you'll have to reset your object yourself!
	// and these are defaults:
	#define Float_t_in_NTuple(NTuple, Name)         NT_##Name = DEFAULT_PARAMETER ;
	#define Int_t_in_NTuple(NTuple, Name)           NT_##Name = DEFAULT_PARAMETER ;
	#define Bool_t_in_NTuple(NTuple, Name)          NT_##Name = false;
// ok, the classes should work
// the following are outdated at the moment:
#elif defined(NTUPLE_INTERFACE_CREATE)
	#define VECTOR_PARAMs_in_NTuple(NTuple, TYPE, Name)   std::vector<TYPE> NT_##Name; NTuple.Branch(#Name, &NT_##Name);
	#define VECTOR_OBJECTs_in_NTuple(NTuple, VECTOR_CLASS, Name)   VECTOR_CLASS NT_##Name; VECTOR_CLASS* pt_NT_##Name ; NTuple.Branch(#Name, #VECTOR_CLASS, &pt_NT_##Name);
	#define OBJECT_in_NTuple(NTuple, CLASS, Name)   CLASS   NT_##Name; NTuple.Branch(#Name, #CLASS, &NT_##Name);
	#define Float_t_in_NTuple(NTuple, Name)         Float_t NT_##Name; NTuple.Branch(#Name, &NT_##Name, #Name "/F");
	#define Int_t_in_NTuple(NTuple, Name)           Int_t   NT_##Name; NTuple.Branch(#Name, &NT_##Name, #Name "/I");
	#define Bool_t_in_NTuple(NTuple, Name)          Bool_t  NT_##Name; NTuple.Branch(#Name, &NT_##Name, #Name "/O");
#elif defined(NTUPLE_INTERFACE_OPEN)
	#define OBJECT_in_NTuple(NTuple, CLASS, Name)   CLASS*  NT_##Name = 0; NTuple->SetBranchAddress(#Name, &NT_##Name);
	#define PARAMETER_in_NTuple(NTuple, TYPE, Name)  TYPE   NT_##Name; NTuple->SetBranchAddress(#Name, &NT_##Name);
	#define Float_t_in_NTuple(NTuple, Name)         PARAMETER_in_NTuple(NTuple, Float_t, Name);
	#define Int_t_in_NTuple(NTuple, Name)           PARAMETER_in_NTuple(NTuple, Int_t, Name);
	#define Bool_t_in_NTuple(NTuple, Name)          PARAMETER_in_NTuple(NTuple, Bool_t, Name);
#else
	error: set ntuple interface mode
#endif

/*
 * complex objects in vectors
 * from https://root.cern.ch/root/html/tutorials/math/mathcoreVectorCollection.C.html
 *   std::vector<ROOT::Math::XYZTVector>  tracks;
 *   std::vector<ROOT::Math::XYZTVector> * pTracks = &tracks;
 *   t1.Branch("tracks","std::vector<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<double> > >",&pTracks);
 *
 * simple objects (float, int) in vectors)
 * from
 *
 *   std::vector<float> vpx;
 *
 *   // Create a TTree
 *   TTree *t = new TTree("tvec","Tree with vectors");
 *   t->Branch("vpx",&vpx);
 *
 */

/*
 * this file ties the interface to our ntuple (TTree) in the current namespace
 *
 * Usage
 * 
 * actual files using it are:
 *   bin/ntupleEvents.cc           (creates the TTree, at line 1542 in main)
 *   test/likelihood_regions.cc    (uses existing TTree, at line 51 in pull_likelihood_regions)
 *
 * Roughly the idea is as follows
 *
 * declare your ntuple:
 *
 *     TTree output("reduced_ttree", "TTree with reduced event data");
 *     // if the name is not `NT_output_ttree` (which is assumed here in the interface)
 *     // define your name for preprocessor:
 *     #define OUTNTUPLE output
 *
 *     // set the mode of the interface to branches (create branches in a new TTree or open branches of existing TTree):
 *     #define NTUPLE_INTERFACE_CREATE
 * 
 *     // load this interface:
 *     #include "ntupleOutput.h"
 *
 * now you have NT_Name objects in the name space and the ntuple has branches "Name" with pointers to these objects
 * you can loop over TTree:
 *
 *     for (Long64_t i=0; i<NT_output_ttree.GetEntries(); i++)
 *         {
 *         NT_output_ttree.GetEntry(i);
 *         ...
 *         }
 *
 * copy objects from event (pseudocode):
 *
 *     NT_foo = events[i]["foo"])
 *
 * or actual example from ntupleEvents:
 *     NT_aMCatNLO_weight = evt->weight();
 * or from likelihood_regions:
 *     if (NT_tau_IDlev_0 != 3. && NT_tau_IDlev_1 != 3.) continue;
 *     
 * when done fill the ntuple:
 *
 *     output.Fill();
 *
 * clearing/reseting of the objects for each event -- currently it is responsibility of the programmer
 * but there is a sketchy macro for this now, it is in development
 * used as in ntupleEvents:
 *     RESET_NTUPLE_PARAMETERS // defaults all parameters
 *
 * -- with no ;
 * that's how sketchy it is
 *
 */


/* TODO: add what's missing from eventSelection
 *       and use proper TLorentzVector etc classes
 *
 * MET filters and lumisection certificate are done on the fly at ntuple production
 * lumi passes after MET filters -- to properly account for it in luminosity
 */

#ifndef NTUPLEOUTPUT_LORENTZVECTOR_H
#define NTUPLEOUTPUT_LORENTZVECTOR_H
// the exact LorentzVector declaration
typedef ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<double> > LorentzVector;
#endif /* NTUPLEOUTPUT_LORENTZVECTOR_H */

//#endif /* NTUPLEOUTPUT_INTERFACE_H */

/*
 * And declarations of the whole output
 * (tried splitting it into several files, for lighter/faster processing -- no significant speed-up, and not worth trouble for now)
 */

// COMMON OUTPUT
Float_t_in_NTuple(OUTNTUPLE, aMCatNLO_weight)
Float_t_in_NTuple(OUTNTUPLE, gen_t_pt)
Float_t_in_NTuple(OUTNTUPLE, gen_tb_pt)
Int_t_in_NTuple(OUTNTUPLE, gen_t_w_decay_id) // = id of lepton (11/13/15, but the sign means which product is lepton: minus=1, plus=2) or 1 for quarks
Int_t_in_NTuple(OUTNTUPLE, gen_tb_w_decay_id)
Int_t_in_NTuple(OUTNTUPLE, NUP_gen) // TODO: add gen info from TTbar
Int_t_in_NTuple(OUTNTUPLE, nvtx)

Bool_t_in_NTuple(OUTNTUPLE, HLT_el)
Bool_t_in_NTuple(OUTNTUPLE, HLT_mu)

Int_t_in_NTuple(OUTNTUPLE, leps_ID)
Int_t_in_NTuple(OUTNTUPLE, nleps)
Int_t_in_NTuple(OUTNTUPLE, njets)
Int_t_in_NTuple(OUTNTUPLE, nbjets)
Int_t_in_NTuple(OUTNTUPLE, ntaus)

// MET OUTPUT
OBJECT_in_NTuple(OUTNTUPLE, LorentzVector, met_init)
OBJECT_in_NTuple(OUTNTUPLE, LorentzVector, met_uncorrected)
OBJECT_in_NTuple(OUTNTUPLE, LorentzVector, met_corrected)

// LEPTONS OUTPUT
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Int_t, lep_id)
VECTOR_OBJECTs_in_NTuple(OUTNTUPLE, std::vector<LorentzVector>, lep_p4)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, lep_dxy)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, lep_dz)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, lep_relIso)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, lep_dB)

// JETS OUTPUT
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Int_t, jet_id)
VECTOR_OBJECTs_in_NTuple(OUTNTUPLE, std::vector<LorentzVector>, jet_initial_p4)
VECTOR_OBJECTs_in_NTuple(OUTNTUPLE, std::vector<LorentzVector>, jet_p4)
VECTOR_OBJECTs_in_NTuple(OUTNTUPLE, std::vector<LorentzVector>, jet_uncorrected_p4)
VECTOR_OBJECTs_in_NTuple(OUTNTUPLE, std::vector<LorentzVector>, jet_matched_genjet_p4)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, jet_jes_correction)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, jet_jes_correction_relShift)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, jet_resolution)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, jet_sf)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, jet_sf_up)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, jet_sf_down)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, jet_jer_factor)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, jet_jer_factor_up)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, jet_jer_factor_down)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, jet_rad)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, jet_pu_discr)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, jet_b_discr)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Int_t,   jet_hadronFlavour)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Int_t,   jet_partonFlavour)

// TAUS OUTPUT
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Int_t, tau_id)
VECTOR_OBJECTs_in_NTuple(OUTNTUPLE, std::vector<LorentzVector>, tau_p4)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Int_t, tau_IDlev)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, tau_leading_track_pt)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, tau_leadChargedHadrCand_pt)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, tau_leadNeutralCand_pt)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, tau_leadCand_pt)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, tau_flightLength)
VECTOR_PARAMs_in_NTuple(OUTNTUPLE, Float_t, tau_flightLengthSignificance)

