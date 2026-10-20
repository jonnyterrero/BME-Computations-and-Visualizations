# Bioperformance of Materials

Interactive synthesis for the FGCU senior project **Surface-Dependent Fibroblast Recovery Following GO Exposure**.

## Open the visualization

**[Launch the Bioperformance dashboard](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/bioperformance-of-materials/dashboard.html)**

Or open [`dashboard.html`](dashboard.html) locally in a browser.

## What is in this folder

| File | What it is |
| --- | --- |
| [`dashboard.html`](dashboard.html) | Tabbed dashboard: experimental 2×2×2 factorial flow, governing attachment/morphology/degradation models, ISO 10993 biocompatibility, and FGCU lab feasibility with a hypothetical GO recovery chart |
| [`graphene-oxide-presentation/`](graphene-oxide-presentation/) | Related Graphene Oxide biocompatibility slide deck (Vite + React). Run locally with `npm install` then `npm run dev` from that folder |

## Topics in the dashboard

1. **Experimental flow** — substrate definition (TCP / collagen I / gelatin), serum and aging conditioning, sublethal GO challenge, recovery endpoints.
2. **Governing models** — attachment efficiency \(\eta_{attachment}\), aspect ratio and circularity, polyester hydrolysis \(M_w(t) = M_{w0}e^{-kt}\).
3. **Biocompatibility** — ISO 10993-5 / -6 and a fibroblast-collapse failure chain.
4. **FGCU feasibility** — lab resources vs protocol, plus a survival ≠ function chart.

## References

Wang et al. (2011), Davidenko et al. (2016), Ratner *Biomaterials Science*, ISO 10993.
