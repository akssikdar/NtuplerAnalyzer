import logging

# new selection stages
all_std_channels = {
'mu_selSV':          ('({selection_stage}==  9 || {selection_stage}==  7) && event_taus_sv_sign[0] > 2.5', 'selection_stage'),
'mu_selSV_ss':       ('({selection_stage}==  8 || {selection_stage}==  6) && event_taus_sv_sign[0] > 2.5', 'selection_stage'),
'el_selSV':          ('({selection_stage}== 19 || {selection_stage}== 17) && event_taus_sv_sign[0] > 2.5', 'selection_stage'),
'el_selSV_ss':       ('({selection_stage}== 18 || {selection_stage}== 16) && event_taus_sv_sign[0] > 2.5', 'selection_stage'),
'mu_selSVVloose':    ('({selection_stage}==  9 || {selection_stage}==  7 || {selection_stage}==  5) && event_taus_sv_sign[0] > 2.5', 'selection_stage'),
'mu_selSVVloose_ss': ('({selection_stage}==  8 || {selection_stage}==  6 || {selection_stage}==  4) && event_taus_sv_sign[0] > 2.5', 'selection_stage'),
'el_selSVVloose':    ('({selection_stage}== 19 || {selection_stage}== 17 || {selection_stage}== 15) && event_taus_sv_sign[0] > 2.5', 'selection_stage'),
'el_selSVVloose_ss': ('({selection_stage}== 18 || {selection_stage}== 16 || {selection_stage}== 14) && event_taus_sv_sign[0] > 2.5', 'selection_stage'),

'mu_selTight':     ('({selection_stage}==  9)', 'selection_stage'),
'mu_selTight_ss':  ('({selection_stage}==  8)', 'selection_stage'),
'el_selTight':     ('({selection_stage}== 19)', 'selection_stage'),
'el_selTight_ss':  ('({selection_stage}== 18)', 'selection_stage'),
'mu_sel':          ('({selection_stage}==  9 || {selection_stage}==  7)', 'selection_stage'),
'mu_sel_ss':       ('({selection_stage}==  8 || {selection_stage}==  6)', 'selection_stage'),
'el_sel':          ('({selection_stage}== 19 || {selection_stage}== 17)', 'selection_stage'),
'el_sel_ss':       ('({selection_stage}== 18 || {selection_stage}== 16)', 'selection_stage'),
'mu_selVloose':    ('({selection_stage}==  9 || {selection_stage}==  7 || {selection_stage}==  5)', 'selection_stage'),
'mu_selVloose_ss': ('({selection_stage}==  8 || {selection_stage}==  6 || {selection_stage}==  4)', 'selection_stage'),
'el_selVloose':    ('({selection_stage}== 19 || {selection_stage}== 17 || {selection_stage}== 15)', 'selection_stage'),
'el_selVloose_ss': ('({selection_stage}== 18 || {selection_stage}== 16 || {selection_stage}== 14)', 'selection_stage'),

'mu_selTight_ljout':     ('({selection_stage}==  9) && event_jets_lj_var >  60.', 'selection_stage'),
'mu_selTight_ljout_ss':  ('({selection_stage}==  8) && event_jets_lj_var >  60.', 'selection_stage'),
'el_selTight_ljout':     ('({selection_stage}== 19) && event_jets_lj_var >  60.', 'selection_stage'),
'el_selTight_ljout_ss':  ('({selection_stage}== 18) && event_jets_lj_var >  60.', 'selection_stage'),
'mu_sel_ljout':          ('({selection_stage}==  9 || {selection_stage}==  7) && event_jets_lj_var >  60.', 'selection_stage'),
'mu_sel_ljout_ss':       ('({selection_stage}==  8 || {selection_stage}==  6) && event_jets_lj_var >  60.', 'selection_stage'),
'el_sel_ljout':          ('({selection_stage}== 19 || {selection_stage}== 17) && event_jets_lj_var >  60.', 'selection_stage'),
'el_sel_ljout_ss':       ('({selection_stage}== 18 || {selection_stage}== 16) && event_jets_lj_var >  60.', 'selection_stage'),
'mu_selVloose_ljout':    ('({selection_stage}==  9 || {selection_stage}==  7 || {selection_stage}==  5) && event_jets_lj_var >  60.', 'selection_stage'),
'mu_selVloose_ljout_ss': ('({selection_stage}==  8 || {selection_stage}==  6 || {selection_stage}==  4) && event_jets_lj_var >  60.', 'selection_stage'),
'el_selVloose_ljout':    ('({selection_stage}== 19 || {selection_stage}== 17 || {selection_stage}== 15) && event_jets_lj_var >  60.', 'selection_stage'),
'el_selVloose_ljout_ss': ('({selection_stage}== 18 || {selection_stage}== 16 || {selection_stage}== 14) && event_jets_lj_var >  60.', 'selection_stage'),

'mu_selTight_lj':     ('({selection_stage}==  9) && event_jets_lj_var <= 60.', 'selection_stage'),
'mu_selTight_lj_ss':  ('({selection_stage}==  8) && event_jets_lj_var <= 60.', 'selection_stage'),
'el_selTight_lj':     ('({selection_stage}== 19) && event_jets_lj_var <= 60.', 'selection_stage'),
'el_selTight_lj_ss':  ('({selection_stage}== 18) && event_jets_lj_var <= 60.', 'selection_stage'),
'mu_sel_lj':          ('({selection_stage}==  9 || {selection_stage}==  7) && event_jets_lj_var <= 60.', 'selection_stage'),
'mu_sel_lj_ss':       ('({selection_stage}==  8 || {selection_stage}==  6) && event_jets_lj_var <= 60.', 'selection_stage'),
'el_sel_lj':          ('({selection_stage}== 19 || {selection_stage}== 17) && event_jets_lj_var <= 60.', 'selection_stage'),
'el_sel_lj_ss':       ('({selection_stage}== 18 || {selection_stage}== 16) && event_jets_lj_var <= 60.', 'selection_stage'),
'mu_selVloose_lj':    ('({selection_stage}==  9 || {selection_stage}==  7 || {selection_stage}==  5) && event_jets_lj_var <= 60.', 'selection_stage'),
'mu_selVloose_lj_ss': ('({selection_stage}==  8 || {selection_stage}==  6 || {selection_stage}==  4) && event_jets_lj_var <= 60.', 'selection_stage'),
'el_selVloose_lj':    ('({selection_stage}== 19 || {selection_stage}== 17 || {selection_stage}== 15) && event_jets_lj_var <= 60.', 'selection_stage'),
'el_selVloose_lj_ss': ('({selection_stage}== 18 || {selection_stage}== 16 || {selection_stage}== 14) && event_jets_lj_var <= 60.', 'selection_stage'),

# additional channels
'dy_mutau': ('({selection_stage}== 102 || {selection_stage}== 103)', 'selection_stage_dy'),
'dy_eltau': ('({selection_stage}== 112 || {selection_stage}== 113)', 'selection_stage_dy'),
'dy_mumu':  ('({selection_stage}== 102 || {selection_stage}== 103 || {selection_stage}== 105)', 'selection_stage_dy_mumu'),
'dy_elel':  ('({selection_stage}== 112 || {selection_stage}== 113 || {selection_stage}== 115)', 'selection_stage_dy_mumu'),

'tt_elmu':  ('({selection_stage}== 205)', 'selection_stage_em'),
}


systs_weights_nominal = {
'NOMINAL': 'event_weight',
}

systs_weights_common = {
'PUUp'   : "event_weight*event_weight_PUUp/event_weight_PU"    ,
'PUDown' : "event_weight*event_weight_PUDown/event_weight_PU"    ,
'bSFUp'  : "event_weight*event_weight_bSFUp/event_weight_bSF"  ,
'bSFDown': "event_weight*event_weight_bSFDown/event_weight_bSF",

'LEPelIDUp'   : "event_weight*event_weight_LEPelIDUp"   ,
'LEPelIDDown' : "event_weight*event_weight_LEPelIDDown" ,
'LEPelTRGUp'  : "event_weight*event_weight_LEPelTRGUp"  ,
'LEPelTRGDown': "event_weight*event_weight_LEPelTRGDown",
'LEPmuIDUp'   : "event_weight*event_weight_LEPmuIDUp"   ,
'LEPmuIDDown' : "event_weight*event_weight_LEPmuIDDown" ,
'LEPmuTRGUp'  : "event_weight*event_weight_LEPmuTRGUp"  ,
'LEPmuTRGDown': "event_weight*event_weight_LEPmuTRGDown",
}

systs_weights_tt = {
'TOPPTDown'     : 'event_weight'                           ,
'TOPPTUp'       : 'event_weight*event_weight_toppt'        ,
'FragUp'        : 'event_weight*event_weight_FragUp'       ,
'FragDown'      : 'event_weight*event_weight_FragDown'     ,
'SemilepBRUp'   : 'event_weight*event_weight_SemilepBRUp'  ,
'SemilepBRDown' : 'event_weight*event_weight_SemilepBRDown',
'PetersonUp'    : 'event_weight*event_weight_PetersonUp'   ,
'PetersonDown'  : 'event_weight'                           ,
}

systs_weights_tt_hard = {
"MrUp"    : "event_weight*event_weight_me_f_rUp",
"MrDown"  : "event_weight*event_weight_me_f_rDn",
"MfUp"    : "event_weight*event_weight_me_fUp_r",
"MfDown"  : "event_weight*event_weight_me_fDn_r",
"MfrUp"   : "event_weight*event_weight_me_frUp" ,
"MfrDown" : "event_weight*event_weight_me_frDn" ,
}

systs_weights_tt_alpha = {
'AlphaSUp'  : "event_weight*event_weight_AlphaS_up",
'AlphaSDown': "event_weight*event_weight_AlphaS_dn",
}

systs_weights_tt_pdf1 = {
'PDFCT14n1Up'     : "event_weight*event_weight_pdf[0]" ,
'PDFCT14n2Up'     : "event_weight*event_weight_pdf[1]" ,
'PDFCT14n3Up'     : "event_weight*event_weight_pdf[2]" ,
'PDFCT14n4Up'     : "event_weight*event_weight_pdf[3]" ,
'PDFCT14n5Up'     : "event_weight*event_weight_pdf[4]" ,
'PDFCT14n6Up'     : "event_weight*event_weight_pdf[5]" ,
'PDFCT14n7Up'     : "event_weight*event_weight_pdf[6]" ,
'PDFCT14n8Up'     : "event_weight*event_weight_pdf[7]" ,
'PDFCT14n9Up'     : "event_weight*event_weight_pdf[8]" ,
'PDFCT14n10Up'    : "event_weight*event_weight_pdf[9]" ,
}

systs_weights_tt_pdf10 = {
'PDFCT14n11Up'    : "event_weight*event_weight_pdf[10]",
'PDFCT14n12Up'    : "event_weight*event_weight_pdf[11]",
'PDFCT14n13Up'    : "event_weight*event_weight_pdf[12]",
'PDFCT14n14Up'    : "event_weight*event_weight_pdf[13]",
'PDFCT14n15Up'    : "event_weight*event_weight_pdf[14]",
'PDFCT14n16Up'    : "event_weight*event_weight_pdf[15]",
'PDFCT14n17Up'    : "event_weight*event_weight_pdf[16]",
'PDFCT14n18Up'    : "event_weight*event_weight_pdf[17]",
'PDFCT14n19Up'    : "event_weight*event_weight_pdf[18]",
'PDFCT14n20Up'    : "event_weight*event_weight_pdf[19]",
}

systs_weights_tt_pdf20 = {
'PDFCT14n21Up'    : "event_weight*event_weight_pdf[20]",
'PDFCT14n22Up'    : "event_weight*event_weight_pdf[21]",
'PDFCT14n23Up'    : "event_weight*event_weight_pdf[22]",
'PDFCT14n24Up'    : "event_weight*event_weight_pdf[23]",
'PDFCT14n25Up'    : "event_weight*event_weight_pdf[24]",
'PDFCT14n26Up'    : "event_weight*event_weight_pdf[25]",
'PDFCT14n27Up'    : "event_weight*event_weight_pdf[26]",
'PDFCT14n28Up'    : "event_weight*event_weight_pdf[27]",
'PDFCT14n29Up'    : "event_weight*event_weight_pdf[28]",
'PDFCT14n30Up'    : "event_weight*event_weight_pdf[29]",
}

systs_weights_tt_pdf30 = {
'PDFCT14n31Up'    : "event_weight*event_weight_pdf[30]",
'PDFCT14n32Up'    : "event_weight*event_weight_pdf[31]",
'PDFCT14n33Up'    : "event_weight*event_weight_pdf[32]",
'PDFCT14n34Up'    : "event_weight*event_weight_pdf[33]",
'PDFCT14n35Up'    : "event_weight*event_weight_pdf[34]",
'PDFCT14n36Up'    : "event_weight*event_weight_pdf[35]",
'PDFCT14n37Up'    : "event_weight*event_weight_pdf[36]",
'PDFCT14n38Up'    : "event_weight*event_weight_pdf[37]",
'PDFCT14n39Up'    : "event_weight*event_weight_pdf[38]",
'PDFCT14n40Up'    : "event_weight*event_weight_pdf[39]",
}

systs_weights_tt_pdf40 = {
'PDFCT14n41Up'    : "event_weight*event_weight_pdf[40]",
'PDFCT14n42Up'    : "event_weight*event_weight_pdf[41]",
'PDFCT14n43Up'    : "event_weight*event_weight_pdf[42]",
'PDFCT14n44Up'    : "event_weight*event_weight_pdf[43]",
'PDFCT14n45Up'    : "event_weight*event_weight_pdf[44]",
'PDFCT14n46Up'    : "event_weight*event_weight_pdf[45]",
'PDFCT14n47Up'    : "event_weight*event_weight_pdf[46]",
'PDFCT14n48Up'    : "event_weight*event_weight_pdf[47]",
'PDFCT14n49Up'    : "event_weight*event_weight_pdf[48]",
'PDFCT14n50Up'    : "event_weight*event_weight_pdf[49]",
}

systs_weights_tt_pdf50 = {
'PDFCT14n51Up'    : "event_weight*event_weight_pdf[50]",
'PDFCT14n52Up'    : "event_weight*event_weight_pdf[51]",
'PDFCT14n53Up'    : "event_weight*event_weight_pdf[52]",
'PDFCT14n54Up'    : "event_weight*event_weight_pdf[53]",
'PDFCT14n55Up'    : "event_weight*event_weight_pdf[54]",
'PDFCT14n56Up'    : "event_weight*event_weight_pdf[55]",
}


systs_weights_tt_alpha_pdf = {
'AlphaSUp'  : "event_weight*event_weight_AlphaS_up",
'AlphaSDown': "event_weight*event_weight_AlphaS_dn",

'PDFCT14n1Up'     : "event_weight*event_weight_pdf[0]" ,
'PDFCT14n2Up'     : "event_weight*event_weight_pdf[1]" ,
'PDFCT14n3Up'     : "event_weight*event_weight_pdf[2]" ,
'PDFCT14n4Up'     : "event_weight*event_weight_pdf[3]" ,
'PDFCT14n5Up'     : "event_weight*event_weight_pdf[4]" ,
'PDFCT14n6Up'     : "event_weight*event_weight_pdf[5]" ,
'PDFCT14n7Up'     : "event_weight*event_weight_pdf[6]" ,
'PDFCT14n8Up'     : "event_weight*event_weight_pdf[7]" ,
'PDFCT14n9Up'     : "event_weight*event_weight_pdf[8]" ,
'PDFCT14n10Up'    : "event_weight*event_weight_pdf[9]" ,
'PDFCT14n11Up'    : "event_weight*event_weight_pdf[10]",
'PDFCT14n12Up'    : "event_weight*event_weight_pdf[11]",
'PDFCT14n13Up'    : "event_weight*event_weight_pdf[12]",
'PDFCT14n14Up'    : "event_weight*event_weight_pdf[13]",
'PDFCT14n15Up'    : "event_weight*event_weight_pdf[14]",
'PDFCT14n16Up'    : "event_weight*event_weight_pdf[15]",
'PDFCT14n17Up'    : "event_weight*event_weight_pdf[16]",
'PDFCT14n18Up'    : "event_weight*event_weight_pdf[17]",
'PDFCT14n19Up'    : "event_weight*event_weight_pdf[18]",
'PDFCT14n20Up'    : "event_weight*event_weight_pdf[19]",
'PDFCT14n21Up'    : "event_weight*event_weight_pdf[20]",
'PDFCT14n22Up'    : "event_weight*event_weight_pdf[21]",
'PDFCT14n23Up'    : "event_weight*event_weight_pdf[22]",
'PDFCT14n24Up'    : "event_weight*event_weight_pdf[23]",
'PDFCT14n25Up'    : "event_weight*event_weight_pdf[24]",
'PDFCT14n26Up'    : "event_weight*event_weight_pdf[25]",
'PDFCT14n27Up'    : "event_weight*event_weight_pdf[26]",
'PDFCT14n28Up'    : "event_weight*event_weight_pdf[27]",
'PDFCT14n29Up'    : "event_weight*event_weight_pdf[28]",
'PDFCT14n30Up'    : "event_weight*event_weight_pdf[29]",
'PDFCT14n31Up'    : "event_weight*event_weight_pdf[30]",
'PDFCT14n32Up'    : "event_weight*event_weight_pdf[31]",
'PDFCT14n33Up'    : "event_weight*event_weight_pdf[32]",
'PDFCT14n34Up'    : "event_weight*event_weight_pdf[33]",
'PDFCT14n35Up'    : "event_weight*event_weight_pdf[34]",
'PDFCT14n36Up'    : "event_weight*event_weight_pdf[35]",
'PDFCT14n37Up'    : "event_weight*event_weight_pdf[36]",
'PDFCT14n38Up'    : "event_weight*event_weight_pdf[37]",
'PDFCT14n39Up'    : "event_weight*event_weight_pdf[38]",
'PDFCT14n40Up'    : "event_weight*event_weight_pdf[39]",
'PDFCT14n41Up'    : "event_weight*event_weight_pdf[40]",
'PDFCT14n42Up'    : "event_weight*event_weight_pdf[41]",
'PDFCT14n43Up'    : "event_weight*event_weight_pdf[42]",
'PDFCT14n44Up'    : "event_weight*event_weight_pdf[43]",
'PDFCT14n45Up'    : "event_weight*event_weight_pdf[44]",
'PDFCT14n46Up'    : "event_weight*event_weight_pdf[45]",
'PDFCT14n47Up'    : "event_weight*event_weight_pdf[46]",
'PDFCT14n48Up'    : "event_weight*event_weight_pdf[47]",
'PDFCT14n49Up'    : "event_weight*event_weight_pdf[48]",
'PDFCT14n50Up'    : "event_weight*event_weight_pdf[49]",
'PDFCT14n51Up'    : "event_weight*event_weight_pdf[50]",
'PDFCT14n52Up'    : "event_weight*event_weight_pdf[51]",
'PDFCT14n53Up'    : "event_weight*event_weight_pdf[52]",
'PDFCT14n54Up'    : "event_weight*event_weight_pdf[53]",
'PDFCT14n55Up'    : "event_weight*event_weight_pdf[54]",
'PDFCT14n56Up'    : "event_weight*event_weight_pdf[55]",
}

systs_weights_tt_updowns = {
'TuneCUETP8M2T4Down' : 'event_weight',
'TuneCUETP8M2T4Up'   : 'event_weight',
'FSRDown'            : 'event_weight',
'FSRUp'              : 'event_weight',
'HDAMPDown'          : 'event_weight',
'HDAMPUp'            : 'event_weight',
'ISRDown'            : 'event_weight',
'ISRUp'              : 'event_weight',
}

systs_weights_objects = {
'JERDown':  'event_weight',
'JERUp'  :  'event_weight',
'JESDown':  'event_weight',
'JESUp'  :  'event_weight',
'TESDown':  'event_weight',
'TESUp'  :  'event_weight',
}

updown_dtags_to_sys = {
'MC2016_Summer16_TTJets_powheg_CUETP8M2T4down' : 'TuneCUETP8M2T4Down',
'MC2016_Summer16_TTJets_powheg_CUETP8M2T4up'   : 'TuneCUETP8M2T4Up',
'MC2016_Summer16_TTJets_powheg_fsrdown'        : 'FSRDown',
'MC2016_Summer16_TTJets_powheg_fsrup'          : 'FSRUp',
'MC2016_Summer16_TTJets_powheg_hdampDOWN'      : 'HDAMPDown',
'MC2016_Summer16_TTJets_powheg_hdampUP'        : 'HDAMPUp',
'MC2016_Summer16_TTJets_powheg_isrdown'        : 'ISRDown',
'MC2016_Summer16_TTJets_powheg_isrup'          : 'ISRUp',
}

named_systs_weights_all = {'nom': systs_weights_nominal,
'common': systs_weights_common,
'tt_weights': systs_weights_tt,
'tt_hard':  systs_weights_tt_hard,
'tt_pdf':   systs_weights_tt_alpha_pdf,
'tt_alpha': systs_weights_tt_alpha,
'tt_pdf1':  systs_weights_tt_pdf1,
'tt_pdf10': systs_weights_tt_pdf10,
'tt_pdf20': systs_weights_tt_pdf20,
'tt_pdf30': systs_weights_tt_pdf30,
'tt_pdf40': systs_weights_tt_pdf40,
'tt_pdf50': systs_weights_tt_pdf50,
}


systs_weights_all = {}
for s_d in named_systs_weights_all.values():
    systs_weights_all.update(s_d)

systs_weights_all.update(systs_weights_tt_updowns)

named_systs_weights_all_2 = {'nom': systs_weights_nominal,
'common': systs_weights_common,
'obj':    systs_weights_objects,
'tt_weights': systs_weights_tt,
'tt_hard':  systs_weights_tt_hard,
'tt_pdf':   systs_weights_tt_alpha_pdf,
'tt_alpha': systs_weights_tt_alpha,
'tt_pdf1':  systs_weights_tt_pdf1,
'tt_pdf10': systs_weights_tt_pdf10,
'tt_pdf20': systs_weights_tt_pdf20,
'tt_pdf30': systs_weights_tt_pdf30,
'tt_pdf40': systs_weights_tt_pdf40,
'tt_pdf50': systs_weights_tt_pdf50,
}

systs_weights_all_2 = {}
for s_d in named_systs_weights_all_2.values():
    systs_weights_all_2.update(s_d)
systs_weights_all_2.update(systs_weights_tt_updowns)


# ----- event-function weights
def event_function(param_name):
    return lambda ev: getattr(ev, param_name)

# dtags and systematics
std_dtag_systs = {
'data': (['SingleMuon', 'SingleElectron'], ['nom']),
'tt'  : (['MC2016_Summer16_TTJets_powheg'],  ["nom,common", "obj", "tt_weights", "tt_hard", "tt_pdf1", "tt_pdf10", "tt_pdf20", "tt_pdf30", "tt_pdf40", "tt_pdf50,tt_alpha"]), #select_sparse_channels
'other_mc': (['MC2016_Summer16_DYJetsToLL_10to50_amcatnlo',
'MC2016_Summer16_DYJetsToLL_50toInf_madgraph',
'MC2016_Summer16_SingleT_tW_5FS_powheg',
'MC2016_Summer16_SingleTbar_tW_5FS_powheg',
'MC2016_Summer16_W1Jets_madgraph',
'MC2016_Summer16_W2Jets_madgraph',
'MC2016_Summer16_W3Jets_madgraph',
'MC2016_Summer16_W4Jets_madgraph',
'MC2016_Summer16_WJets_madgraph',
'MC2016_Summer16_WWTo2L2Nu_powheg',
'MC2016_Summer16_WWToLNuQQ_powheg',
'MC2016_Summer16_WZTo1L1Nu2Q_amcatnlo_madspin',
'MC2016_Summer16_WZTo1L3Nu_amcatnlo_madspin',
'MC2016_Summer16_WZTo2L2Q_amcatnlo_madspin',
'MC2016_Summer16_WZTo3LNu_powheg',
'MC2016_Summer16_ZZTo2L2Nu_powheg',
'MC2016_Summer16_ZZTo2L2Q_amcatnlo_madspin',
'MC2016_Summer16_schannel_4FS_leptonicDecays_amcatnlo',
'MC2016_Summer16_tchannel_antitop_4f_leptonicDecays_powheg',
'MC2016_Summer16_tchannel_top_4f_leptonicDecays_powheg'], ['nom', 'common', 'obj']),

'qcd_mc': (['MC2016_Summer16_QCD_HT-100-200',
'MC2016_Summer16_QCD_HT-200-300',
'MC2016_Summer16_QCD_HT-300-500',
'MC2016_Summer16_QCD_HT-500-700',
'MC2016_Summer16_QCD_HT-700-1000',
'MC2016_Summer16_QCD_HT-1000-1500',
'MC2016_Summer16_QCD_HT-1500-2000',
'MC2016_Summer16_QCD_HT-2000-Inf'], ['nom'])
}




# selection stages and parameters per object sys variation
# object sys affects the thresholds of event, can move it between categories

systs_objects = {
'JERDown':  'selection_stage_JERDown',
'JERUp'  :  'selection_stage_JERUp'  ,
'JESDown':  'selection_stage_JESDown',
'JESUp'  :  'selection_stage_JESUp'  ,
'TESDown':  'selection_stage_TESDown',
'TESUp'  :  'selection_stage_TESUp'  ,
}

systs_objects_mt_variation = {
'JERUp'    : 'event_met_lep_mt_JERUp',   
'JERDown'  : 'event_met_lep_mt_JERDown', 
'JESUp'    : 'event_met_lep_mt_JESUp',   
'JESDown'  : 'event_met_lep_mt_JESDown', 
'TESUp'    : 'event_met_lep_mt_TESUp',   
'TESDown'  : 'event_met_lep_mt_TESDown', 
}

systs_objects_met_variation = {
'JERUp'    : 'event_met_JERUp.pt()',   
'JERDown'  : 'event_met_JERDown.pt()', 
'JESUp'    : 'event_met_JESUp.pt()',   
'JESDown'  : 'event_met_JESDown.pt()', 
'TESUp'    : 'event_met_TESUp.pt()',   
'TESDown'  : 'event_met_TESDown.pt()', 
}



# standard distrs

'''
distr_ranges = {
    'Mt_lep_met_c': '--custom-range 0,20,40,60,80,100,130,160,200,250',
    'Mt_lep_met_c2': '--custom-range 0,20,40,60,80,100,120,140,170,200,250,500',
    'Mt_lep_met_f':  '--histo-range 20,0,250',
    'met_f':         '--histo-range 20,0,300',
    'met_c':         '--custom-range 0,20,40,60,80,100,120,140,200,500',
    'dilep_mass':    '--histo-range 100,0,400',
    'lep_pt':        '--histo-range 20,0,150',
    'lep_eta':       '--histo-range 26,-2.6,2.6',
    'tau_sv_sign':   '--histo-range 42,-1,20',
    'tau_pt':        '--histo-range 20,0,100',
    'tau_eta':       '--histo-range 26,-2.6,2.6',
    'yield':         '--histo-range 3,0.0,3.0'
}

distrs_leptonic = [('std_mt_vars', 'Mt_lep_met_c'), ('std_mt_vars', 'Mt_lep_met_c2'), ('event_met_lep_mt', 'Mt_lep_met_f'), ('event_dilep_mass', 'dilep_mass'), ('event_leptons[0].pt()', 'lep_pt')]
distrs_tauonic_std  = [('std_mt_vars', 'Mt_lep_met_c'), ('std_mt_vars', 'Mt_lep_met_c2'), ('event_met_lep_mt', 'Mt_lep_met_f'), ('event_dilep_mass', 'dilep_mass'), ('event_leptons[0].pt()', 'lep_pt'),
        ('event_taus[0].pt()', 'tau_pt'), ('event_taus[0].eta()', 'tau_eta'),
        ('event_taus_sv_sign[0]', 'tau_sv_sign')]
'''

# a parameter can change due to object systamtics -- variation of objects in the event
# it happens for kinematic distributions and energy corrections
# variation of jet energy leads to change in MET and corresponding MET-related parameters

# calculation of standard distrs

systs_objects_mt_variation = {
'NOMINAL'  : lambda ev: ev.event_met_lep_mt,
'JERUp'    : lambda ev: ev.event_met_lep_mt_JERUp,
'JERDown'  : lambda ev: ev.event_met_lep_mt_JERDown,
'JESUp'    : lambda ev: ev.event_met_lep_mt_JESUp,
'JESDown'  : lambda ev: ev.event_met_lep_mt_JESDown,
'TESUp'    : lambda ev: ev.event_met_lep_mt_TESUp,
'TESDown'  : lambda ev: ev.event_met_lep_mt_TESDown,
}

systs_objects_met_variation = {
'NOMINAL'  : lambda ev: ev.event_met.pt(),
'JERUp'    : lambda ev: ev.event_met_JERUp.pt(),
'JERDown'  : lambda ev: ev.event_met_JERDown.pt(),
'JESUp'    : lambda ev: ev.event_met_JESUp.pt(),
'JESDown'  : lambda ev: ev.event_met_JESDown.pt(),
'TESUp'    : lambda ev: ev.event_met_TESUp.pt(),
'TESDown'  : lambda ev: ev.event_met_TESDown.pt(),
}

distr_defs = {
    'Mt_lep_met_c':  (systs_objects_mt_variation,  ('custom-range', [0,20,40,60,80,100,130,160,200,250])),
    'Mt_lep_met_c2': (systs_objects_mt_variation,  ('custom-range', [0,20,40,60,80,100,120,140,170,200,250,500])),
    'Mt_lep_met_f':  (systs_objects_mt_variation,  ('histo-range',  [20,0,250])),
    'met_f':         (systs_objects_met_variation, ('histo-range',  [20,0,300])),
    'met_c':         (systs_objects_met_variation, ('custom-range', [0,20,40,60,80,100,120,140,200,500])),
    'dilep_mass':    ({'NOMINAL': lambda ev: ev.event_dilep_mass},       ('histo-range',  [100,0,400])),
    'lep_pt':        ({'NOMINAL': lambda ev: ev.event_leptons[0].pt()},  ('histo-range',  [20,0,150])),
    'lep_eta':       ({'NOMINAL': lambda ev: ev.event_leptons[0].eta()}, ('histo-range',  [26,-2.6,2.6])),
    'tau_sv_sign':   ({'NOMINAL': lambda ev: ev.event_taus_sv_sign[0]},  ('histo-range',  [42,-1,20])),
    'tau_pt':        ({'NOMINAL': lambda ev: ev.event_taus[0].pt()},     ('histo-range',  [20,0,100])),
    'tau_eta':       ({'NOMINAL': lambda ev: ev.event_taus[0].eta()},    ('histo-range',  [26,-2.6,2.6])),
    'yield':         ({'NOMINAL': lambda ev: 1},                         ('histo-range',  [3,0.0,3.0]))
}

# TODO: implement multi-dim histos?

def make_histo(name, histo_range):
    import ctypes
    from ROOT import TH1D
    range_type, bin_edges = histo_range

    if range_type == 'custom-range':
        #bin_edges = [float(b) for b in args.custom_range.split(',')]
        n_bin_edges = len(bin_edges)
        n_bins = n_bin_edges - 1
        logging.debug("making %d bins from %s" % (n_bins, args.custom_range))
        root_bin_edges = (ctypes.c_double * n_bin_edges)(*bin_edges)
        output_histo = TH1D(name, "", n_bins, root_bin_edges)

    elif range_type == 'histo-range':
        n_bins, lbin, rbin = bin_edges
        output_histo = TH1D(name, "", n_bins, lbin, rbin)
    else:
        raise ValueError('UNKNOWN range type %s in %s' % (range_type, name))

    return output_histo

# also a selection stage can change with object variations, events can move between categories
# now it is implemented only for main selection (no control selections have it)

# calculation of standard channels

main_sel_stages = {
'NOMINAL':  lambda ev: ev.selection_stage,
'JERDown':  lambda ev: ev.selection_stage_JERDown,
'JERUp'  :  lambda ev: ev.selection_stage_JERUp  ,
'JESDown':  lambda ev: ev.selection_stage_JESDown,
'JESUp'  :  lambda ev: ev.selection_stage_JESUp  ,
'TESDown':  lambda ev: ev.selection_stage_TESDown,
'TESUp'  :  lambda ev: ev.selection_stage_TESUp  ,
}

#def main_sel_stages(sname, event):
#    if sname in main_selection_stages:
#        return main_selection_stages[sname](ev)
#    else:
#        return main_selection_stages['NOMINAL'](ev)

# new selection stages
std_channels_ev_loop = {
'mu_selSV':          (lambda sel_stage, ev: (sel_stage==  9 or sel_stage==  7) and event_taus_sv_sign[0] > 2.5, main_sel_stages),
'mu_selSV_ss':       (lambda sel_stage, ev: (sel_stage==  8 or sel_stage==  6) and event_taus_sv_sign[0] > 2.5, main_sel_stages),
'el_selSV':          (lambda sel_stage, ev: (sel_stage== 19 or sel_stage== 17) and event_taus_sv_sign[0] > 2.5, main_sel_stages),
'el_selSV_ss':       (lambda sel_stage, ev: (sel_stage== 18 or sel_stage== 16) and event_taus_sv_sign[0] > 2.5, main_sel_stages),
'mu_selSVVloose':    (lambda sel_stage, ev: (sel_stage==  9 or sel_stage==  7 or sel_stage==  5) and event_taus_sv_sign[0] > 2.5, main_sel_stages),
'mu_selSVVloose_ss': (lambda sel_stage, ev: (sel_stage==  8 or sel_stage==  6 or sel_stage==  4) and event_taus_sv_sign[0] > 2.5, main_sel_stages),
'el_selSVVloose':    (lambda sel_stage, ev: (sel_stage== 19 or sel_stage== 17 or sel_stage== 15) and event_taus_sv_sign[0] > 2.5, main_sel_stages),
'el_selSVVloose_ss': (lambda sel_stage, ev: (sel_stage== 18 or sel_stage== 16 or sel_stage== 14) and event_taus_sv_sign[0] > 2.5, main_sel_stages),

'mu_selTight':     (lambda sel_stage, ev: (sel_stage==  9), main_sel_stages),
'mu_selTight_ss':  (lambda sel_stage, ev: (sel_stage==  8), main_sel_stages),
'el_selTight':     (lambda sel_stage, ev: (sel_stage== 19), main_sel_stages),
'el_selTight_ss':  (lambda sel_stage, ev: (sel_stage== 18), main_sel_stages),
'mu_sel':          (lambda sel_stage, ev: (sel_stage==  9 or sel_stage==  7), main_sel_stages),
'mu_sel_ss':       (lambda sel_stage, ev: (sel_stage==  8 or sel_stage==  6), main_sel_stages),
'el_sel':          (lambda sel_stage, ev: (sel_stage== 19 or sel_stage== 17), main_sel_stages),
'el_sel_ss':       (lambda sel_stage, ev: (sel_stage== 18 or sel_stage== 16), main_sel_stages),
'mu_selVloose':    (lambda sel_stage, ev: (sel_stage==  9 or sel_stage==  7 or sel_stage ==  5), main_sel_stages),
'mu_selVloose_ss': (lambda sel_stage, ev: (sel_stage==  8 or sel_stage==  6 or sel_stage ==  4), main_sel_stages),
'el_selVloose':    (lambda sel_stage, ev: (sel_stage== 19 or sel_stage== 17 or sel_stage == 15), main_sel_stages),
'el_selVloose_ss': (lambda sel_stage, ev: (sel_stage== 18 or sel_stage== 16 or sel_stage == 14), main_sel_stages),

'mu_selTight_ljout':     (lambda sel_stage, ev: (sel_stage==  9) and ev.event_jets_lj_var >  60., main_sel_stages),
'mu_selTight_ljout_ss':  (lambda sel_stage, ev: (sel_stage==  8) and ev.event_jets_lj_var >  60., main_sel_stages),
'el_selTight_ljout':     (lambda sel_stage, ev: (sel_stage== 19) and ev.event_jets_lj_var >  60., main_sel_stages),
'el_selTight_ljout_ss':  (lambda sel_stage, ev: (sel_stage== 18) and ev.event_jets_lj_var >  60., main_sel_stages),
'mu_sel_ljout':          (lambda sel_stage, ev: (sel_stage==  9 or sel_stage==  7) and ev.event_jets_lj_var >  60., main_sel_stages),
'mu_sel_ljout_ss':       (lambda sel_stage, ev: (sel_stage==  8 or sel_stage==  6) and ev.event_jets_lj_var >  60., main_sel_stages),
'el_sel_ljout':          (lambda sel_stage, ev: (sel_stage== 19 or sel_stage== 17) and ev.event_jets_lj_var >  60., main_sel_stages),
'el_sel_ljout_ss':       (lambda sel_stage, ev: (sel_stage== 18 or sel_stage== 16) and ev.event_jets_lj_var >  60., main_sel_stages),
'mu_selVloose_ljout':    (lambda sel_stage, ev: (sel_stage==  9 or sel_stage==  7 or sel_stage==  5) and ev.event_jets_lj_var >  60., main_sel_stages),
'mu_selVloose_ljout_ss': (lambda sel_stage, ev: (sel_stage==  8 or sel_stage==  6 or sel_stage==  4) and ev.event_jets_lj_var >  60., main_sel_stages),
'el_selVloose_ljout':    (lambda sel_stage, ev: (sel_stage== 19 or sel_stage== 17 or sel_stage== 15) and ev.event_jets_lj_var >  60., main_sel_stages),
'el_selVloose_ljout_ss': (lambda sel_stage, ev: (sel_stage== 18 or sel_stage== 16 or sel_stage== 14) and ev.event_jets_lj_var >  60., main_sel_stages),

'mu_selTight_lj':     (lambda sel_stage, ev: (sel_stage==  9) and ev.event_jets_lj_var <= 60., main_sel_stages),
'mu_selTight_lj_ss':  (lambda sel_stage, ev: (sel_stage==  8) and ev.event_jets_lj_var <= 60., main_sel_stages),
'el_selTight_lj':     (lambda sel_stage, ev: (sel_stage== 19) and ev.event_jets_lj_var <= 60., main_sel_stages),
'el_selTight_lj_ss':  (lambda sel_stage, ev: (sel_stage== 18) and ev.event_jets_lj_var <= 60., main_sel_stages),
'mu_sel_lj':          (lambda sel_stage, ev: (sel_stage==  9 or sel_stage==  7) and ev.event_jets_lj_var <= 60., main_sel_stages),
'mu_sel_lj_ss':       (lambda sel_stage, ev: (sel_stage==  8 or sel_stage==  6) and ev.event_jets_lj_var <= 60., main_sel_stages),
'el_sel_lj':          (lambda sel_stage, ev: (sel_stage== 19 or sel_stage== 17) and ev.event_jets_lj_var <= 60., main_sel_stages),
'el_sel_lj_ss':       (lambda sel_stage, ev: (sel_stage== 18 or sel_stage== 16) and ev.event_jets_lj_var <= 60., main_sel_stages),
'mu_selVloose_lj':    (lambda sel_stage, ev: (sel_stage==  9 or sel_stage==  7 or sel_stage==  5) and ev.event_jets_lj_var <= 60., main_sel_stages),
'mu_selVloose_lj_ss': (lambda sel_stage, ev: (sel_stage==  8 or sel_stage==  6 or sel_stage==  4) and ev.event_jets_lj_var <= 60., main_sel_stages),
'el_selVloose_lj':    (lambda sel_stage, ev: (sel_stage== 19 or sel_stage== 17 or sel_stage== 15) and ev.event_jets_lj_var <= 60., main_sel_stages),
'el_selVloose_lj_ss': (lambda sel_stage, ev: (sel_stage== 18 or sel_stage== 16 or sel_stage== 14) and ev.event_jets_lj_var <= 60., main_sel_stages),

# additional channels
'dy_mutau': (lambda sel_stage, ev: (sel_stage== 102 or sel_stage== 103), {'NOMINAL': lambda _, ev: ev.selection_stage_dy}),
'dy_eltau': (lambda sel_stage, ev: (sel_stage== 112 or sel_stage== 113), {'NOMINAL': lambda _, ev: ev.selection_stage_dy}),
'dy_mumu':  (lambda sel_stage, ev: (sel_stage== 102 or sel_stage== 103 or sel_stage== 105), {'NOMINAL': lambda _, ev: ev.selection_stage_dy_mumu}),
'dy_elel':  (lambda sel_stage, ev: (sel_stage== 112 or sel_stage== 113 or sel_stage== 115), {'NOMINAL': lambda _, ev: ev.selection_stage_dy_mumu}),

'tt_elmu':  (lambda sel_stage, ev: (sel_stage== 205), lambda _, ev: ev.selection_stage_em),
}
# calculation of standard systematic weights


