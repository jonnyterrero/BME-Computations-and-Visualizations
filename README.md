# BME Computations and Visualizations

Computational models, interactive visualizations, in-class work, and homework computations from my biomedical engineering coursework at FGCU. Every entry is dated, so this repo doubles as a running record of the work.

- **Live site:** [jonnyterrero.github.io/BME-Computations-and-Visualizations](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/)
- **Work log:** [`LOG.md`](LOG.md), a chronological index of every in-class entry and computation across courses

## Courses

| Course | Highlights | Open visualization |
| --- | --- | --- |
| [Biofluid Mechanics](biofluid-mechanics/) | Blood rheology, hydrostatics, capillary rise; arterial-stenosis CFD; sleep apnea and CPAP expiratory-relief simulation | [dashboard](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biofluid-mechanics/dashboard.html) · [stenosis CFD](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biofluid-mechanics/atherosclerosis-cfd.html) · [sleep apnea](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biofluid-mechanics/sleep-apnea-simulation.html) |
| [Biomedical Instrumentation](biomedical-instrumentation/) | IEC 60601 signal chain; electrode loading, linearity, CMRR, Johnson noise; biosignal filter bank | [architecture](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biomedical-instrumentation/medical-instrument-architecture/architecture.html) · [signal models](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biomedical-instrumentation/biomedical-signal-models/visualizations.html) · [filter bank](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biomedical-instrumentation/biomedical-signal-models/filter-bank.html) |
| [Circuits](circuits/) | DC/AC analysis, transients, phasors, frequency response, op-amps | |
| [Biomechanics](biomechanics/) | Sagittal-plane knee torque and patellar-tendon force | [knee simulator](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/biomechanics/simulator.html) |
| [Human Physiology for Engineers](human-physiology-for-engineers/) | Windkessel blood pressure, left-heart PV loops, glucose-insulin, cell populations, diffusion and membrane potential, enzyme kinetics, Hodgkin-Huxley | [visualized examples](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/human-physiology-for-engineers/visualized-examples/index.html) |
| [Bioperformance of Materials](bioperformance-of-materials/) | Graphene oxide fibroblast recovery synthesis and slide deck | [dashboard](https://jonnyterrero.github.io/BME-Computations-and-Visualizations/bioperformance-of-materials/dashboard.html) |

## Layout

```
<course>/
├── README.md              course overview and visualization links
├── in-class/              work done in lecture or lab
│   └── YYYY-MM-DD-<topic>/
│       ├── README.md      problem, approach, results, takeaways
│       ├── main.py        the computation (# %% cells)
│       └── figures/       saved plots
├── computations/          homework and computational assignments (same entry layout)
└── *.html                 interactive visualizations, served by GitHub Pages
```

`LOG.md` and the `in-class/README.md` / `computations/README.md` indexes are generated from the entry folders by `tools/worklog.py`. CI fails if they are out of date.

## Working in Cursor

One-time setup (requires [uv](https://docs.astral.sh/uv/)):

```bash
uv sync
```

This creates `.venv/` with NumPy, SciPy, SymPy, Matplotlib, pandas, Pint, python-control, and a Jupyter kernel. Cursor picks it up automatically via `.vscode/settings.json`.

Start a new entry:

```bash
uv run tools/worklog.py new circuits in-class "Thevenin equivalents" --tags thevenin,nodal
uv run tools/worklog.py new biofluid-mechanics computation "Poiseuille flow in a stenosis"
uv run tools/worklog.py new human-physiology-for-engineers in-class "Nernst potential" --date 2026-10-14
```

Then open the generated `main.py`:

- **Run cell by cell:** click *Run Cell* above any `# %%` marker or press Shift+Enter. Output and plots appear in the interactive window.
- **Run the whole file:** `uv run python <path>/main.py`, or F5 with the *Python: current file* launch config.
- **Notebooks:** `.ipynb` files also work; select the `.venv` kernel.

Fill in the entry `README.md` (the **Problem** paragraph becomes the summary in the course index), then refresh the log and commit:

```bash
uv run tools/worklog.py build
git add -A && git commit -m "circuits: Thevenin equivalents (in-class)"
```

Quick experiments that should not be published go in [`scratch/`](scratch/), which is git-ignored.

Courses are registered in [`tools/courses.toml`](tools/courses.toml). To add one, add an entry there and create the folder.

## Viewing the visualizations

GitHub's file browser shows HTML as source. Use the live site links above, or open any `.html` file locally in a browser. GitHub Pages deploys from `main` via `.github/workflows/pages.yml`.
