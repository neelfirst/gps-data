next steps:
1) create a dataset that condenses each gps measurement to the following:
	- lat/long (for plotting)
	- sats used/visible (proxy for signal strength)
	- pos/vel/time accuracy (performance metric)
	- average CN0 for used satellites (proxy for EMI)
2) create a comparative analysis between ref/dut with/out external antenna
	- lat/long trace
	- sats used/visible
	- average CN0
	- accuracy
3) determine most frequently used/visible space vehicle numbers and average CN0 per SV for each case

dataset design:
1/2) index - time - lat - long - sat vis - sat use - pos acc - vel acc - time acc - avg CN0
3) space vehicle - CN0
