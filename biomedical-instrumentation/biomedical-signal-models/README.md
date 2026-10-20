# Biomedical Signal Models

Four-panel instrumentation models from Webster and Northrop: source loading, transduction linearity, common-mode rejection, and thermal noise.

## Open the visualizations

**[Launch the signal-model dashboard](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biomedical-instrumentation/biomedical-signal-models/visualizations.html)** — loading, linearity, CMRR, noise.

**[Launch the biosignal filter bank](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biomedical-instrumentation/biomedical-signal-models/filter-bank.html)** — high-pass, low-pass, band-pass, and notch frequency responses over the physiological spectrum.

Or open [`visualizations.html`](visualizations.html) / [`filter-bank.html`](filter-bank.html) locally in a browser.

## What is in this folder

| File | What it is |
| --- | --- |
| [`visualizations.html`](visualizations.html) | Interactive browser version of the four-panel figure (sliders for \(Z_{in}\), CMRR, temperature, bandwidth) |
| [`filter-bank.html`](filter-bank.html) | Interactive frequency-response explorer for the four signal-conditioning filters (draggable cutoffs, dB/linear axis, 50/60 Hz line toggle) |
| [`biomedical_signal_models_visualizations.py`](biomedical_signal_models_visualizations.py) | Original matplotlib / NumPy source (same physics as the dashboard) |
| [`instrumentation_constraints.png`](instrumentation_constraints.png) | Static four-panel figure generated from the Python script |

Python dependencies are managed once for the whole repo in [`pyproject.toml`](../../pyproject.toml).

## Topics in the visualization

1. **Skin-electrode loading** — \(V_{measured} = V_{bio}\,Z_{in}/(Z_{in}+Z_{skin})\). Low \(Z_{in}\) attenuates the ECG.
2. **Sensor linearity** — thermistor \(R(T)=R_0\exp[\beta(1/T-1/T_0)]\) vs linear piezoresistive strain gauge.
3. **Instrumentation amplifier CMRR** — 60 Hz body-coupled interference leaking through finite \(A_{cm}=A_d/10^{\mathrm{CMRR}/20}\).
4. **Johnson noise** — \(V_{n,rms}=\sqrt{4k_B T R\,\Delta f}\), with a 10 MΩ microelectrode floor callout.

## Topics in the filter bank

Each filter's magnitude response \(|H(f)|\) is drawn on a shared log-frequency axis over the physiological spectrum (DC/drift, ECG/EEG, EMG, 50/60 Hz line, HF noise).

1. **High-pass** \(|H|=r/\sqrt{1+r^2},\ r=f/f_c\) — removes DC offset, baseline drift, and slow motion artifacts.
2. **Low-pass** \(|H|=1/\sqrt{1+(f/f_c)^2}\) — removes high-frequency noise and limits (anti-alias) bandwidth.
3. **Band-pass** — HPF × LPF cascade; isolates the useful band (e.g. 0.5–40 Hz ECG/EEG, ~20–500 Hz surface EMG).
4. **Notch** \(|H|=|f_0^2-f^2| / \sqrt{(f_0^2-f^2)^2+(f f_0/Q)^2}\) — a narrow null on 50/60 Hz mains interference; Q sets its width.

## Run the Python figure

```bash
uv sync   # from the repo root, once
uv run python biomedical-instrumentation/biomedical-signal-models/biomedical_signal_models_visualizations.py
```

Uncomment `plt.show()` at the bottom of the script, or add `plt.savefig("instrumentation_constraints.png")`.
