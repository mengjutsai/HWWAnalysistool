from QFramework import *
from ROOT import *

def Fun_plots():
    Arr_plots = []
    Arr_plots.append("leadJetPt")
    Arr_plots.append("subleadJetPt")
    Arr_plots.append("leadJetEta")
    Arr_plots.append("subleadJetEta")
    Arr_plots.append("leadJetPhi")
    Arr_plots.append("subleadJetPhi")
    Arr_plots.append("leadJetPt_Forward")
    Arr_plots.append("subleadJetPt_Forward")
    Arr_plots.append("leadJetPt_Central")
    Arr_plots.append("subleadJetPt_Central")
    Arr_plots.append("Jet1_Pt")
    Arr_plots.append("Jet2_Pt")
    Arr_plots.append("Jet1_Eta")
    Arr_plots.append("Jet2_Eta")
    Arr_plots.append("Jet1_Phi")
    Arr_plots.append("Jet2_Phi")
    Arr_plots.append("Jet3_Pt")
    Arr_plots.append("Jet4_Pt")
    Arr_plots.append("Jet3_Eta")
    Arr_plots.append("Jet4_Eta")
    Arr_plots.append("Jet3_Phi")
    Arr_plots.append("Jet4_Phi")
    Arr_plots.append("leadLepPt")
    Arr_plots.append("subleadLepPt")
    Arr_plots.append("leadLepEta")
    Arr_plots.append("subleadLepEta")
    Arr_plots.append("leadLepPhi")
    Arr_plots.append("subleadLepPhi")
    Arr_plots.append("MET")
    Arr_plots.append("METPhi")
    Arr_plots.append("Mll")
    Arr_plots.append("DPhill")
    Arr_plots.append("MT")
    Arr_plots.append("Mjj")
    Arr_plots.append("DYjj")
    Arr_plots.append("contOLV")
    Arr_plots.append("SumOFMLepxJety")
    Arr_plots.append("PtTot")
    Arr_plots.append("mtt")
    Arr_plots.append("nJetsTight")
    Arr_plots.append("contOLV_b")
    Arr_plots.append("OLV")
    Arr_plots.append("Ptll")
    Arr_plots.append("DRll")
    Arr_plots.append("DEtall")
    Arr_plots.append("DPhillMET")
    Arr_plots.append("MTlep0")
    Arr_plots.append("MTlep1")
    Arr_plots.append("PTjj")
    Arr_plots.append("DPhil0j0")
    Arr_plots.append("DPhil0j1")
    Arr_plots.append("DPhil1j0")
    Arr_plots.append("DPhil1j1")
    Arr_plots.append("DEtal0j0")
    Arr_plots.append("DEtal0j1")
    Arr_plots.append("DEtal1j0")
    Arr_plots.append("DEtal1j1")

    Arr_plots.append("DRl0j0")
    Arr_plots.append("DRl0j1")
    Arr_plots.append("DRl1j0")
    Arr_plots.append("DRl1j1")
    Arr_plots.append("DRjj")
    Arr_plots.append("DPhil0MET")
    Arr_plots.append("DPhil1MET")
    Arr_plots.append("pTTot_nJets")
    Arr_plots.append("centralJetVetoLeadpT")
    Arr_plots.append("MT2_1jet")
    Arr_plots.append("MT2_2jet")

    Arr_plots.append("ScalarJets")
    Arr_plots.append("ScalarALL")
    Arr_plots.append("nInteraction")
    Arr_plots.append("nInteraction_old_1_09")
    Arr_plots.append("nInteraction_new_1_03")
    Arr_plots.append("actualInteractionsPerCrossin_1_09")
    Arr_plots.append("actualInteractionsPerCrossing_1_03")
    Arr_plots.append("MCweights_Large")
    Arr_plots.append("MCweights_Medium")
    Arr_plots.append("MCweights_Small")
    Arr_plots.append("PUweight")
    Arr_plots.append("PUweight_UseGetWeight")
    Arr_plots.append("Lepweights")
    Arr_plots.append("EleIDweights")
    Arr_plots.append("EleIsoweights")
    Arr_plots.append("MuonIsoweights")
    Arr_plots.append("MuonTTVAweights")
    Arr_plots.append("ttbarNNLOweights")
    Arr_plots.append("singleTrigWeightweights")
    Arr_plots.append("bTagweights")
    Arr_plots.append("bTagTrackJetweights")
    Arr_plots.append("jetJVTweights")
    Arr_plots.append("jetForwardJVTweights")



    Arr_plots.append("nPV")
    Arr_plots.append("MaxMTlep")

    Arr_plots.append("nJet")

    return Arr_plots

def Fun_cuts():
    Arr_cuts = []
    Arr_cuts.append("CutChannels")
    Arr_cuts.append("CutFF")
    Arr_cuts.append("CutMET")
    Arr_cuts.append("CutGGF_0jet")
    Arr_cuts.append("CutGGF_1jet")
    Arr_cuts.append("CutGGF_SR_bVeto_0jet")
    Arr_cuts.append("CutGGF_TopoDPhill_1jet")
    Arr_cuts.append("CutVBF_2jet")
    Arr_cuts.append("CutVBFbVeto_2jet")
    Arr_cuts.append("CutVBFTopControl_2jetinclZttVeto")


    return Arr_cuts

def Fun_channels():
    Arr_channels = []
    Arr_channels.append("em")
    Arr_channels.append("me")
    Arr_channels.append("emme")
    return Arr_channels

def Fun_processes():
    Arr_processes = []
    Arr_processes.append("VBF")
    Arr_processes.append("GGF")
    Arr_processes.append("WW")
    Arr_processes.append("Top")
    Arr_processes.append("Zjets")
    return Arr_processes

# def process_to_run(processes, channels):
#     for i in range(len(processes)):
#         for j in range(len(channels)):
#             print(processes_dictionary().get(processes[i]+"-"+channels[j]))



def processes_dictionary():
    dictionary = {"data-em":"/data/em",
                  "data-me":"/data/me",
                  "data-emme":"/data/[em+me]",

                  "VBF-em":"/sig/em/mh125/vbf",
                  "VBF-me":"/sig/me/mh125/vbf",
                  "VBF-emme":"/sig/[em+me]/mh125/vbf",

                  "GGF-em":"/sig/em/mh125/ggf",
                  "GGF-me":"/sig/me/mh125/ggf",
                  "GGF-emme":"/sig/[em+me]/mh125/ggf",

                  "WW-em":"/bkg/em/diboson/WW",
                  "WW-me":"/bkg/me/diboson/WW",
                  "WW-emme":"/bkg/[em+me]/diboson/WW",

                  "Top-em":"/bkg/em/top",
                  "Top-me":"/bkg/me/top",
                  "Top-emme":"/bkg/[em+me]/top",

                  "Zjets-em":"/sig/em/Zjets",
                  "Zjets-me":"/sig/me/Zjets",
                  "Zjets-emme":"/sig/[em+me]/Zjets",
    }
    return dictionary


def PrepareHist(rd, Actual_processes, Actual_channels, Actual_cuts, Actual_plots):

    print("Prepare histogram with {:s}, {:s}, {:s}, {:s}\n".format(Actual_cuts,Actual_plots, Actual_channels, Actual_processes))
    ProcessName = processes_dictionary().get(Actual_processes+"-"+Actual_channels)

    if 	rd.hasHistogram(ProcessName,Actual_cuts+"/"+Actual_plots,"errors.drawStatMC=true"):
        hist = rd.getHistogram(ProcessName,Actual_cuts+"/"+Actual_plots,"errors.drawStatMC=true")
        return hist
    else:
        print("No plots for the process {:s} in {:s}/{:s}".format(ProcessName, Actual_cuts, Actual_plots))
        return 0


def NormalizeToUnitArea(hist, Flag):
    if Flag:
        if hist.Integral() == 0:
            print("Integral of plots is 0")
        else:
            print("Normalize to unit area")
            norm = 1
            scale_flat = norm/(hist.Integral())
            hist.Scale(scale_flat)
    else:
            print("Normalize to XSec")

def prepareCanvas():
    canvas =  TCanvas("canvas", "canvas", 800, 850)
    canvas.cd()
    return canvas

        # pad_main.cd()

def prepareMainPad(doSubPlot):
    pad =  TPad("main", "main", 0, 0.3, 1, 1.0)
    pad.SetBottomMargin(0.005)
    pad.Draw("SAME")
    return pad

def prepareSubPad(doSubPlot):
    pad =  TPad("ratio", "ratio", 0, 0.05, 1, 0.3)
    pad.SetTopMargin(0)
    pad.SetBottomMargin(0.2)
    pad.SetGridx()
    pad.Draw("SAME")
    return pad

# def prepareSubPad(doSubPlot):
def ColorOrder():
    ColorList = [2, 1, 600, 210, 219, 594, 6, 28, 39]
    return ColorList

def SetupHist(hist, LineColor = kBlack, FillColor = 0, FillStyle = 0, title = "", DrawOption = "hist E1 SAME"):
    #FillColor = kRed-7, FillStyle = 3345
    hist.SetStats(0)
    hist.SetTitle(title)
    hist.GetXaxis().SetLabelOffset(1.0)

    # Set up the maximum of the y-axis
    HistMax = hist.GetBinContent(hist.GetMaximumBin())
    hist.SetMaximum(1.6*HistMax)
    hist.SetMinimum(0)

    # Set up the line color for the histogram
    hist.SetLineColor(LineColor)
    hist.SetFillColor(FillColor)
    hist.SetFillStyle(FillStyle)

    hist.GetYaxis().SetTitle("Events")

    hist.GetYaxis().SetNdivisions(408)

    hist.GetYaxis().SetTitleSize(18)
    hist.GetYaxis().SetTitleFont(43)
    hist.GetYaxis().SetTitleOffset(1.9)
    hist.GetYaxis().SetLabelFont(43)
    hist.GetYaxis().SetLabelSize(20)

    hist.GetXaxis().SetLimits(hist.GetXaxis().GetXmin(),hist.GetXaxis().GetXmax())
    hist.GetXaxis().SetTitleSize(20)
    hist.GetXaxis().SetTitleFont(43)
    hist.GetXaxis().SetTitleOffset(1.5)
    hist.GetXaxis().SetLabelFont(43)
    hist.GetXaxis().SetLabelSize(20)
    hist.GetXaxis().SetLabelOffset(0.02)

    hist.Draw(DrawOption)

def ATLASstyle(channels_name):
    latex = TLatex()

    latex.SetTextSize(0.05)
    latex.SetNDC()

    if channels_name == "em":
        print("enter in em")
        latex.DrawLatexNDC(0.15, 0.83, "#bf{ #splitline{ATLAS Private}{H#rightarrowWW^{*}#rightarrowe#mu} }")
    if channels_name == "me":
        print("enter in me")
        latex.DrawLatexNDC(0.15, 0.83, "#bf{ #splitline{ATLAS Private}{H#rightarrowWW^{*}#rightarrow#mue} }")
    if channels_name == "emme":
        print("enter in emme")
        latex.DrawLatexNDC(0.15, 0.83, "#bf{ #splitline{ATLAS Private}{H#rightarrowWW^{*}#rightarrowe#mu+#mue} }")


def DrawInformation(Words):
    if Words:
        latex_processes = TLatex()
        latex_processes.SetTextSize(0.05)
        latex_processes.DrawLatexNDC(0.15,0.75,"#bf{ "+Words+" }")


def DrawCutStage(cuts = "", plots = ""):
    latex_for_cuts_plots = TLatex()
    latex_for_cuts_plots.SetTextAlign(31)
    latex_for_cuts_plots.SetTextSize(0.03)
    latex_for_cuts_plots.DrawLatexNDC(0.9, 0.9,"#bf{ Plots: "+cuts+"/"+plots+"}")
    # latex_for_cuts_plots.SetNDC()
    # latex_for_cuts_plots.Draw("SAME")

def SetupMainPlotLegend(leg):
    leg.SetBorderSize(0)
    leg.SetTextSize(0.04)
    leg.SetTextFont(42)

def AddEntry_MainPlotLegend(leg, hist, tag = "VBF"):
    l = leg.AddEntry(hist,tag,"l")
    # l.SetFillColor(FillColor)
    # l.SetFillStyle(FillStyle)
    # l.SetLineColor(LineColor)


def SetupSubPlotLegend(leg):
    leg.SetHeader("Ratios (sub-pad)")
    leg.SetBorderSize(0)
    leg.SetTextSize(0.04)

def AddEntry_SubPlotLegend(leg, RatioHist, Tag = "RatioPlot"):
    leg.AddEntry(RatioHist,Tag,"lep")



def prepareRatio(doSubPlot, HistUp, HistDown):
    if doSubPlot:
        print("Please enable to make subplot")

    RatioHist = HistUp.Clone()
    RatioHist.Divide(HistDown)

    return RatioHist


def SetupSubPlot(RatioHist, hist, LineColor = 2, Ratio_Max = 1.1, Ratio_Min = 0.9):
# hist: pass a histogram for the x-axis range

    RatioHist.GetYaxis().SetTitle("RATIO")

    RatioHist.GetYaxis().SetNdivisions(408)
    RatioHist.SetMaximum(Ratio_Max)
    RatioHist.SetMinimum(Ratio_Min)

    RatioHist.GetYaxis().SetTitleSize(18)
    RatioHist.GetYaxis().SetTitleFont(43)
    RatioHist.GetYaxis().SetTitleOffset(1.8)
    RatioHist.GetYaxis().SetLabelFont(43)
    RatioHist.GetYaxis().SetLabelSize(20)
    RatioHist.GetXaxis().SetLimits(hist.GetXaxis().GetXmin(),hist.GetXaxis().GetXmax())

    RatioHist.GetXaxis().SetTitleSize(20)
    RatioHist.GetXaxis().SetTitleFont(43)
    RatioHist.GetXaxis().SetTitleOffset(3.5)
    RatioHist.GetXaxis().SetLabelFont(43)
    RatioHist.GetXaxis().SetLabelSize(20)
    RatioHist.GetXaxis().SetLabelOffset(0.02)

    RatioHist.SetLineColor(LineColor)
    RatioHist.SetStats(0)
    RatioHist.SetTitle("")
    RatioHist.SetMarkerStyle(8)
    RatioHist.SetMarkerColor(LineColor)
    RatioHist.Draw("hist p E0 SAME")

def DrawDashedLine_SubPlot(hist, Ratio_Max = 1.1, Ratio_Min = 0.9, width = 0.025):
    N_Lines = int((Ratio_Max - Ratio_Min)/width)
    line = TLine()
    line.SetLineColor(1)
    line.SetLineStyle(7)

    for line_it in range(0, N_Lines):
        # print line_it
        if round(Ratio_Min)+(line_it+1)*width==1:
            continue
        line.DrawLine(hist.GetXaxis().GetXmin(),Ratio_Min+(line_it+1)*width,hist.GetXaxis().GetXmax(),Ratio_Min+(line_it+1)*width)

    line.Draw("SAME")
