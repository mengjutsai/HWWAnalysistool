# Plotting tool

You can use the following python file in the Plotting tool to run the output root file with TQSampleFolder to make histogram and the ratio of two different processes. 


For flat plot, you could use the following command,

`
python Plotting_rev.py -f -i input/v4/20180702_R21_all_w_PRW_UpdateLumi_addActualMu_TopEnrichSpace_allweights_v4.root -o results/AddSF/R21_dataMC_compare_v1 -n --info mc16a 
`
* `-i` means the input file
* `-o` means the output folder
* `-n` means normalization
* `--info` means to have an additional text (string) on the plot 


For comparison plot, you could create two different processes on the plot and draw the ratio for these different processes.

`python Plotting_rev.py -c --i1 input/20180618_R21_mc16a_p3387_w_PRW_UpdateLumi_v2.root --i2 input/20180618_R21_mc16a_p3387_w_PRW_UpdateLumi_v2.root -o results/compare_v1 --p1 GGF --p2 VBF -n --sln GGF/VBF 
`

* `-i1` means the input file 1
* `-i2` means the input file 2
* `-o` means the output folder
* `--p1` means the process name of 1
* `--p2` means the process name of 2
* `-n` means normalization
* `--sln` means the sublegendname 



# Selection tool for event display

## EventSelection
Use Python to collaborate with eventlist and select the best signal-like data event for the event display. The input data format should like the `example.txt`.

For VBF and GGF, you could modify the python file for the input of the selection tool.

For VBF, 

`python Plot-vbf.py`

For ggF, 

`python Plot-ggf.py`
