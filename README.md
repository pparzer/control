# control

A PsychoPy program for a control task. 

The subject is instructed to keep a red dot on the computer screen as close as
possible to the center of the screen marked by a white cross. The position of
the dot can be changed by moving the computer mouse, but a computer-generated
random process simulates an environmental disturbance invisible to the subject,
that is added to the mouse position. To keep the dot close to the cross, the
subject has to compensate the disturbance by moving the mouse. The control task
is thus a model of a two-dimensional control loop. 

There are two versions of the task. In the "easy" version the effect of the mouse
on the dot is as expected. Moving the mouse upwards moves the dot upwards,
moving the mouse to the right moves the dot to the right and vice versa.

In the "difficult" version, the effect of the mouse is inverted during the task.
That means, that after some time, the dot moves downward, when the mouse is
moved upwards and the dot moves to the right if the mouse is moved to the left.

The program has been tested with PsychoPy2 und PsychoPy3. PsychoPy can be
downloaded from https://www.psychopy.org/

There are also two scripts to plot the results of the task, plot.do for Stata
and plot.R for R.
