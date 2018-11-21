#!/usr/bin/env python
import argparse
import gc
import sys
import os


# Plot the flat histogram with one root file and sample
def Plot_flat(rd, processes, channels, cuts, plots):

    for i in range(len(processes)):
        for j in range(len(channels)):
            for k in range(len(cuts)):
                for l in range(len(plots)):

                    print("-----Start generating plots-----\n")
                    # Retrieve the full path of process
                    process_input = processes_dictionary().get(processes[i]+"-"+channels[j])
                    print("process_input = ", process_input)

                    # Get the histograms by the TQSampleFolder
                    if 	rd.hasHistogram(process_input,cuts[k]+"/"+plots[l],"errors.drawStatMC=true"):
                        hist_flat = rd.getHistogram(process_input,cuts[k]+"/"+plots[l],"errors.drawStatMC=true")
                    else:
                        print("No plots for the process {:s} in {:s}/{:s}".format(process_input, cuts[k], plots[l]))
                        continue

                    hist_flat.Sumw2()

                    # Normalize the plot to unit area
                    if args.normalize:
                        if hist_flat.Integral() == 0:
                            print("Integral of plots is 0")
                            continue
                        else:
                            print("Normalize to unit area")
                            norm = 1
                            scale_flat = norm/(hist_flat.Integral())
                            hist_flat.Scale(scale_flat)
                    else:
                        print("Normalize to XSec")

                    # Book the canvas for the plot
                    c =  TCanvas("canvas", "canvas", 800, 850)
                    c.cd()

                    # Set up the options for the plots
                    plot_flat_setup(hist_flat)

                    # Draw the latex line for the plots
                    if channels[j] == "em":
                        latex =  TLatex(0.15, 0.8, " #bf{ #splitline{ATLAS Private}{H#rightarrowWW#rightarrowe#mu} }")
                    if channels[j] == "me":
                        latex =  TLatex(0.15, 0.8, " #bf{ #splitline{ATLAS Private}{H#rightarrowWW#rightarrow#mue} }")
                    if channels[j] == "emme":
                        latex =  TLatex(0.15, 0.8, " #bf{ #splitline{ATLAS Private}{H#rightarrowWW#rightarrowe#mu+#mue} }")

                    latex.SetTextSize(0.035)
                    latex.SetNDC()
                    latex.Draw("SAME")

                    # Draw the info on the plots (data/MC)
                    if processes[i] == "data":
                        latex.DrawLatex(0.166,0.725,"#bf{ data }")
                    else:
                        latex.DrawLatex(0.166,0.725,"#bf{ mc }")
                        # latex.DrawLatex(0.16,0.725,"mc16a");

                    # Draw the info on the plots (cuts/)
                    latex_for_cuts_plots = TLatex(0.9, 0.9,"#bf{"+cuts[k]+"/"+plots[l]+"}")
                    latex_for_cuts_plots.SetTextAlign(31)
                    latex_for_cuts_plots.SetTextSize(0.025)
                    latex_for_cuts_plots.SetNDC()
                    latex_for_cuts_plots.Draw("SAME")


                    # Draw the legend for the plots
                    leg = TLegend(0.60,0.8,0.80,0.85)
                    obj_legend = leg.AddEntry("hist_flat",processes[i],"f")

                    obj_legend.SetFillColor(kRed-7)
                    obj_legend.SetFillStyle(3345)
                    obj_legend.SetLineColor(kBlack)


                    leg.SetBorderSize(0)
                    leg.SetTextSize(0.03)
                    leg.SetTextFont(42)
                    leg.Draw("SAME")


                    if args.outputfolder:
                        if os.path.isdir(args.outputfolder):
                            # print(args.outputfolder[-1:])
                            if args.outputfolder[-1:] != "/":
                                args.outputfolder = args.outputfolder + "/"

                            c.SaveAs(args.outputfolder+cuts[k]+"-"+plots[l]+"-"+channels[j]+"-"+processes[i]+".pdf","pdf")
                        else:
                            os.system("mkdir -p "+args.outputfolder)
                    else:
                        c.SaveAs(args.outputfolder+cuts[k]+"-"+plots[l]+"-"+channels[j]+"-"+processes[i]+".pdf","pdf")

                    print("-----End of generating plots-----\n")


# Plot the comparison of histogram with root files and samples
def Plot_compare(rdUp, rdDown, processes, channels, cuts, plots):

    for i in range(len(processes)):
        for j in range(len(channels)):
            for k in range(len(cuts)):
                for l in range(len(plots)):

                    print("-----Start generating plots-----\n")
                    # Retrieve the full path of process
                    process_input = processes_dictionary().get(processes[i]+"-"+channels[j])
                    print("process_input = ", process_input)

                    # Get the histograms by the TQSampleFolder
                    if 	rdUp.hasHistogram(process_input,cuts[k]+"/"+plots[l],"errors.drawStatMC=true"):
                        hist_flat = rd.getHistogram(process_input,cuts[k]+"/"+plots[l],"errors.drawStatMC=true")
                    else:
                        print("No plots for the process {:s} in {:s}/{:s}".format(process_input, cuts[k], plots[l]))
                        continue

                    if 	rdDown.hasHistogram(process_input,cuts[k]+"/"+plots[l],"errors.drawStatMC=true"):
                        hist_flat = rd.getHistogram(process_input,cuts[k]+"/"+plots[l],"errors.drawStatMC=true")
                    else:
                        print("No plots for the process {:s} in {:s}/{:s}".format(process_input, cuts[k], plots[l]))
                        continue

                    hist_flat.Sumw2()

                    # Normalize the plot to unit area
                    if args.normalize:
                        if hist_flat.Integral() == 0:
                            print("Integral of plots is 0")
                            continue
                        else:
                            print("Normalize to unit area")
                            norm = 1
                            scale_flat = norm/(hist_flat.Integral())
                            hist_flat.Scale(scale_flat)
                    else:
                        print("Normalize to XSec")

                    # Book the canvas for the plot
                    c =  TCanvas("canvas", "canvas", 800, 850)
                    c.cd()

                    # Set up the options for the plots
                    plot_flat_setup(hist_flat)

                    # Draw the latex line for the plots
                    if channels[j] == "em":
                        latex =  TLatex(0.15, 0.8, " #bf{ #splitline{ATLAS Private}{H#rightarrowWW#rightarrowe#mu} }")
                    if channels[j] == "me":
                        latex =  TLatex(0.15, 0.8, " #bf{ #splitline{ATLAS Private}{H#rightarrowWW#rightarrow#mue} }")
                    if channels[j] == "emme":
                        latex =  TLatex(0.15, 0.8, " #bf{ #splitline{ATLAS Private}{H#rightarrowWW#rightarrowe#mu+#mue} }")

                    latex.SetTextSize(0.035)
                    latex.SetNDC()
                    latex.Draw("SAME")

                    # Draw the info on the plots (data/MC)
                    if processes[i] == "data":
                        latex.DrawLatex(0.166,0.725,"#bf{ data }")
                    else:
                        latex.DrawLatex(0.166,0.725,"#bf{ mc }")
                        # latex.DrawLatex(0.16,0.725,"mc16a");

                    # Draw the info on the plots (cuts/)
                    latex_for_cuts_plots = TLatex(0.9, 0.9,"#bf{"+cuts[k]+"/"+plots[l]+"}")
                    latex_for_cuts_plots.SetTextAlign(31)
                    latex_for_cuts_plots.SetTextSize(0.025)
                    latex_for_cuts_plots.SetNDC()
                    latex_for_cuts_plots.Draw("SAME")


                    # Draw the legend for the plots
                    leg = TLegend(0.60,0.8,0.80,0.85)
                    obj_legend = leg.AddEntry("hist_flat",processes[i],"f")

                    obj_legend.SetFillColor(kRed-7)
                    obj_legend.SetFillStyle(3345)
                    obj_legend.SetLineColor(kBlack)


                    leg.SetBorderSize(0)
                    leg.SetTextSize(0.03)
                    leg.SetTextFont(42)
                    leg.Draw("SAME")


                    if args.outputfolder:
                        if os.path.isdir(args.outputfolder):
                            # print(args.outputfolder[-1:])
                            if args.outputfolder[-1:] != "/":
                                args.outputfolder = args.outputfolder + "/"

                            c.SaveAs(args.outputfolder+cuts[k]+"-"+plots[l]+"-"+channels[j]+"-"+processes[i]+".pdf","pdf")
                        else:
                            os.system("mkdir -p "+args.outputfolder)
                    else:
                        c.SaveAs(args.outputfolder+cuts[k]+"-"+plots[l]+"-"+channels[j]+"-"+processes[i]+".pdf","pdf")

                    print("-----End of generating plots-----\n")






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

        # Load lists
        processes = Fun_processes()
        channels = Fun_channels()
        cuts = Fun_cuts()
        plots = Fun_plots()

        # The plots I booked in the PlotSetup
        print(processes)
        # The cuts I booked in the PlotSetup
        print(cuts)
        Plot_flat(rd, processes, channels, cuts, plots)

    if args.compare:
        # Load the sample folder in the root file
        if args.compare_inputfileUp and args.compare_inputfileDown:
            SampleFolderUp = TQSampleFolder.loadSampleFolder(args.compare_inputfileUp+":samples")
            SampleFolderDown = TQSampleFolder.loadSampleFolder(args.compare_inputfileDown+":samples")

        else:
            print("Please pass a input root file!")

        # Check the TQSampleDataReader for the plots
        rdUp = TQSampleDataReader(SampleFolderUp)
        rdDown = TQSampleDataReader(SampleFolderDown)


        processes = Fun_processes()
        channels = Fun_channels()
        cuts = Fun_cuts()
        plots = Fun_plots()

        # The plots I booked in the PlotSetup
        print(processes)
        # The cuts I booked in the PlotSetup
        print(cuts)

        Plot_flat(rdUp, rdDown, processes, channels, cuts, plots)

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


  parser.add_argument('--diffproc', '-d', dest="diff", action="store_const", const=True, default=False, help='Only run with two root files and make the comparison plots')


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
