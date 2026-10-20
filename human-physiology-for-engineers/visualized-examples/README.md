# Visualized Examples

> **Edit in [BME-Computations-and-Visualizations](https://github.com/jonnyterrero/BME-Computations-and-Visualizations/tree/main/human-physiology-for-engineers/visualized-examples).** That copy is canonical; the `visualized examples/` folder in [Human-Physiology-for-Engineers](https://github.com/jonnyterrero/Human-Physiology-for-Engineers) is overwritten from it on every push to `main`.

Interactive visualizations for every Human Physiology for Engineers homework/project assignment. The original MATLAB/Simulink source files referenced below live in [jonnyterrero/Human-Physiology-for-Engineers](https://github.com/jonnyterrero/Human-Physiology-for-Engineers). Each page re-implements the course's MATLAB/Simulink model in plain JavaScript using the **same equations, parameters, and numerical schemes** as the original files, with sliders, scenario presets, and hoverable Plotly charts.

## How to use

**[Launch the examples index](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/human-physiology-for-engineers/visualized-examples/index.html)**, or open **`index.html`** (or any individual page) in a browser — no MATLAB, install, or server needed. An internet connection is required the first time so the Plotly.js charting library can load from its CDN.

## Contents

| Page | Assignment | Source model files |
|---|---|---|
| `pfe1-hw1-blood-pressure.html` | PFE I — Homework 1: Blood Pressure Model | `sa.m`, `in_sa.m`, `Psa_new.m`, `QAo_now.m` |
| `pfe1-hw2-left-heart.html` | PFE I — Homework 2: Left Heart & Aorta | `Cardio_SA_LV.slx`, `Command_Cardio_SA_LV.m` |
| `pfe1-hw3-glucose-insulin.html` | PFE I — Homework 3: Glucose/Insulin (OGTT, diabetes, metformin) | `GLUINSMODEL.slx` + run scripts |
| `hpe-hw1-cell-population.html` | Homework 1: Cell Population (logistic, predator-prey, 3-species) | Simulink models in `Physiology Hw attempts/` |
| `hpe-hw2-diffusion-membrane.html` | Homework 2: Diffusion, Mass Action & Membrane Potential | assignment doc |
| `hpe-hw3-enzyme-kinetics.html` | Homework 3: Enzyme Kinetics (MM, Lineweaver-Burk, Hill) | assignment doc |
| `hpe-hw4-hodgkin-huxley.html` | Homework 4: Action Potentials (Hodgkin-Huxley) | `HH.m`, `in_HH.m`, `alpha*/beta*.m`, `snew.m`, `izero.m` |

## Fidelity notes

- **HW1 (blood pressure)** uses the exact semi-implicit Euler update from `Psa_new.m` and the triangular systolic flow pulse from `QAo_now.m` (100 steps/cycle, 16 cycles), including the heart-block modification (QAo = 0 for 0.03–0.13 min).
- **HW2 (left heart)** implements the Hoppensteadt–Peskin time-varying ventricular compliance C_LV(t) with the course constants (tauS = 0.0025, tauD = 0.005 min), diode valves, and the `AoBkflo` aortic-regurgitation term.
- **HW3 (glucose-insulin)** uses the standard parameterization of Khoo's minimal model, which reproduces the course's fasting steady state (0.81 mg/ml glucose, 0.057 IU/ml insulin at QL = 8400 mg/hr) and the Type 1 (κ, insulin production) / Type 2 (η, insulin sensitivity) severity gains. Drug models are the one-compartment Bateman PK models specified in the assignment.
- **HW4 (Hodgkin-Huxley)** is a line-by-line transcription of Dr. Peskin's scripts: same rate functions, same semi-implicit gate/voltage updates, dt = 0.01 ms. The resting potential is recomputed from E_K via the chord-conductance weights (0.0945/0.9055) exactly as Part 2 of the assignment derives.
