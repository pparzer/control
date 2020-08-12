// Plot data created with the PsychoPy control task
set scheme s1mono

// task ID
local id "pp3"

// import data from control task
import delimited data/`id'.csv, clear

// draw a vertical line at the time the mouse was reversed
summarize time if reverse == 1
if r(N) > 0 local xline = "xline(`=r(min)', lcolor(gs12))"

line mouse_y time, lcolor(black) ///
  || line noise_y time, lpattern(dash) lcolor(gs5) ///
  || line target_y time, lpattern(shortdash) lcolor(gs8) ///
  xtitle("time [s]") ytitle("vertical position") ///
  `xline' legend(off) ylab(-.5(.5).5)
 
graph export Figure_`id'.png, width(2000) replace
graph export Figure_`id'.eps, replace
