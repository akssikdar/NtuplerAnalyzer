import FWCore.ParameterSet.Config as cms

#demo = cms.EDAnalyzer('NtuplerAnalyzer',
#           minTracks = cms.untracked.uint32(0)
#)

ntupler = cms.EDAnalyzer('NtuplerAnalyzer',
    isMC = cms.bool(False),
    muHLT_MC1   = cms.string("HLT_IsoMu24_v4"  ),
    muHLT_MC2   = cms.string("HLT_IsoTkMu24_v4"),
    muHLT_Data1 = cms.string("HLT_IsoMu24_v*"  ), # the HLT pattern match
    muHLT_Data2 = cms.string("HLT_IsoTkMu24_v*"),
    elHLT_Data  = cms.string("HLT_Ele27_WPTight_Gsf_v*"),
    elHLT_MC    = cms.string("HLT_Ele27_WPTight_Gsf_v7"),
    lepMonitorHLT = cms.string("HLT_PFHT400_SixJet30_DoubleBTagCSV_p056"),

    jecDir          = cms.string('${CMSSW_BASE}/src/UserCode/ttbar-leptons-80X/data/jec/25ns/'),
    resolutionFile  = cms.string('${CMSSW_BASE}/src/UserCode/ttbar-leptons-80X/data/jec/25ns/Spring16_25nsV10_MC_PtResolution_AK4PFchs.txt'),
    scaleFactorFile = cms.string('${CMSSW_BASE}/src/UserCode/ttbar-leptons-80X/data/jec/25ns/Spring16_25nsV10_MC_SF_AK4PFchs.txt'),

    btag_threshold = cms.double(0.5426),
    # X80 2016 ReReco, https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
    # Loose  0.5426
    # Medium 0.8484
    # Tight  0.9535
    el_kino_cuts_pt  = cms.double( 27.),
    el_kino_cuts_eta = cms.double( 2.5),
    el_veto_kino_cuts_pt  = cms.double( 10.),
    el_veto_kino_cuts_eta = cms.double( 2.5),
    mu_kino_cuts_pt  = cms.double( 24.),
    mu_kino_cuts_eta = cms.double( 2.5),
    mu_veto_kino_cuts_pt  = cms.double( 15.),
    mu_veto_kino_cuts_eta = cms.double( 2.5),

    jet_kino_cuts_pt  = cms.double( 25.),
    jet_kino_cuts_eta = cms.double( 2.4),
    tau_kino_cuts_pt  = cms.double( 25.),
    tau_kino_cuts_eta = cms.double( 2.3)
)

