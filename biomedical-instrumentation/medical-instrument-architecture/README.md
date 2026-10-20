# Medical Instrument Architecture

Functional building blocks of a biomedical measurement chain, drawn to IEC 60601 isolation practice.

## Open the visualization

**[Launch the architecture diagram](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biomedical-instrumentation/medical-instrument-architecture/architecture.html)**

Or open [`architecture.html`](architecture.html) locally in a browser.

## What is in this folder

| File | What it is |
| --- | --- |
| [`architecture.html`](architecture.html) | Interactive signal-chain diagram, clickable stage notes, and cascaded transfer-function derivation |
| [`Medical_Instrument_Architecture.docx`](Medical_Instrument_Architecture.docx) | Original architecture write-up (Mermaid source + research note) |

## Topics in the visualization

1. **Signal chain** — measurand → sensor → conditioner → galvanic isolation → ADC → DSP → display.
2. **IEC 60601** — isolation barrier as a patient-safety requirement, not an optional analog block.
3. **System transfer function** — under matched, LTI stages, \(V_{display} \propto K_{sensor}\,G_{amp}\,H_{filter}(s)\,K_{ADC}\,M\).
4. **Nonlinearity note** — thermistors (and similar sensors) break the linear-gain assumption; the processor must invert Steinhart–Hart / LUT maps before display.

Cross-link: Circuits II (cascaded block diagrams and transfer functions).
