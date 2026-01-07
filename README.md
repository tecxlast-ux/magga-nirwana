# Private AI Secure Network

Repository template for a secure, AI-assisted network operations stack. Use
this structure to document topology, monitoring, AI telemetry handling, and
identity controls for private environments.

## Repository layout

- `docs/` – project documentation including scope, acceptance criteria, risks, and diagrams.
- `topology/` – source of truth for devices, links, and probe targets.
- `monitoring/` – Prometheus/Grafana stack for telemetry and alerting.
- `ai/` – normalizer schemas, API contract, prompt set, and runtime configs.
- `identity/` – account inventory, migration plan, and operational checklists.
- `configs/` – sanitized device configuration exports.
- `scripts/` – helper scripts for backups, generation, and validation.

## How to use

1. Populate `topology/topology.yaml` with devices and links.
2. Generate monitoring targets and launch `monitoring/docker-compose.yml`.
3. Feed telemetry into `ai/normalizer` according to the provided schemas.
4. Track progress via `docs/project-tracking.md` and ADRs under `docs/decisions/`.

## Conventions

- Do not store secrets in this repository.
- Keep sanitized exports only in `configs/`.
- Update `CHANGELOG.md` for every meaningful change.

## Public website

The documentation in `docs/` is published automatically as a static site via MkDocs and GitHub Pages.

### Enabling GitHub Pages

To enable automatic deployment to GitHub Pages:

1. Go to repository Settings > Pages
2. Under "Source", select "GitHub Actions"
3. Change `if: false` to `if: true` in `.github/workflows/pages.yml` (deploy job)
4. Push to main branch to trigger deployment

### Local preview

To preview the documentation site locally:

1. Install MkDocs: `pip install mkdocs`
2. Start a live server from the repo root: `mkdocs serve`
3. Open `http://127.0.0.1:8000` to browse the site.
