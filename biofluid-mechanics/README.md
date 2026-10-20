# Biofluid Mechanics

Research-grade interactive models for blood rheology, arterial hydrostatics, capillary rise, atherosclerotic-stenosis hemodynamics, and obstructive sleep apnea with CPAP expiratory relief.

## Open the visualization

**[Launch the Biofluid Mechanics dashboard](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biofluid-mechanics/dashboard.html)**

**[Launch the Arterial Stenosis Hemodynamics tool](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biofluid-mechanics/atherosclerosis-cfd.html)**

**[Launch the Sleep Apnea & CPAP Relief simulation](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biofluid-mechanics/sleep-apnea-simulation.html)**

Or open [`dashboard.html`](dashboard.html) locally in a browser.

## What is in this folder

| File | What it is |
| --- | --- |
| [`dashboard.html`](dashboard.html) | Three-tab computational dashboard with live Chart.js plots and sliders |
| [`atherosclerosis-cfd.html`](atherosclerosis-cfd.html) | Interactive reduced-order CFD of blood flow through a stenotic artery (straight **or** carotid-style bifurcation): velocity heat map, streamlines, pressure, and wall shear stress |
| [`sleep-apnea-simulation.html`](sleep-apnea-simulation.html) | Self-contained (no internet needed) physiology simulation for the Group 10 CPAP project: how obstructive sleep apnea happens, what a night of it does, and how a flow-triggered expiratory relief valve works |
| [`Sleep_Apnea_Presentation_with_Simulation.pptx`](Sleep_Apnea_Presentation_with_Simulation.pptx) | Group 10 deck (16 slides) with the simulation videos embedded |
| [`sleep-apnea-media/`](sleep-apnea-media/) | Ready-to-insert MP4 clips and 1920×1080 stills of the simulation for PowerPoint |

## Topics in the dashboard

1. **Rheology** — Newtonian plasma \(\tau = \mu\dot{\gamma}\) vs shear-thinning whole blood \(\tau = K\dot{\gamma}^n\), including the Fåhræus–Lindqvist effect in microvessels.
2. **Hydrostatics** — standing arterial pressure \(P_{total} = P_{heart} + \rho g h\). Drag density and gravity to see MAP at the feet change.
3. **Capillary action** — Jurin's law \(h = 2\sigma\cos\theta / (\rho g R)\). Radius, surface tension, and contact angle drive the animated meniscus (alveolar / organ-on-chip scale).

## Arterial stenosis hemodynamics (`atherosclerosis-cfd.html`)

A quasi-1-D reduction of the incompressible Navier–Stokes equations models blood flow through an atherosclerotic plaque, in either a **straight artery** or a **carotid-style bifurcation** (flow divides between two daughter branches by resistance, with a flow divider and sinus/bulb). Adjustable in real time: geometry mode, stenosis severity (% area reduction), plaque asymmetry (concentric → eccentric, or bilateral → unilateral in bifurcation mode), inlet velocity, dynamic viscosity, artery diameter, plaque length, blood density, and steady vs. pulsatile flow.

- **Continuity** \(U(x) = U_0 (D/H(x))^2\) drives the stenotic jet.
- **Reynolds number** \(Re = \rho V D / \mu\) updates live and flags laminar / transitional / turbulent regimes.
- **Poiseuille wall shear** \(\tau_w = 8\mu U / H\) and viscous loss \(dp/dx = 32\mu U/H^2\); **Bernoulli + Borda–Carnot** estimate the pressure drop.
- **Bifurcation mode** adds daughter-branch flow division by viscous conductance, an apex flow divider (high shear), and a carotid sinus with low / reversed outer-wall shear — the preferential site of plaque.
- Velocity heat map, particle streamlines, velocity vectors, a pressure band, and wall-shear coloring, plus axial plots of velocity, pressure, and wall shear stress. The tool labels which quantities are directly calculated, estimated, or qualitative, and is a teaching model — not a validated clinical CFD simulation.

## Sleep apnea & CPAP expiratory relief (`sleep-apnea-simulation.html`)

Built for **Group 10 · BME 3261C · Respiratory Flow Device Design Challenge** ("Rethinking CPAP"). One physiology model drives three scenes, and the third reproduces the group's deck numbers exactly.

| Scene | What it shows | Model |
| --- | --- | --- |
| **1 · How it happens** | Side view of the airway with live airflow. Sleep relaxes the airway, pressure at the collapse site falls below the closing pressure Pcrit, the walls stick together, effort climbs, SpO₂ falls, the brain arouses, the airway reopens, and the cycle repeats. CPAP toggles on as a pneumatic splint. | Starling-resistor airway + single-compartment RC lung + CO₂/O₂ mass balance + delayed chemoreflex + effort-triggered arousal. Four traits (Pcrit, dilator response, arousal threshold, loop gain) after Eckert 2013 |
| **2 · What it does** | The same patient over 8 h, untreated vs CPAP: fragmented hypnogram, event track, SpO₂, AHI / ODI / time < 90% / arousals / N3 / REM, and what one event does to SpO₂, heart rate and BP | AASM-style scoring (apnea ≥ 90% reduction ≥ 10 s; hypopnea ≥ 30% with ≥ 3% dip or arousal). HR/BP are illustrative |
| **3 · Our solution** | Airflow path (blower → tube → EPR valve → mask → nares → vent), one-breath flow / mask-pressure / effort traces, work-of-breathing loop, before → after metrics, and a comfort-vs-airway-margin sweep | The deck's RC model: `P_mus + P_dev = R·V̇ + V/C`, flow-proportional relief, orifice vent jet (Cd 0.6, D 1 mm). Matches slides 8–10 to the digit: 8.48 → 5.48 cmH₂O, 0.41 → 0.29 J, PTP −24%, jet 24.3 → 20.3 m/s, Re 1617 → 1353, v² −30% |

Press **▶ Guided tour** (or `T`) for a ~2.5 minute self-running walkthrough. **ⓘ Model notes** (`I`) lists equations, parameters, verified references and honest limits, including that the deck's "effort" percentages depend on its constant-offset convention and that an adherence benefit from expiratory relief is not established in the literature.

Simulated presets (8 h, untreated → CPAP 10 cmH₂O, averaged over four random seeds): healthy AHI 0 → 0, mild ≈ 8 → 0, moderate ≈ 19 → 0, severe ≈ 49 → 0. Nothing is scripted: events, desaturations and hypnograms come out of the model.

### Put it in a PowerPoint

1. **Video (works offline, most reliable).** Insert → Video → This Device and pick a clip from [`sleep-apnea-media/`](sleep-apnea-media/): `walkthrough.mp4` (captioned tour), or the clean per-scene clips `scene1-airway.mp4`, `scene2-night.mp4`, `scene3-relief-valve.mp4`. In Playback set Start to *Automatically* (and *Loop until stopped* for scene 1).
2. **Live and interactive.** After this branch is merged to `main` and GitHub Pages is on, the page is at `https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biofluid-mechanics/sleep-apnea-simulation.html`. Insert a still from `sleep-apnea-media/` and give it a hyperlink to that URL (Insert → Link) to open the live page during the talk, or use a web-page add-in such as *Web Viewer* or *LiveWeb* (availability depends on your PowerPoint version and platform; needs internet).
3. **Offline and interactive.** The page is one self-contained HTML file with no external requests. Copy it next to the deck and hyperlink a slide object to it (Insert → Link → Existing File); it opens in the default browser.

URL parameters for slide-sized embeds: `?scene=1|2|3` · `&embed=1` (trims header buttons) · `&autoplay=1` (starts the tour) · `&patient=healthy|mild|moderate|severe` · `&cpap=1` · `&stage=REM`. Example: `sleep-apnea-simulation.html?scene=3&embed=1`. The stage is a fixed 16:9 canvas that scales to any frame; use at least ~800 px wide for readable text. The page needs a modern browser engine (Chromium, WebKit or Firefox); if an add-in shows a blank frame, use the video instead. Keys: `1 2 3` scenes, `Space` pause, `F` full screen.

This is a teaching model, not a validated clinical simulator.

## How to use

Switch tabs in the header. Hydrostatics and capillary panels update as soon as you move a slider. No install required.

## Coursework

| Folder | What it holds |
| --- | --- |
| [`in-class/`](in-class/) | Dated in-class examples and derivations |
| [`computations/`](computations/) | Homework and computational assignments |

The course-wide history is in the root [work log](../LOG.md).
