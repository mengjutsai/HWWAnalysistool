import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import timeit
import math
from matplotlib.legend_handler import HandlerPatch
import matplotlib.patches as mpatches
# from matplotlib import gridspec

def make_legend_arrow(legend, orig_handle,
                      xdescent, ydescent,
                      width, height, fontsize):
    p = mpatches.FancyArrow(0, 0.5*height, width, 0, length_includes_head=True, head_width=0.75*height )
    # p = mpatches.FancyArrow(0, 0.5*height, 0.2, 0, length_includes_head=True, head_width=0.75*height )

    return p

start = timeit.default_timer()
print "Start Running Events ... It will take some times !"
f = open('selected/vbf/Selected-vbf.txt', 'w')
initial_line = "run number   event number     mT    Mll   DPhill     Mjj   DYjj   nJets25   nJets3030   leadLepPt   leadLepEta   leadLepPhi   subleadLepPt   subleadLepEta   subleadLepPhi   leadJetPt   leadJetEta   leadJetPhi   subleadJetPt   subleadJetEta   subleadJetPhi    MET   METPhi   isLeadE   skl   isData\n"
initial_line1 = "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
initial_line = initial_line+initial_line1
f.write(initial_line)

num_lines = sum(1 for line in open('eventlist_v2/evtlist2j-CutVBFZttVeto_2jet-data.txt'))

width_plt = 100
Value_Start_point = 2
list1 = []
with open('eventlist_v2/evtlist2j-CutVBFZttVeto_2jet-data.txt') as fp:
    for index, line in enumerate(fp):
        # if Value_Start_point <= index <= num_lines-1: #Value_Start_point = 2, num_lines-1 = max of line number
        if Value_Start_point <= index <= num_lines-1: #Value_Start_point = 2, num_lines-1 = max of line number
            tmp_line_arr = line.split()
            # #print tmp_line_arr
            if float(tmp_line_arr[24]) >= 0.97: # skl > 0.86
                # if float(tmp_line_arr[5]) > 1000: #mjj > 1000
                # if abs(float(tmp_line_arr[16])) > 3 and abs(float(tmp_line_arr[19])) > 3: #abs of jet0 and jet1 eta > 3
                    # if float(tmp_line_arr[3]) < 60: #mll > 55
                        # if float(tmp_line_arr[4]) < 1: #dphill > 55
                #             if float(tmp_line_arr[2]) > 100 and float(tmp_line_arr[2]) < 135: #mT 100-135
                #                 if abs(float(tmp_line_arr[10])) < 1 and abs(float(tmp_line_arr[13])) < 1: #abs of lep eta < 1
                                    # if float(tmp_line_arr[6]) > 6: #DYJJ > 6

                                                LeadLep_x = float(tmp_line_arr[9]) * math.cos(float(tmp_line_arr[11]))
                                                LeadLep_y = float(tmp_line_arr[9]) * math.sin(float(tmp_line_arr[11]))

                                                SubLeadLep_x = float(tmp_line_arr[12]) * math.cos(float(tmp_line_arr[14]))
                                                SubLeadLep_y = float(tmp_line_arr[12]) * math.sin(float(tmp_line_arr[14]))

                                                LeadJet_x = float(tmp_line_arr[15]) * math.cos(float(tmp_line_arr[17]))
                                                LeadJet_y = float(tmp_line_arr[15]) * math.sin(float(tmp_line_arr[17]))

                                                SubLeadJet_x = float(tmp_line_arr[18]) * math.cos(float(tmp_line_arr[20]))
                                                SubLeadJet_y = float(tmp_line_arr[18]) * math.sin(float(tmp_line_arr[20]))

                                                MET_x = float(tmp_line_arr[21]) * math.cos(float(tmp_line_arr[22]))
                                                MET_y = float(tmp_line_arr[21]) * math.sin(float(tmp_line_arr[22]))



                                                # Sum_x = LeadLep_x + SubLeadLep_x + MET_x
                                                # Sum_y = LeadLep_y + SubLeadLep_y + MET_y
                                                # print "Sum_x**2+Sum_y**2 = {:f}".format(Sum_x**2+Sum_y**2)

                                                # if (Sum_x**2+Sum_y**2) < 10:

                                                f.write(line)

                                                fig = plt.figure(figsize=(10, 8))
                                                fig.suptitle('Event Display', fontsize=20)
                                                ax = fig.add_subplot(111)
                                                plt.xlim(-width_plt, width_plt)
                                                plt.ylim(-width_plt, width_plt)

                                                arrow_LeadLep = plt.arrow( 0.0, 0.0, LeadLep_x, LeadLep_y,head_width=5, head_length=2, color="saddlebrown") #, fc="k", ec="k"
                                                arrow_SubLeadLep = plt.arrow( 0.0, 0.0, SubLeadLep_x, SubLeadLep_y,head_width=5, head_length=2, color="black" )
                                                arrow_LeadJet = plt.arrow( 0.0, 0.0, LeadJet_x, LeadJet_y,head_width=5, head_length=2, color="blue" )
                                                arrow_SubLeadJet = plt.arrow( 0.0, 0.0, SubLeadJet_x, SubLeadJet_y,head_width=5, head_length=2, color="red" )
                                                arrow_MET = plt.arrow( 0.0, 0.0, MET_x, MET_y,head_width=5, head_length=2, color="darkorange" )


                                                plt.legend([arrow_LeadLep, arrow_SubLeadLep, arrow_LeadJet, arrow_SubLeadJet, arrow_MET], ['LeadLep        ('+tmp_line_arr[9]+'[GeV],'+tmp_line_arr[11]+'[rad])', 'SubLeadLep  ('+tmp_line_arr[12]+'[GeV],'+tmp_line_arr[14]+'[rad])', 'LeadJet        ('+tmp_line_arr[15]+'[GeV],'+tmp_line_arr[17]+'[rad])', 'SubLeadJet  ('+tmp_line_arr[18]+'[GeV],'+tmp_line_arr[20]+'[rad])', 'MET              ('+tmp_line_arr[21]+'[GeV],'+tmp_line_arr[22]+'[rad])'], fontsize=10, handler_map={mpatches.FancyArrow : HandlerPatch(patch_func=make_legend_arrow),
                                                      })
                                                list1.append(tmp_line_arr)
                                                fig.savefig('Selected/vbf/plots-vbf/run-'+tmp_line_arr[0]+'-event-'+tmp_line_arr[1]+'.pdf')
                                                plt.close()



# for i in range((num_lines-1))
# plt.show()



stop = timeit.default_timer()
print "Min = {:d}, Second = {:.2f}".format(int((stop - start)/60), stop - start)
