from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

version = 'v12-7_test1' # PARAMETER
suffix  = '' # PARAMETER for ext datasets of MC (they don't differ in primary name)
dtag    = 'MC2016_Summer16_TTJets_powheg' # PARAMETER
dset    = '/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM' # PARAMETER
LumiMask = '' # PARAMETER

request_tag = 'Ntupler_' + version + suffix # apparently it's the only place to distinguish ext datasets of MC for crab

config.General.requestName = request_tag
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'python/crab_cfgs/' + dtag + suffix + '_cfg.py'

config.Data.inputDataset = dset
config.Data.inputDBS = 'global'
if not LumiMask:
    config.Data.splitting = 'FileBased'
    config.Data.unitsPerJob = 10
else
    config.Data.splitting = 'LumiBased'
    config.Data.unitsPerJob = 20
    config.Data.lumiMask = LumiMask

config.Data.outLFNDirBase = '/store/user/%s/%s/' % (getUsernameFromSiteDB(), version)
config.Data.publication = False
config.Data.outputDatasetTag = request_tag

config.Site.storageSite = 'T2_PT_NCG_Lisbon'

