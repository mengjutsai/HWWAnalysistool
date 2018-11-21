#!/usr/bin/env python
import argparse
import gc
import sys
import os

def CheckOutputDirectory(outputfolder):

    if outputfolder:
        if outputfolder[-1:] != "/":
            outputfolder = outputfolder + "/"
        print(outputfolder)

        if os.path.isdir(outputfolder):
            print("The folder already existed")
        else:
            os.system("mkdir -p "+outputfolder)
    else:
        outputfolder = "results/tmp/"

    return outputfolder





def main(args):

    # Calculate the time for the program
    start = timeit.default_timer()

    if args.flat:
        # Load the sample folder in the root file
        if args.inputfile:
            SampleFolder = TQSampleFolder.loadSampleFolder(args.inputfile+":samples")
        else:
            print("Please pass a input root file!")

        # Check the TQSampleDataReader for the plots
        rd = TQSampleDataReader(SampleFolder)
        if args.printHist:
            rd.printListOfHistograms()
        # Load lists
        processes = Fun_processes()
        channels = Fun_channels()
        cuts = Fun_cuts()
        plots = Fun_plots()

        # The plots I booked in the PlotSetup
        print(processes)
        # The cuts I booked in the PlotSetup
        print(cuts)

        # Check we have output directory
        outputfolder = CheckOutputDirectory(args.outputfolder)

        for i in range(len(processes)):
            for j in range(len(channels)):
                for k in range(len(cuts)):
                    for l in range(len(plots)):
                        histogram = PrepareHist(rd, processes[i], channels[j], cuts[k], plots[l])
                        if histogram == 0:
                            continue
                        NormalizeToUnitArea(histogram, args.normalize)

                        c = prepareCanvas()

                        SetupHist(histogram)
                        print(channels[j])
                        ATLASstyle(channels[j])
                        DrawInformation(args.info)

                        # Main legend
                        leg = TLegend(0.60,0.8,0.80,0.85)
                        SetupMainPlotLegend(leg)
                        AddEntry_MainPlotLegend(leg, histogram, processes[i])
                        leg.Draw("SAME")

                        DrawCutStage(cuts[k], plots[l])

                        #Subplot legend
                        # leg_sub = TLegend(0.65,0.65,0.85,0.85)
                        print("Store plots in {:s}".format(args.outputfolder))
                        c.SaveAs(outputfolder+cuts[k]+"-"+plots[l]+"-"+channels[j]+"-"+processes[i]+".pdf","pdf")





    if args.compare: # two plot comparison


        if args.compare_inputfileUp and args.compare_inputfileDown:
            InputFileList = []
            InputFileList.append(args.compare_inputfileUp)
            InputFileList.append(args.compare_inputfileDown)
        else:
            print("Please pass a input root file!")
            return 0

        SampleFolder = []
        rd = []

        for i in range(2):

            # Load the sample folder in the root file
            SampleFolder.append(TQSampleFolder.loadSampleFolder(InputFileList[i]+":samples"))

            # Check the TQSampleDataReader for the plots
            rd.append(TQSampleDataReader(SampleFolder[i]))

            if args.printHist:
                rd[i].printListOfHistograms()

        # processes = Fun_processes()
        channels = Fun_channels()
        cuts = Fun_cuts()
        plots = Fun_plots()

        # The plots I booked in the PlotSetup
        # print(processes)
        # The cuts I booked in the PlotSetup
        print(cuts)

        # Check we have output directory
        outputfolder = CheckOutputDirectory(args.outputfolder)

        # Run with different processes
        # if args.diffprocess:
        for j in range(len(channels)):
            for k in range(len(cuts)):
                for l in range(len(plots)):

                    c = prepareCanvas()

                    pad_main = prepareMainPad(args.compare)
                    pad_ratio = prepareSubPad(args.compare)

                    ColorList = ColorOrder()

                    leg = TLegend(0.45,0.65,0.60,0.85)
                    leg_sub = TLegend(0.65,0.65,0.85,0.85)

                    processes = []
                    processes.append(args.compare_ProcessUp)
                    processes.append(args.compare_ProcessDown)

                    pad_main.cd()

                    histogram = []
                    for i in range(2):
                        hist = PrepareHist(rd[i], processes[i], channels[j], cuts[k], plots[l])
                        histogram.append(hist)

                    if histogram[0] == 0 or histogram[1] == 0:
                        continue

                    for i in range(2):
                        NormalizeToUnitArea(histogram[i], args.normalize)

                        SetupHist(histogram[i], ColorList[i])

                        # Main legend
                        AddEntry_MainPlotLegend(leg, histogram[i], processes[i])
                        SetupMainPlotLegend(leg)

                    hist_ratio = prepareRatio(args.compare, histogram[0], histogram[1])

                    #Subplot legend
                    SetupSubPlotLegend(leg_sub)

                    if args.sublegendname:
                        AddEntry_SubPlotLegend(leg_sub, hist_ratio, args.sublegendname)
                    else:
                        AddEntry_SubPlotLegend(leg_sub, hist_ratio, "")

                    ATLASstyle(channels[j])
                    DrawInformation(args.info)
                    DrawCutStage(cuts[k], plots[l])

                    leg.Draw("SAME")
                    leg_sub.Draw("SAME")

                    pad_ratio.cd()

                    SetupSubPlot(hist_ratio, histogram[0])

                    DrawDashedLine_SubPlot(hist_ratio)



                    print("Store plots in {:s}".format(args.outputfolder))
                    c.SaveAs(outputfolder+cuts[k]+"-"+plots[l]+"-"+channels[j]+".pdf","pdf")





    stop = timeit.default_timer()
    print "Min = {:d}, {:d}, Second = {:.2f}".format(int((stop - start)/60), int(stop - start)%60, stop - start)







if __name__ == "__main__":
  # parse the CLI arguments
  parser = argparse.ArgumentParser(description='Plotting tool for HWW')

  # For the flat mode
  parser.add_argument('--flat', '-f', dest="flat", action="store_const", const=True, default=False, help='Only run with one root file and create flat plot')
  parser.add_argument('--input', '-i', metavar='INPUT', type=str, dest="inputfile", default="input/20180618_R21_mc16a_p3387_w_PRW_UpdateLumi_v1.root", help='ROOT file with input sample folder')
  parser.add_argument('--normalize', '-n', dest="normalize", action="store_const", const=True, default=False, help='Normalize the plot to unit area')
  parser.add_argument('--outputfolder', '-o', metavar='OUTPUT', type=str, dest="outputfolder", default="results/tmp/", help='outputfolder for plots')

  parser.add_argument('--compare', '-c', dest="compare", action="store_const", const=True, default=False, help='Run with two root files and make the comparison plots')
  parser.add_argument('--i1', metavar='INPUT', type=str, dest="compare_inputfileUp", default="input/20180618_R21_mc16a_p3387_w_PRW_UpdateLumi_v1.root", help='Comparison plot with input 1')
  parser.add_argument('--i2', metavar='INPUT', type=str, dest="compare_inputfileDown", default="input/20180618_R21_mc16a_p3387_w_PRW_UpdateLumi_v1.root", help='Comparison plot with input 2')

  parser.add_argument('--diffprocess', '-d', dest="diffprocess", action="store_const", const=True, default=False, help='Compare with diff processes')
  parser.add_argument('--p1', metavar='INPUT', type=str, dest="compare_ProcessUp", default="input/20180618_R21_mc16a_p3387_w_PRW_UpdateLumi_v1.root", help='Comparison plot with input 1')
  parser.add_argument('--p2', metavar='INPUT', type=str, dest="compare_ProcessDown", default="input/20180618_R21_mc16a_p3387_w_PRW_UpdateLumi_v1.root", help='Comparison plot with input 2')


  parser.add_argument('--info', metavar='info', type=str, dest="info", default="", help='Adding addtional string on the plot')
  parser.add_argument('--sublegendname', '--sln', metavar='sublegendname', type=str, dest="sublegendname", default="", help='Adding legend name of subplot')
  parser.add_argument('--printHist', '--ph', dest="printHist", action="store_const", const=True, default=False, help='Print list of histograms')

  # parser.add_argument('--rd', dest="rd", action="store_const", const=True, default=False, help='Check TQSampleDataReader to see the plots in the sample folder')


  # parser.add_argument('--cuts', '-c', metavar='*CUT*', type=str, dest="cuts", default=["CutGGF_TopoDPhill_0jet","CutGGF_TopoDPhill_1jet"], nargs='+', help='filter for cuts to plot distributions')
  parser.add_argument('--samplename', '-s', metavar='NAME', type=str, dest="samplename", default=["ggf","Vgamma/Wgamma","diboson/NonWW/qq/WZgammaStar","Wjets","WjetsCompB"], nargs='+', help='list of the processes for plotting')
  parser.add_argument('--append', dest="append", action="store_const", const=True, default=False,help='append to the output file (instead of overwriting)')
  parser.add_argument('--observable', metavar='obs', type=str, dest="observable", default=["Mll_3", "subleadLepPt_3"], nargs='+', help='list of the 1D observables to be plotted')
  args = parser.parse_args()

  # setup ROOT
  from QFramework import *
  from ROOT import *
  from PlotSetup import *

  import timeit
  import time

  # close to open window when generating plots
  gROOT.SetBatch(True)

  # disable garbage collection
  gc.disable()


  # call the main function
  main(args);
