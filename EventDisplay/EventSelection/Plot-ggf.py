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
f = open('selected/ggf/Selected-ggf.txt', 'w')
initial_line = "run number   event number     mT   Mll   DPhill   nJets25   nJets3030   leadLepPt   leadLepEta   leadLepPhi   subleadLepPt   subleadLepEta   subleadLepPhi   leadJetPt   leadJetEta   leadJetPhi    MET   METPhi   isLeadE   isData\n"
initial_line1 = "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
initial_line = initial_line+initial_line1
f.write(initial_line)

num_lines = sum(1 for line in open('eventlist_v1/evtlist-CutGGF_SR_bVeto_0jet-data.txt'))

width_plt = 80
Value_Start_point = 2
list1 = []
count = 0
with open('eventlist_v1/evtlist-CutGGF_SR_bVeto_0jet-data.txt') as fp:
    for index, line in enumerate(fp):
        # if Value_Start_point <= index <= num_lines-1: #Value_Start_point = 2, num_lines-1 = max of line number
        if Value_Start_point <= index <= num_lines-1: #Value_Start_point = 2, num_lines-1 = max of line number
            tmp_line_arr = line.split()
            # #print tmp_line_arr
            if float(tmp_line_arr[2]) > 119. and  float(tmp_line_arr[2]) < 128.: #mT 110 - 130
                if float(tmp_line_arr[5]) < 1: #nJet25 < 1
                    if float(tmp_line_arr[7]) > 25 and float(tmp_line_arr[7]) < 45: #LeadLepPt  25 - 40
                        # if float(tmp_line_arr[10]) > 20 and float(tmp_line_arr[10]) < 25: #SubLeadLepPt  20 - 25
                        if float(tmp_line_arr[10]) < 30: #SubLeadLepPt  20 - 25
                            if float(tmp_line_arr[16]) > 40 and float(tmp_line_arr[16]) < 60: #MET
                                if float(tmp_line_arr[14]) == 0. and float(tmp_line_arr[15]) == 0.:
                                    if abs(float(tmp_line_arr[8])) < 0.5  and abs(float(tmp_line_arr[11])) < 0.5:
                                        if abs(float(tmp_line_arr[8])-float(tmp_line_arr[11])) < 1:
                                            if float(tmp_line_arr[3]) < 45 and float(tmp_line_arr[3]) > 30: #Mll < 55

                                                                    LeadLep_x = float(tmp_line_arr[7]) * math.cos(float(tmp_line_arr[9]))
                                                                    LeadLep_y = float(tmp_line_arr[7]) * math.sin(float(tmp_line_arr[9]))

                                                                    SubLeadLep_x = float(tmp_line_arr[10]) * math.cos(float(tmp_line_arr[12]))
                                                                    SubLeadLep_y = float(tmp_line_arr[10]) * math.sin(float(tmp_line_arr[12]))

                                                                    MET_x = float(tmp_line_arr[16]) * math.cos(float(tmp_line_arr[17]))
                                                                    MET_y = float(tmp_line_arr[16]) * math.sin(float(tmp_line_arr[17]))

                                                                    Sum_x = LeadLep_x + SubLeadLep_x + MET_x
                                                                    Sum_y = LeadLep_y + SubLeadLep_y + MET_y
                                                                    # print "Sum_x**2+Sum_y**2 = {:f}".format(Sum_x**2+Sum_y**2)

                                                                    # if (Sum_x**2+Sum_y**2) < 10:
                                                                    f.write(line)

                                                                    fig = plt.figure(figsize=(10, 8))
                                                                    fig.suptitle('Event Display', fontsize=20)
                                                                    ax = fig.add_subplot(111)
                                                                    plt.xlim(-width_plt, width_plt)
                                                                    plt.ylim(-width_plt, width_plt)
                                                                    # LeadJet_x = float(tmp_line_arr[8]) * math.cos(float(tmp_line_arr[9]))
                                                                    # LeadJet_y = float(tmp_line_arr[8]) * math.sin(float(tmp_line_arr[9]))
                                                                    #
                                                                    # SubLeadJet_x = float(tmp_line_arr[10]) * math.cos(float(tmp_line_arr[11]))
                                                                    # SubLeadJet_y = float(tmp_line_arr[10]) * math.sin(float(tmp_line_arr[11]))




                                                                    arrow_LeadLep = plt.arrow( 0.0, 0.0, LeadLep_x, LeadLep_y,head_width=5, head_length=2, color="saddlebrown") #, fc="k", ec="k"
                                                                    arrow_SubLeadLep = plt.arrow( 0.0, 0.0, SubLeadLep_x, SubLeadLep_y,head_width=5, head_length=2, color="black" )
                                                                    # arrow_LeadJet = plt.arrow( 0.0, 0.0, LeadJet_x, LeadJet_y,head_width=10, head_length=5, color="blue" )
                                                                    # arrow_SubLeadJet = plt.arrow( 0.0, 0.0, SubLeadJet_x, SubLeadJet_y,head_width=10, head_length=5, color="red" )
                                                                    arrow_MET = plt.arrow( 0.0, 0.0, MET_x, MET_y,head_width=5, head_length=2, color="darkorange" )


                                                                    plt.legend([arrow_LeadLep, arrow_SubLeadLep, arrow_MET], ['LeadLep        ('+tmp_line_arr[7]+'[GeV],'+tmp_line_arr[9]+'[rad])', 'SubLeadLep  ('+tmp_line_arr[10]+'[GeV],'+tmp_line_arr[12]+'[rad])', 'MET              ('+tmp_line_arr[16]+'[GeV],'+tmp_line_arr[17]+'[rad])'], fontsize=10, handler_map={mpatches.FancyArrow : HandlerPatch(patch_func=make_legend_arrow),
                                                                          })
                                                                    list1.append(tmp_line_arr)
                                                                    fig.savefig('selected/ggf/plots-ggf/run-'+tmp_line_arr[0]+'-event-'+tmp_line_arr[1]+'.pdf')
                                                                    plt.close()

                                                                    count = count + 1


print "Collect {:d} events".format(count)
# for i in range((num_lines-1))
# plt.show()



stop = timeit.default_timer()
print "Min = {:d}, Second = {:.2f}".format(int((stop - start)/60), stop - start)
