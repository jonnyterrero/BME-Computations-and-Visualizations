# Biomechanics

Sagittal-plane knee model for static equilibrium: external load torque versus the patellar-tendon force needed to hold the joint.

## Open the visualization

**[Launch the knee joint simulator](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biomechanics/simulator.html)**

Or open [`simulator.html`](simulator.html) locally in a browser.

## What is in this folder

| File | What it is |
| --- | --- |
| [`simulator.html`](simulator.html) | Interactive canvas: segment mass, external moment arm, and muscle insertion set the required quadriceps force |

## Topics in the simulator

1. **External torque** — \(\tau_{\mathrm{ext}} = mg\,r_{\mathrm{load}}\) about the knee (ΣTz = 0).
2. **Muscle force** — \(F_{\mathrm{muscle}} = \tau_{\mathrm{ext}} / r_{\mathrm{insertion}}\). A shorter patellar-tendon moment arm demands a much larger force.
3. **Free-body view** — red arrow is the external load, blue arrow is the muscle force (thickness scales with \(F_{\mathrm{muscle}}\)).

## How to use

Drag **System Mass**, **External Moment Arm**, and **Muscle Insertion**. Torque and force update immediately; the force arrows move with the moment arms.

## Coursework

| Folder | What it holds |
| --- | --- |
| [`in-class/`](in-class/) | Dated in-class examples and derivations |
| [`computations/`](computations/) | Homework and computational assignments |

The course-wide history is in the root [work log](../LOG.md).
