#!/usr/bin/Rscript
# plot data created with the PsychoPy control task

# set to the task ID
id = "x"

# open data file
d = read.csv(paste0("data/", id, ".csv"))

# plot vertical positions
plot(d$time, d$mouse_y, type = "l", xlab = "time [s]", ylab = "vertical position")
lines(d$time, d$noise_y, type = "l", lty = "dashed")
lines(d$time, d$target_y, type = "l", lty = "dotted")
