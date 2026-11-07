import json

with open("days_dataset.json", "r", encoding="utf-8") as f:
    days_data = json.load(f)

days_json = json.dumps(days_data)

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The ₹20 LPA Remote SDET Master Roadmap & 90-Day Execution Engine — Red-Team Validated</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #07090e;
      --surface: #0e131f;
      --surface-elevated: #141c2e;
      --surface-hover: #1a253c;
      --border: #202b40;
      --border-subtle: #172033;
      --border-focus: #00f5a0;
      --text: #f0f4f8;
      --text-muted: #8fa0b5;
      --text-dim: #54667d;
      
      --pass: #00f5a0;
      --pass-dim: rgba(0, 245, 160, 0.12);
      --pass-glow: rgba(0, 245, 160, 0.35);
      --run: #f59e0b;
      --run-dim: rgba(245, 158, 11, 0.15);
      --fail: #fb7185;
      --fail-dim: rgba(251, 113, 133, 0.12);
      --cyan: #38bdf8;
      --cyan-dim: rgba(56, 189, 248, 0.12);
      --indigo: #818cf8;
      --purple: #c084fc;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg);
      background-image: radial-gradient(circle at 50% 0%, rgba(30, 41, 59, 0.35) 0%, transparent 60%);
      color: var(--text);
      font-family: 'Inter', -apple-system, sans-serif;
      line-height: 1.5;
      padding-bottom: 120px;
      -webkit-font-smoothing: antialiased;
    }

    h1, h2, h3, h4, .font-heading {
      font-family: 'Space Grotesk', sans-serif;
      letter-spacing: -0.02em;
    }

    code, pre, .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }

    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb { background: #202b40; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #334460; }

    .wrap {
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Fixed Command Bar */
    header {
      background: rgba(14, 19, 31, 0.94);
      border-bottom: 1px solid var(--border);
      backdrop-filter: blur(12px);
      position: sticky;
      top: 0;
      z-index: 50;
      padding: 12px 0;
    }

    .nav-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }

    .brand-cluster {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .beacon {
      width: 10px;
      height: 10px;
      background: var(--pass);
      border-radius: 50%;
      box-shadow: 0 0 12px var(--pass-glow);
      animation: pulse 2.2s infinite ease-in-out;
    }

    @keyframes pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.35; transform: scale(0.85); }
    }

    .brand-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
    }

    .brand-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      background: var(--surface-elevated);
      border: 1px solid var(--border);
      padding: 2px 8px;
      border-radius: 4px;
      color: var(--pass);
      font-weight: 600;
    }

    .nav-tools {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    button.tool-btn {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.82rem;
      font-weight: 600;
      padding: 7px 13px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: var(--surface-elevated);
      color: var(--text);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }
    button.tool-btn:hover {
      background: var(--surface-hover);
      border-color: #354766;
      color: #fff;
      transform: translateY(-1px);
    }
    button.tool-btn.primary {
      background: var(--pass-dim);
      border-color: rgba(0, 245, 160, 0.4);
      color: var(--pass);
    }
    button.tool-btn.primary:hover {
      background: rgba(0, 245, 160, 0.22);
    }

    /* Hero Cockpit Deck */
    .cockpit {
      margin: 24px 0 20px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 24px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.45);
    }

    .cockpit-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 20px;
    }

    .deck-subhead {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      color: var(--cyan);
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .deck-title {
      font-size: 1.6rem;
      font-weight: 700;
      color: #fff;
    }

    .deck-desc {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 4px;
    }

    .gauge-block {
      text-align: right;
    }

    .gauge-num {
      font-family: 'JetBrains Mono', monospace;
      font-size: 2.4rem;
      font-weight: 700;
      color: var(--pass);
      line-height: 1;
      text-shadow: 0 0 16px var(--pass-glow);
    }

    .gauge-label {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      color: var(--text-dim);
      margin-top: 4px;
    }

    /* Calibrated Phosphor Track */
    .gauge-track {
      height: 6px;
      background: var(--surface-elevated);
      border-radius: 9999px;
      overflow: hidden;
      margin-bottom: 24px;
      position: relative;
    }

    .gauge-fill {
      height: 100%;
      background: linear-gradient(90deg, #00f5a0, #38bdf8);
      border-radius: 9999px;
      transition: width 0.5s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 0 12px var(--pass-glow);
    }

    /* Interactive 84-Day Pipeline Matrix */
    .matrix-section {
      margin-bottom: 22px;
      background: var(--bg);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 16px;
    }

    .matrix-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 8px;
    }

    .matrix-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.85rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .matrix-legend {
      display: flex;
      align-items: center;
      gap: 12px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      color: var(--text-dim);
    }

    .legend-item { display: flex; align-items: center; gap: 5px; }
    .dot-sample { width: 8px; height: 8px; border-radius: 2px; }
    .dot-sample.todo { background: #1c2638; border: 1px solid #2a384f; }
    .dot-sample.run { background: var(--run); }
    .dot-sample.done { background: var(--pass); box-shadow: 0 0 6px var(--pass-glow); }

    .matrix-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(28px, 1fr));
      gap: 6px;
    }

    .matrix-cell {
      height: 28px;
      background: #121927;
      border: 1px solid #1f2d42;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.68rem;
      font-weight: 600;
      color: var(--text-dim);
      cursor: pointer;
      transition: all 0.15s ease;
      user-select: none;
    }
    .matrix-cell:hover {
      border-color: var(--cyan);
      color: #fff;
      transform: scale(1.1);
      z-index: 10;
    }
    .matrix-cell.in-progress {
      background: var(--run-dim);
      border-color: var(--run);
      color: var(--run);
      font-weight: 700;
    }
    .matrix-cell.completed {
      background: var(--pass-dim);
      border-color: var(--pass);
      color: var(--pass);
      font-weight: 700;
      box-shadow: 0 0 8px rgba(0, 245, 160, 0.2);
    }

    /* Telemetry Telemetry Stat Row */
    .cockpit-stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
      gap: 12px;
    }

    .stat-tile {
      background: var(--bg);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 12px 14px;
    }

    .stat-kicker {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .stat-number {
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.35rem;
      font-weight: 700;
      color: #fff;
      margin-top: 2px;
    }

    .stat-micro {
      font-size: 0.72rem;
      color: var(--text-dim);
      margin-top: 2px;
    }

    /* Next Up Focus Banner */
    .next-up-strip {
      margin-bottom: 24px;
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.08) 0%, rgba(0, 245, 160, 0.08) 100%), var(--surface);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 10px;
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }

    .next-label {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      font-weight: 700;
      color: var(--cyan);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }

    .next-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      margin-top: 2px;
    }

    .next-info {
      font-size: 0.8rem;
      color: var(--text-muted);
    }

    /* Phase Selector Tabs */
    .phase-shelf {
      margin-bottom: 20px;
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
    }

    .phase-tab {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.82rem;
      font-weight: 600;
      padding: 8px 16px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
    }
    .phase-tab:hover {
      border-color: #384d6b;
      color: #fff;
    }
    .phase-tab.active {
      background: var(--surface-elevated);
      border-color: var(--pass);
      color: var(--pass);
      font-weight: 700;
    }

    /* Search & Control Filter Strip */
    .filter-deck {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 16px;
      margin-bottom: 20px;
      display: flex;
      gap: 12px;
      align-items: center;
      flex-wrap: wrap;
    }

    .search-input-wrap {
      flex: 1;
      min-width: 260px;
      position: relative;
    }

    .search-ctrl {
      width: 100%;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 8px 12px 8px 34px;
      color: #fff;
      font-family: 'Inter', sans-serif;
      font-size: 0.83rem;
      transition: border-color 0.15s ease;
    }
    .search-ctrl:focus {
      outline: none;
      border-color: var(--pass);
    }

    .search-sym {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
    }

    .filter-options {
      display: flex;
      gap: 6px;
      align-items: center;
      flex-wrap: wrap;
    }

    .pill-filter {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      padding: 5px 11px;
      border-radius: 4px;
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--text-muted);
      cursor: pointer;
    }
    .pill-filter:hover { color: #fff; border-color: #384d6b; }
    .pill-filter.active {
      background: var(--surface-elevated);
      border-color: #4a6182;
      color: #fff;
      font-weight: 700;
    }

    /* Sprint Ledger List */
    .sprint-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .sprint-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 18px 20px;
      transition: all 0.15s ease;
    }
    .sprint-card:hover {
      border-color: #354766;
    }
    .sprint-card.completed {
      border-color: rgba(0, 245, 160, 0.35);
      background: rgba(14, 19, 31, 0.75);
    }
    .sprint-card.in-progress {
      border-color: rgba(245, 158, 11, 0.4);
    }

    .sprint-main {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }

    .sprint-left {
      display: flex;
      align-items: flex-start;
      gap: 14px;
      flex: 1;
    }

    .sprint-idx {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--cyan);
      min-width: 42px;
      padding-top: 2px;
    }

    .sprint-check {
      width: 22px;
      height: 22px;
      accent-color: var(--pass);
      cursor: pointer;
      margin-top: 2px;
    }

    .sprint-body { flex: 1; }

    .sprint-tags {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 6px;
      flex-wrap: wrap;
    }

    .tag-token {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      color: var(--text-dim);
    }
    .tag-category {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      font-weight: 600;
      color: var(--cyan);
    }
    .tag-time {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.68rem;
      color: var(--text-dim);
      background: var(--bg);
      padding: 1px 6px;
      border-radius: 3px;
    }

    .sprint-name {
      font-size: 1.05rem;
      font-weight: 600;
      color: #fff;
      margin-bottom: 8px;
    }
    .sprint-card.completed .sprint-name {
      color: var(--text-dim);
      text-decoration: line-through;
    }

    .concept-capsules {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin-bottom: 10px;
    }

    .capsule {
      font-size: 0.75rem;
      color: var(--text-muted);
      background: var(--bg);
      border: 1px solid var(--border-subtle);
      padding: 2px 8px;
      border-radius: 4px;
    }

    .sprint-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .inspect-btn {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.77rem;
      font-weight: 600;
      color: var(--pass);
      background: transparent;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 0;
    }
    .inspect-btn:hover { text-decoration: underline; }

    .copy-path-btn {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      color: var(--text-dim);
      background: var(--bg);
      border: 1px solid var(--border-subtle);
      padding: 2px 7px;
      border-radius: 4px;
      cursor: pointer;
    }
    .copy-path-btn:hover { color: #fff; border-color: #384d6b; }

    .sprint-right {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .state-dropdown {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 5px 9px;
      border-radius: 4px;
      cursor: pointer;
    }

    /* Expandable Inspection Console */
    .inspection-drawer {
      margin-top: 14px;
      padding-top: 14px;
      border-top: 1px solid var(--border-subtle);
      display: none;
      flex-direction: column;
      gap: 12px;
    }
    .inspection-drawer.open { display: flex; }

    .panel-block {
      background: var(--bg);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 14px;
    }

    .panel-title {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--pass);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .panel-title.interview { color: var(--fail); }
    .panel-title.notes { color: var(--cyan); }

    .panel-body {
      font-size: 0.84rem;
      color: var(--text);
      line-height: 1.55;
    }

    .deliverable-banner {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 8px;
      flex-wrap: wrap;
    }

    .code-chip {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      background: #111825;
      border: 1px solid var(--border);
      color: var(--pass);
      padding: 3px 9px;
      border-radius: 4px;
    }

    .q-stem { font-weight: 600; color: #fff; }

    .reveal-trigger {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      color: var(--fail);
      background: transparent;
      border: 1px solid rgba(251, 113, 133, 0.4);
      border-radius: 4px;
      padding: 3px 9px;
      cursor: pointer;
      margin-top: 8px;
      display: inline-block;
    }
    .reveal-trigger:hover { background: rgba(251, 113, 133, 0.12); }

    .answer-vault {
      margin-top: 8px;
      padding: 10px 14px;
      background: rgba(251, 113, 133, 0.07);
      border-left: 2px solid var(--fail);
      font-size: 0.82rem;
      color: #ffd4db;
      display: none;
    }
    .answer-vault.visible { display: block; }

    /* 3-Pillar Daily Activity Layout */
    .activity-pillars {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
      margin: 12px 0 14px;
    }

    .pillar-col {
      background: #090d15;
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      transition: all 0.2s ease;
    }
    .pillar-col:hover {
      border-color: #2b3952;
    }

    .pillar-col.pillar-theory {
      border-top: 2px solid var(--indigo);
      background: linear-gradient(180deg, rgba(129, 140, 248, 0.04) 0%, rgba(9, 13, 21, 0.85) 100%);
    }
    .pillar-col.pillar-coding {
      border-top: 2px solid var(--pass);
      background: linear-gradient(180deg, rgba(0, 245, 160, 0.04) 0%, rgba(9, 13, 21, 0.85) 100%);
    }
    .pillar-col.pillar-katas {
      border-top: 2px solid var(--run);
      background: linear-gradient(180deg, rgba(245, 158, 11, 0.04) 0%, rgba(9, 13, 21, 0.85) 100%);
    }

    .pillar-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
      padding-bottom: 6px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }

    .pillar-tag {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.76rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 6px;
      letter-spacing: -0.01em;
    }
    .pillar-tag.theory { color: #a5b4fc; }
    .pillar-tag.coding { color: var(--pass); }
    .pillar-tag.katas { color: #fbbf24; }

    .pillar-time {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.68rem;
      color: var(--text-dim);
      background: rgba(255, 255, 255, 0.04);
      padding: 1px 6px;
      border-radius: 3px;
    }

    .pillar-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin: 0;
      padding: 0;
      flex: 1;
    }

    .pillar-item {
      font-size: 0.77rem;
      color: var(--text);
      line-height: 1.4;
      display: flex;
      align-items: flex-start;
      gap: 6px;
    }

    .pillar-marker {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
      line-height: 1.3;
    }
    .pillar-marker.theory { color: #818cf8; }
    .pillar-marker.coding { color: var(--pass); }
    .pillar-marker.katas { color: #f59e0b; }

    .kata-preview-chip {
      margin-top: 10px;
      padding: 6px 9px;
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.22);
      border-radius: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
      font-size: 0.72rem;
    }
    .kata-chip-label {
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-dim);
      font-size: 0.65rem;
      text-transform: uppercase;
    }
    .kata-chip-name {
      color: #fff;
      font-weight: 600;
    }
    .kata-chip-diff {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.65rem;
      font-weight: 700;
      padding: 1px 6px;
      border-radius: 3px;
    }
    .kata-chip-diff.easy { background: rgba(0, 245, 160, 0.15); color: var(--pass); }
    .kata-chip-diff.medium { background: rgba(245, 158, 11, 0.15); color: #fbbf24; }
    .kata-chip-diff.hard { background: rgba(251, 113, 133, 0.15); color: var(--fail); }

    /* Track Focus Modes */
    .sprint-list[data-track-focus="theory"] .pillar-coding,
    .sprint-list[data-track-focus="theory"] .pillar-katas {
      opacity: 0.25;
    }
    .sprint-list[data-track-focus="coding"] .pillar-theory,
    .sprint-list[data-track-focus="coding"] .pillar-katas {
      opacity: 0.25;
    }
    .sprint-list[data-track-focus="katas"] .pillar-theory,
    .sprint-list[data-track-focus="katas"] .pillar-coding {
      opacity: 0.25;
    }

    /* Inspection Drawer Enhanced Panels */
    .panel-title.theory-title { color: #a5b4fc; }
    .panel-title.katas-title { color: #fbbf24; }

    .theory-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 8px;
    }
    .theory-card {
      background: rgba(129, 140, 248, 0.05);
      border: 1px solid rgba(129, 140, 248, 0.15);
      border-radius: 6px;
      padding: 9px 12px;
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }
    .theory-check {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
      color: #818cf8;
    }
    .theory-text {
      font-size: 0.8rem;
      color: #e0e7ff;
      line-height: 1.4;
    }

    .coding-checklist {
      margin: 10px 0 8px;
      padding: 10px 12px;
      background: rgba(0, 245, 160, 0.03);
      border: 1px solid rgba(0, 245, 160, 0.15);
      border-radius: 6px;
    }
    .coding-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 6px;
    }
    .code-topic-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      color: var(--pass);
      background: rgba(0, 245, 160, 0.1);
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid rgba(0, 245, 160, 0.2);
    }

    .kata-challenge-box {
      background: rgba(245, 158, 11, 0.04);
      border: 1px solid rgba(245, 158, 11, 0.2);
      border-radius: 6px;
      padding: 12px 14px;
    }
    .kata-challenge-head {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 8px;
    }
    .kata-title-highlight {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.95rem;
      font-weight: 700;
      color: #fff;
    }
    .kata-pattern-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      color: #cbd5e1;
      background: #141c2e;
      padding: 2px 8px;
      border-radius: 4px;
      border: 1px solid var(--border);
    }
    .kata-desc {
      font-size: 0.82rem;
      color: #e2e8f0;
      line-height: 1.5;
      margin-bottom: 10px;
    }
    .kata-practice-topics {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
      margin-bottom: 10px;
    }
    .kata-subhead {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.68rem;
      color: var(--text-dim);
      text-transform: uppercase;
    }
    .kata-topic-pill {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.3);
      color: #fbbf24;
      padding: 2px 8px;
      border-radius: 3px;
    }
    .kata-hint-btn {
      color: #f59e0b;
      border-color: rgba(245, 158, 11, 0.4);
    }
    .kata-hint-btn:hover {
      background: rgba(245, 158, 11, 0.12);
    }
    .kata-vault {
      background: rgba(245, 158, 11, 0.08);
      border-left-color: #f59e0b;
      color: #fed7aa;
    }

    .track-switcher {
      margin-left: auto;
    }
    @media (max-width: 900px) {
      .track-switcher { margin-left: 0; width: 100%; }
      .activity-pillars { grid-template-columns: 1fr; }
    }

    .input-row {
      width: 100%;
      background: #090c12;
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 8px 10px;
      color: #fff;
      font-size: 0.8rem;
      font-family: inherit;
    }
    .input-row:focus { outline: none; border-color: var(--pass); }
    .input-row.mono { font-family: 'JetBrains Mono', monospace; color: var(--cyan); font-size: 0.76rem; }

    .persisted-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.68rem;
      color: var(--pass);
      margin-top: 4px;
      opacity: 0;
      transition: opacity 0.2s;
    }
    .persisted-badge.shown { opacity: 1; }

    /* Modal */
    .modal-veil {
      position: fixed;
      inset: 0;
      background: rgba(7, 9, 14, 0.88);
      backdrop-filter: blur(10px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }
    .modal-veil.open { display: flex; }

    .modal-window {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      max-width: 860px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 24px;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6);
    }

    .modal-header-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 12px;
      margin-bottom: 18px;
    }

    .close-btn {
      background: transparent;
      border: none;
      color: var(--text-dim);
      font-size: 1.25rem;
      cursor: pointer;
    }
    .close-btn:hover { color: #fff; }

    .code-frame {
      background: var(--bg);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 14px;
      overflow-x: auto;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.78rem;
      color: #d1d9e2;
      line-height: 1.5;
      margin: 8px 0 16px;
    }

    /* Floating Cockpit Focus Stopwatch */
    .cockpit-timer {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--surface);
      border: 1px solid rgba(0, 245, 160, 0.35);
      border-radius: 10px;
      padding: 10px 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      z-index: 40;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.65);
    }

    .timer-readout {
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--pass);
    }

    .timer-action {
      background: var(--surface-elevated);
      border: 1px solid var(--border);
      color: #fff;
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.75rem;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: 4px;
      cursor: pointer;
    }
    .timer-action:hover { background: #28374d; }

    @media (max-width: 768px) {
      .nav-bar { flex-direction: column; align-items: stretch; }
      .gauge-block { text-align: left; }
      .cockpit { padding: 18px; }
      .cockpit-timer { bottom: 12px; right: 12px; left: 12px; justify-content: space-between; }
    }
  </style>
</head>
<body>

  <!-- Top Navigation & Command Controls -->
  <header>
    <div class="wrap nav-bar">
      <div class="brand-cluster">
        <div class="beacon"></div>
        <div>
          <span class="brand-title">The ₹20 LPA Remote SDET Master Roadmap</span>
          <span class="brand-tag">Red-Team Validated // 90-Day Execution Engine</span>
        </div>
      </div>

      <div class="nav-tools">
        <button class="tool-btn" onclick="openExposeModal()" style="border-color: rgba(251, 113, 133, 0.4); color: var(--fail);">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
          Red-Team Audit & Expose
        </button>
        <button class="tool-btn" onclick="openGatesModal()" style="border-color: rgba(245, 158, 11, 0.4); color: var(--run);">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg>
          3 Competency Gates
        </button>
        <button class="tool-btn" onclick="openReposModal()" style="border-color: rgba(56, 189, 248, 0.4); color: var(--cyan);">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
          2 Core Repos + AI Spec
        </button>
        <button class="tool-btn" onclick="openDrillsModal()" style="border-color: rgba(192, 132, 252, 0.4); color: var(--purple);">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          Machine Coding Drills
        </button>
        <button class="tool-btn" onclick="openVault()">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
          Code Vault
        </button>
        <button class="tool-btn" onclick="exportData()">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          Export
        </button>
        <button class="tool-btn" onclick="triggerRestore()">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
          Restore
        </button>
        <input type="file" id="restoreInput" style="display:none;" onchange="handleRestore(event)">
      </div>
    </div>
  </header>

  <div class="wrap">

    <!-- Cockpit Telemetry Hub -->
    <div class="cockpit">
      <div class="cockpit-header">
        <div>
          <div class="deck-subhead">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
            Red-Team Validated 90-Day Execution Engine // 4.5 - 5.0h Daily Protocol
          </div>
          <h2 class="deck-title">The ₹20 LPA Remote SDET Master Roadmap & 90-Day Execution Engine</h2>
          <p class="deck-desc">Re-engineered from Red-Team Audit. Focuses on production engineering depth, parallel-safe fixtures, flake post-mortems, mutation testing, and early job-market execution for ₹15–20 LPA+ fixed opportunities.</p>
        </div>
        <div class="gauge-block">
          <div class="gauge-num" id="gaugePct">0%</div>
          <div class="gauge-label" id="gaugeRatio">0 of 90 Sprints Verified</div>
        </div>
      </div>

      <!-- Linear Gauge -->
      <div class="gauge-track">
        <div class="gauge-fill" id="gaugeBar" style="width: 0%;"></div>
      </div>

      <!-- Interactive 84-Day Pipeline Matrix -->
      <div class="matrix-section">
        <div class="matrix-head">
          <span class="matrix-title">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
            90-Day Sprint Matrix (Click any node to navigate)
          </span>
          <div class="matrix-legend">
            <div class="legend-item"><div class="dot-sample todo"></div> Todo</div>
            <div class="legend-item"><div class="dot-sample run"></div> In Progress</div>
            <div class="legend-item"><div class="dot-sample done"></div> Verified</div>
          </div>
        </div>
        <div class="matrix-grid" id="matrixGrid">
          <!-- 84 Interactive Nodes Injected by JS -->
        </div>
      </div>

      <!-- Telemetry Tiles -->
      <div class="cockpit-stats">
        <div class="stat-tile">
          <div class="stat-kicker">Study Duration</div>
          <div class="stat-number" id="valHours">0.0 hrs</div>
          <div class="stat-micro">4.8 hrs / sprint completed (4.5–5.0h budget)</div>
        </div>
        <div class="stat-tile">
          <div class="stat-kicker">Active Streak</div>
          <div class="stat-number" id="valStreak">0 Days</div>
          <div class="stat-micro">Continuous daily cadence</div>
        </div>
        <div class="stat-tile">
          <div class="stat-kicker">Theory Topics</div>
          <div class="stat-number" id="valTheory">360</div>
          <div class="stat-micro">Architectural concepts covered</div>
        </div>
        <div class="stat-tile">
          <div class="stat-kicker">Daily Katas</div>
          <div class="stat-number" id="valKatas">90</div>
          <div class="stat-micro">Focused algorithmic drills (30–45m)</div>
        </div>
        <div class="stat-tile">
          <div class="stat-kicker">Remaining Sprints</div>
          <div class="stat-number" id="valRemaining">90</div>
          <div class="stat-micro">Milestones until target</div>
        </div>
        <div class="stat-tile">
          <div class="stat-kicker">Flagship Repos</div>
          <div class="stat-number" id="valRepos">0 / 3</div>
          <div class="stat-micro">2 Core Flagships + 1 AI Extension</div>
        </div>
      </div>
    </div>

    <!-- Next Up Active Focus Hero Banner -->
    <div class="next-up-strip" id="nextUpBanner">
      <div>
        <div class="next-label">Next Up On Your Radar</div>
        <div class="next-title" id="nextSprintTitle">Day 01: Python Setup, Environment & Primitive Types</div>
        <div class="next-info" id="nextSprintDesc">Phase 1: Python Engineering Foundation • Daily: 4.5–5.0 Hours</div>
      </div>
      <div>
        <button class="tool-btn primary" onclick="jumpToNextSprint()">
          Launch Next Sprint →
        </button>
      </div>
    </div>

    <!-- Phase Navigation Shelf -->
    <div class="phase-shelf">
      <button class="phase-tab active" onclick="setPhase('all', this)">All Curriculum (90 Days)</button>
      <button class="phase-tab" onclick="setPhase('phase1', this)">Phase 1: Python Engineering Foundation (D1–14)</button>
      <button class="phase-tab" onclick="setPhase('phase2', this)">Phase 2: Testing & Pytest Mastery + Security (D15–30)</button>
      <button class="phase-tab" onclick="setPhase('phase3', this)">Phase 3: Flagship API & SQL Reconciliation (D31–45)</button>
      <button class="phase-tab" onclick="setPhase('phase4', this)">Phase 4: Playwright Enterprise Automation (D46–65)</button>
      <button class="phase-tab" onclick="setPhase('phase5', this)">Phase 5: DevOps, Quality Gates & AI Extension (D66–78)</button>
      <button class="phase-tab" onclick="setPhase('phase6', this)">Phase 6: Interview Gauntlet & Career Execution (D79–90)</button>
    </div>

    <!-- Search & Filter Controls -->
    <div class="filter-deck">
      <div class="search-input-wrap">
        <span class="search-sym">/</span>
        <input type="text" id="queryInput" class="search-ctrl" placeholder="Search keywords (e.g. 'Two Sum', 'LRU Cache', 'Playwright', 'Docker', 'MCP')..." oninput="applyFilters()">
      </div>

      <div class="filter-options">
        <button class="pill-filter active" onclick="setStatusFilter('all', this)">All (<span id="cAll">90</span>)</button>
        <button class="pill-filter" onclick="setStatusFilter('completed', this)">Verified (<span id="cPass">0</span>)</button>
        <button class="pill-filter" onclick="setStatusFilter('in-progress', this)">In Progress (<span id="cRun">0</span>)</button>
        <button class="pill-filter" onclick="setStatusFilter('todo', this)">To Do (<span id="cTodo">90</span>)</button>
      </div>

      <div class="filter-options track-switcher">
        <button class="pill-filter track-pill active" onclick="setTrackFilter('all', this)">All Pillars</button>
        <button class="pill-filter track-pill" onclick="setTrackFilter('theory', this)">📚 Theory</button>
        <button class="pill-filter track-pill" onclick="setTrackFilter('coding', this)">💻 Coding</button>
        <button class="pill-filter track-pill" onclick="setTrackFilter('katas', this)">🥋 Katas</button>
        <button class="pill-filter" id="masterExpandBtn" onclick="toggleAllDrawers()" style="border-color:#384d6b; color:#fff;">⤢ Expand All Specs</button>
      </div>
    </div>

    <!-- Sprints Ledger Feed -->
    <div class="sprint-list" id="sprintFeed">
      <!-- 84 Day Cards Injected by JS -->
    </div>

  </div>

  <!-- Minimal DFloating Focus Timer (Red-Team 4.5h Protocol) -->
  <div class="cockpit-timer">
    <div style="display:flex; align-items:center; gap:8px;">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#00f5a0" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <div>
        <div style="font-family:'JetBrains Mono', monospace; font-size:0.65rem; color:var(--text-dim); text-transform:uppercase;">Daily Goal: 4.5–5.0 Hrs</div>
        <div class="timer-readout" id="timerDisplay">04:30:00</div>
      </div>
    </div>
    <div style="display:flex; gap:6px;">
      <button class="timer-action" id="timerStartBtn" onclick="toggleTimer()">Start 4.5h</button>
      <button class="timer-action" onclick="resetTimer()">Reset</button>
    </div>
  </div>

  <!-- Interview Code Vault Modal -->
  <div class="modal-veil" id="codeVaultModal">
    <div class="modal-window">
      <div class="modal-header-row">
        <div>
          <div style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--cyan); text-transform:uppercase;">Technical Reference Library</div>
          <h3 style="font-size:1.2rem; font-weight:700; color:#fff;">Production SDET Implementations</h3>
        </div>
        <button class="close-btn" onclick="closeVault()">✕</button>
      </div>

      <div>
        <h4 style="font-size:0.95rem; color:#fff; font-weight:600;">1. Abstract Base Client with Dunder Representation</h4>
        <pre class="code-frame"><code>from abc import ABC, abstractmethod

class BaseClient(ABC):
    def __init__(self, base_url: str, timeout: int = 30):
        self._base_url = base_url.rstrip("/")
        self.timeout = timeout

    @abstractmethod
    def authenticate(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(base_url='{self._base_url}', timeout={self.timeout})"</code></pre>

        <h4 style="font-size:0.95rem; color:#fff; font-weight:600;">2. API Retry Decorator with Exponential Backoff & Jitter</h4>
        <pre class="code-frame"><code>import functools, random, time
from typing import Callable, Tuple, Type, Any

def retry(
    max_attempts: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    retry_exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except retry_exceptions as exc:
                    last_exc = exc
                    if attempt == max_attempts: break
                    sleep_time = delay + (random.uniform(0, 0.5 * delay) if jitter else 0)
                    time.sleep(sleep_time)
                    delay *= backoff_factor
            raise RuntimeError(f"{func.__name__} failed after {max_attempts} retries") from last_exc
        return wrapper
    return decorator</code></pre>

        <h4 style="font-size:0.95rem; color:#fff; font-weight:600;">3. Playwright StorageState Fast-Forward Auth Fixture</h4>
        <pre class="code-frame"><code>import pytest
from playwright.sync_api import Browser, BrowserContext

@pytest.fixture(scope="session")
def session_auth_state(browser: Browser, tmp_path_factory) -> str:
    state_file = str(tmp_path_factory.mktemp("state") / "auth.json")
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.target.com/login")
    page.get_by_label("Email").fill("test_sdet@target.com")
    page.get_by_label("Password").fill("Secret123!")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url("**/dashboard")
    context.storage_state(path=state_file)
    context.close()
    return state_file

@pytest.fixture
def auth_context(browser: Browser, session_auth_state: str) -> BrowserContext:
    return browser.new_context(storage_state=session_auth_state)</code></pre>

        <h4 style="font-size:0.95rem; color:#fff; font-weight:600;">4. Source-to-Target (S2T) SQL Ledger Reconciliation</h4>
        <pre class="code-frame"><code>WITH refund_summary AS (
    SELECT order_id, SUM(amount) AS total_refunded_items
    FROM refund_items GROUP BY order_id
),
ledger_summary AS (
    SELECT order_id, SUM(transaction_amount) AS total_ledger_recorded
    FROM ledger_transactions WHERE transaction_type = 'REFUND'
    GROUP BY order_id
)
SELECT 
    r.order_id, r.total_refunded_items, l.total_ledger_recorded,
    (r.total_refunded_items - COALESCE(l.total_ledger_recorded, 0)) AS discrepancy
FROM refund_summary r
FULL OUTER JOIN ledger_summary l ON r.order_id = l.order_id
WHERE r.total_refunded_items != l.total_ledger_recorded OR l.total_ledger_recorded IS NULL;</code></pre>
      </div>
    </div>
  </div>

  <!-- Devil's Advocate & Ground Reality Expose Modal -->
  <div class="modal-veil" id="exposeModal">
    <div class="modal-window" style="max-width:980px;">
      <div class="modal-header-row">
        <div>
          <div style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--fail); text-transform:uppercase; letter-spacing:0.06em;">/devils_advocate • /expose • Red-Team Audit Verification</div>
          <h3 style="font-size:1.3rem; font-weight:700; color:#fff;">Red-Team Review & Reality Check: ₹20 LPA Remote SDET</h3>
        </div>
        <button class="close-btn" onclick="closeExposeModal()">✕</button>
      </div>

      <div class="expose-content" style="display:flex; flex-direction:column; gap:20px; font-size:0.88rem; line-height:1.6; color:#d1d9e2;">
        
        <!-- Red-Team Audit Scorecard -->
        <div style="background:var(--bg); border:1px solid #332029; border-left:4px solid var(--fail); border-radius:8px; padding:16px;">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:12px;">
            <h4 style="font-size:1.05rem; color:#fff; font-weight:700; display:flex; align-items:center; gap:8px;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--fail)" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
              1. Red-Team Executive Verdict: Baseline 5.8/10 ➔ Remediated 9.5/10
            </h4>
            <span style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; background:rgba(251, 113, 133, 0.15); color:var(--fail); padding:3px 8px; border-radius:4px; font-weight:600;">Status: Production Ready</span>
          </div>
          <p style="font-size:0.84rem; color:var(--text-muted); margin-bottom:12px;">The original roadmap lacked realistic execution discipline, job search sequencing, and flake post-mortems. Here is the qualitative audit and the fixes implemented:</p>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(170px, 1fr)); gap:10px;">
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border); text-align:center;">
              <div style="font-size:0.75rem; color:var(--text-dim); text-transform:uppercase;">Curriculum</div>
              <div style="font-size:1.2rem; font-weight:700; color:var(--pass);">8/10 ➔ 9.8/10</div>
              <div style="font-size:0.72rem; color:var(--text-muted);">Python, Pytest, Playwright</div>
            </div>
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border); text-align:center;">
              <div style="font-size:0.75rem; color:var(--text-dim); text-transform:uppercase;">Practical Eng</div>
              <div style="font-size:1.2rem; font-weight:700; color:var(--cyan);">7/10 ➔ 9.5/10</div>
              <div style="font-size:0.72rem; color:var(--text-muted);">3 Flake Post-Mortems added</div>
            </div>
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border); text-align:center;">
              <div style="font-size:0.75rem; color:var(--text-dim); text-transform:uppercase;">Portfolio</div>
              <div style="font-size:1.2rem; font-weight:700; color:var(--run);">6/10 ➔ 9.5/10</div>
              <div style="font-size:0.72rem; color:var(--text-muted);">2 Flagships + 1 AI Spec</div>
            </div>
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border); text-align:center;">
              <div style="font-size:0.75rem; color:var(--text-dim); text-transform:uppercase;">Interview Prep</div>
              <div style="font-size:1.2rem; font-weight:700; color:var(--purple);">5/10 ➔ 9.2/10</div>
              <div style="font-size:0.72rem; color:var(--text-muted);">Competency Gates & Defense</div>
            </div>
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border); text-align:center;">
              <div style="font-size:0.75rem; color:var(--text-dim); text-transform:uppercase;">Career Strategy</div>
              <div style="font-size:1.2rem; font-weight:700; color:var(--fail); font-weight:700;">3/10 ➔ 9.4/10</div>
              <div style="font-size:0.72rem; color:var(--text-muted);">Week 2, 5, 8 Applications</div>
            </div>
          </div>
        </div>

        <!-- Compensation Math Card -->
        <div style="background:var(--bg); border:1px solid #1a2a40; border-left:4px solid var(--cyan); border-radius:8px; padding:16px;">
          <h4 style="font-size:1.05rem; color:#fff; font-weight:700; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--cyan)" stroke-width="2.5"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
            2. Realistic Compensation Bands & The Contractor Net Advantage
          </h4>
          <p>Hiring committees for 1–3 YOE evaluate engineering output, not 90-day promises. Here is the realistic compensation breakdown:</p>
          <ul style="margin:10px 0 10px 20px;">
            <li><strong>Primary Target:</strong> <strong>₹15–20 LPA Fixed Gross</strong> in top Indian tech product companies or funded scale-ups.</li>
            <li><strong>Stretch Target:</strong> <strong>₹20 LPA+ Fixed Gross</strong> for standout candidates demonstrating deep parallel fixture engineering and database reconciliation.</li>
            <li><strong>Exceptional Outcome (US/EU B2B Remote):</strong> $28,000–$36,000 USD/year (~₹23L–₹30L INR) via Deel or Remote. Under <strong>Section 44ADA presumptive taxation</strong> (50% expense deduction) and 0% LUT GST on software exports, total income tax drops to ~₹1.2L/year, resulting in <strong>₹20 LPA+ net take-home</strong>!</li>
          </ul>
        </div>

        <!-- Early Job Search Strategy Card -->
        <div style="background:var(--bg); border:1px solid #202b40; border-left:4px solid var(--run); border-radius:8px; padding:16px;">
          <h4 style="font-size:1.05rem; color:#fff; font-weight:700; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--run)" stroke-width="2.5"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path></svg>
            3. Early Recruitment Sequencing (Never Wait for Day 84)
          </h4>
          <p>Remote recruitment cycles take 3 to 6 weeks. Applying on Day 84 is a fatal flaw. The curriculum enforces early application gates:</p>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:12px; margin-top:10px;">
            <div style="background:var(--surface-elevated); padding:12px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--pass);">Week 2 (Day 14): Market Calibration</strong>
              <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Audit 20 live remote JDs, calibrate ATS keywords, set up LinkedIn/Wellfound alert filters, and draft the core engineering resume.</p>
            </div>
            <div style="background:var(--surface-elevated); padding:12px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--pass);">Week 5 (Day 35): Targeted Pilot Push</strong>
              <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Release Flagship Repo 1 (API & SQL Reconciliation). Dispatch 10–15 targeted applications to test resume ATS conversion and recruiter reply rates.</p>
            </div>
            <div style="background:var(--surface-elevated); padding:12px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--pass);">Week 8 (Day 56): Sustained Campaign</strong>
              <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Release Flagship Repo 2 (Playwright). Launch 20–25 applications weekly to seed take-homes and live screens for Weeks 11–13.</p>
            </div>
            <div style="background:var(--surface-elevated); padding:12px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--pass);">Weeks 11–13: Interview Gauntlet</strong>
              <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Take-home simulation, live machine coding drills, architectural system design defense, and multi-offer compensation negotiation.</p>
            </div>
          </div>
        </div>

        <!-- 5 Deadly Traps Card -->
        <div style="background:var(--bg); border:1px solid #202b40; border-left:4px solid var(--fail); border-radius:8px; padding:16px;">
          <h4 style="font-size:1.05rem; color:#fff; font-weight:700; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--fail)" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
            4. The 5 Deadly Traps That Eliminate 95% of Candidates
          </h4>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:12px; margin-top:10px;">
            <div style="background:var(--surface-elevated); padding:12px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--fail);">Trap 1: Tutorial Hell</strong>
              <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Watching 60 hours of video courses without building a framework from scratch in an empty directory. In live rounds, you freeze without autocomplete.</p>
            </div>
            <div style="background:var(--surface-elevated); padding:12px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--fail);">Trap 2: Monolithic POM</strong>
              <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Putting locators and business logic in giant 600-line page classes. Modern SDETs use Component-Driven POM with fluent interfaces.</p>
            </div>
            <div style="background:var(--surface-elevated); padding:12px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--fail);">Trap 3: Parallel State Collision</strong>
              <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Tests pass sequentially but fail in <code>pytest -n 4</code> because of hardcoded usernames, shared DB rows, or missing worker isolation.</p>
            </div>
            <div style="background:var(--surface-elevated); padding:12px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--fail);">Trap 4: Blind AI Confidence</strong>
              <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Accepting weak AI assertions like <code>assert status == 200</code> without checking JSON contracts, schema types, or database persistence. Fixed with mutation testing (<code>mutmut</code>).</p>
            </div>
            <div style="background:var(--surface-elevated); padding:12px; border-radius:6px; border:1px solid var(--border); grid-column:1/-1;">
              <strong style="color:var(--fail);">Trap 5: Lone-Wolf Remote Disconnect</strong>
              <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Failing to communicate asynchronously. Remote companies evaluate your PR descriptions, 3-minute Loom video handoffs, and Docker 1-line reproducibility.</p>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- 3 Competency Quality Gates Modal -->
  <div class="modal-veil" id="gatesModal">
    <div class="modal-window" style="max-width:980px;">
      <div class="modal-header-row">
        <div>
          <div style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--run); text-transform:uppercase; letter-spacing:0.06em;">Technical Competency Verification System</div>
          <h3 style="font-size:1.3rem; font-weight:700; color:#fff;">The 3 Quality Gates: Build, Debug & Defend</h3>
        </div>
        <button class="close-btn" onclick="closeGatesModal()">✕</button>
      </div>

      <div style="display:flex; flex-direction:column; gap:20px;">
        
        <!-- Gate A -->
        <div style="background:var(--bg); border:1px solid var(--border); border-left:4px solid var(--cyan); border-radius:8px; padding:18px;">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
            <h4 style="font-size:1.1rem; color:#fff; font-weight:700;">Gate A: Can You Build It? (Construction & Production Architecture)</h4>
            <span style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--cyan); background:rgba(56, 189, 248, 0.15); padding:3px 8px; border-radius:4px;">Core Engineering</span>
          </div>
          <p style="font-size:0.84rem; color:var(--text-muted); margin:6px 0 12px;">Hiring managers test if you can construct clean, maintainable automation from an empty directory without copy-pasting tutorials.</p>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:10px; font-size:0.82rem;">
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--cyan);">1. Parallel-Isolated Fixtures:</strong>
              <div style="color:var(--text-muted); margin-top:2px;">Pytest tiered fixtures with UUID isolation; zero cross-test state leakage under <code>pytest -n auto</code>.</div>
            </div>
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--cyan);">2. Component-Driven POM:</strong>
              <div style="color:var(--text-muted); margin-top:2px;">Independent reusable components (NavBar, DataTable, Modal) rather than brittle 600-line monolithic pages.</div>
            </div>
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--cyan);">3. Dynamic Contract Validation:</strong>
              <div style="color:var(--text-muted); margin-top:2px;">Dual-layer validation: JSONSchema for structural contracts and Pydantic v2 for semantic business logic constraints.</div>
            </div>
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--cyan);">4. 1-Line Docker Reproducibility:</strong>
              <div style="color:var(--text-muted); margin-top:2px;">Runs in any CI/CD environment with <code>docker compose run --rm tests</code>; zero local setup dependencies.</div>
            </div>
          </div>
        </div>

        <!-- Gate B -->
        <div style="background:var(--bg); border:1px solid var(--border); border-left:4px solid var(--pass); border-radius:8px; padding:18px;">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
            <h4 style="font-size:1.1rem; color:#fff; font-weight:700;">Gate B: Can You Debug It? (Empirical Flake Post-Mortems)</h4>
            <span style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--pass); background:rgba(0, 245, 160, 0.15); padding:3px 8px; border-radius:4px;">Seniority Differentiator</span>
          </div>
          <p style="font-size:0.84rem; color:var(--text-muted); margin:6px 0 12px;">Junior engineers write tests. Senior SDETs diagnose and eliminate the flaky failures that cost engineering teams thousands of hours.</p>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:10px; font-size:0.82rem;">
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--fail);">Post-Mortem 1: React 18 Hydration Race</strong>
              <div style="color:var(--text-muted); margin-top:2px;"><strong>Root Cause:</strong> DOM elements render before JavaScript event listeners hydrate.<br><strong>Fix:</strong> Replace static wait with <code>page.wait_for_load_state("networkidle")</code> and web-first state assertion.</div>
            </div>
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--fail);">Post-Mortem 2: Docker /dev/shm Exhaustion</strong>
              <div style="color:var(--text-muted); margin-top:2px;"><strong>Root Cause:</strong> Default Docker container allocates only 64MB shared memory; Chromium crashes under parallel workers.<br><strong>Fix:</strong> Configure <code>shm_size: '2gb'</code> or launch Chromium with <code>--disable-dev-shm-usage</code>.</div>
            </div>
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--fail);">Post-Mortem 3: Mutable Fixture State Collision</strong>
              <div style="color:var(--text-muted); margin-top:2px;"><strong>Root Cause:</strong> Session fixture returned a mutable dict; Test B mutated payload, causing Test C to fail intermittently.<br><strong>Fix:</strong> Factory fixtures returning <code>copy.deepcopy()</code> and dynamic DB records with unique UUIDs.</div>
            </div>
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--purple);">Mutation Testing Verification (mutmut)</strong>
              <div style="color:var(--text-muted); margin-top:2px;"><strong>Proof of Assertions:</strong> Running <code>mutmut run</code> injects deliberate mutants into code. If tests still pass, assertions are weak/hallucinated. Eliminates false confidence.</div>
            </div>
          </div>
        </div>

        <!-- Gate C -->
        <div style="background:var(--bg); border:1px solid var(--border); border-left:4px solid var(--purple); border-radius:8px; padding:18px;">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
            <h4 style="font-size:1.1rem; color:#fff; font-weight:700;">Gate C: Can You Defend It? (Architectural Trade-Offs & Async Remote Comms)</h4>
            <span style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--purple); background:rgba(192, 132, 252, 0.15); padding:3px 8px; border-radius:4px;">Hiring Committee Decision</span>
          </div>
          <p style="font-size:0.84rem; color:var(--text-muted); margin:6px 0 12px;">Senior SDET interviews test your ability to defend design decisions against Staff Engineers and communicate asynchronously.</p>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:10px; font-size:0.82rem;">
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--purple);">HTTPX vs Requests:</strong>
              <div style="color:var(--text-muted); margin-top:2px;">HTTPX supports HTTP/2, connection pooling, and identical sync/async APIs, preparing test suites for high-concurrency performance loads.</div>
            </div>
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--purple);">CDP WebSocket vs Selenium WebDriver:</strong>
              <div style="color:var(--text-muted); margin-top:2px;">Playwright speaks directly over a single WebSocket connection, avoiding WebDriver's JSON-over-HTTP per-action latency and enabling native auto-waiting.</div>
            </div>
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--purple);">StorageState vs UI Login:</strong>
              <div style="color:var(--text-muted); margin-top:2px;">Authenticating once and re-using cookies/tokens in <code>BrowserContext(storage_state=...)</code> cuts suite execution time by 60%+ while avoiding flakiness.</div>
            </div>
            <div style="background:var(--surface-elevated); padding:10px; border-radius:6px; border:1px solid var(--border);">
              <strong style="color:var(--purple);">Asynchronous PR & Loom Handoff:</strong>
              <div style="color:var(--text-muted); margin-top:2px;">Remote teams judge pull requests by their clarity: Mermaid diagrams, reproducible CLI steps, and 3-minute video demos showing trace artifact analysis.</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- 3 Flagship Capstone Portfolio Repositories Modal -->
  <div class="modal-veil" id="reposModal">
    <div class="modal-window" style="max-width:980px;">
      <div class="modal-header-row">
        <div>
          <div style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--cyan); text-transform:uppercase; letter-spacing:0.06em;">Portfolio Tier-1 Architecture</div>
          <h3 style="font-size:1.3rem; font-weight:700; color:#fff;">The 2 Core Flagship Repositories + 1 AI Specialization Extension</h3>
        </div>
        <button class="close-btn" onclick="closeReposModal()">✕</button>
      </div>

      <div style="display:flex; flex-direction:column; gap:22px;">

        <!-- Capstone 1 -->
        <div style="background:var(--bg); border:1px solid var(--border); border-radius:10px; padding:18px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:8px;">
            <div>
              <span style="font-family:'JetBrains Mono', monospace; font-size:0.7rem; background:rgba(56, 189, 248, 0.15); color:var(--cyan); padding:2px 8px; border-radius:4px; font-weight:600;">FLAGSHIP REPO #1 • API & DATA INTEGRITY</span>
              <h4 style="font-size:1.15rem; color:#fff; font-weight:700; margin-top:4px;">api-reliability-data-validator</h4>
              <p style="font-size:0.83rem; color:var(--text-muted);">High-Throughput Fintech Payment Engine & PostgreSQL Reconciliation Platform</p>
            </div>
            <span style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--pass); background:var(--surface-elevated); padding:4px 10px; border-radius:4px; border:1px solid var(--border);">Pytest • HTTPX • Pydantic v2 • SQLAlchemy • Docker</span>
          </div>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:14px;">
            <div>
              <strong style="font-size:0.8rem; color:#fff; text-transform:uppercase; font-family:'JetBrains Mono', monospace;">Directory Architecture:</strong>
              <pre class="code-frame" style="font-size:0.72rem; line-height:1.4; margin:6px 0 0;"><code>api-reliability-data-validator/
├── .github/workflows/api-tests.yml
├── config/settings.py (Pydantic BaseSettings)
├── core/
│   ├── client.py (HTTPX session + telemetry)
│   ├── auth.py (OAuth2 auto-refresh JWT)
│   ├── decorators.py (Retry with jitter)
│   └── exceptions.py (Custom hierarchy)
├── data/
│   ├── factories.py (Faker dynamic builders)
│   └── schemas/ (JSONSchema draft-07)
├── db/
│   ├── connection.py (SQLAlchemy pool)
│   └── queries.py (S2T ledger joins)
├── tests/conftest.py (Tiered fixtures)
├── Dockerfile & docker-compose.yml
└── README.md (Mermaid diagram + Loom)</code></pre>
            </div>
            <div style="font-size:0.82rem; color:var(--text-muted); display:flex; flex-direction:column; gap:8px;">
              <strong style="font-size:0.8rem; color:#fff; text-transform:uppercase; font-family:'JetBrains Mono', monospace;">Core Engineering Innovations:</strong>
              <div>• <strong>OAuth2 Auto-Refresh:</strong> Inspects JWT <code>exp</code> claim; automatically refreshes token before dispatch if < 60s remain.</div>
              <div>• <strong>Resilient Jitter Retry:</strong> Exponential backoff with full randomized jitter preventing thundering herd on 429/503.</div>
              <div>• <strong>Dual Contract Guard:</strong> JSONSchema for strict syntax + Pydantic v2 for business-logic semantic constraints.</div>
              <div>• <strong>S2T DB Reconciliation:</strong> Joins API payload with PostgreSQL ledger across 4 tables in $O(N)$ hash map check.</div>
            </div>
          </div>
        </div>

        <!-- Capstone 2 -->
        <div style="background:var(--bg); border:1px solid var(--border); border-radius:10px; padding:18px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:8px;">
            <div>
              <span style="font-family:'JetBrains Mono', monospace; font-size:0.7rem; background:rgba(0, 245, 160, 0.15); color:var(--pass); padding:2px 8px; border-radius:4px; font-weight:600;">FLAGSHIP REPO #2 • WEB & HYBRID E2E</span>
              <h4 style="font-size:1.15rem; color:#fff; font-weight:700; margin-top:4px;">playwright-python-enterprise-engine</h4>
              <p style="font-size:0.83rem; color:var(--text-muted);">Enterprise B2B SaaS Automation with Network Mocking, Auth State & Flake Isolation</p>
            </div>
            <span style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--cyan); background:var(--surface-elevated); padding:4px 10px; border-radius:4px; border:1px solid var(--border);">Playwright • Python • POM • pytest-xdist • Traces</span>
          </div>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:14px;">
            <div>
              <strong style="font-size:0.8rem; color:#fff; text-transform:uppercase; font-family:'JetBrains Mono', monospace;">Directory Architecture:</strong>
              <pre class="code-frame" style="font-size:0.72rem; line-height:1.4; margin:6px 0 0;"><code>playwright-python-enterprise-engine/
├── .github/workflows/e2e-matrix.yml
├── auth/user_state.json (StorageState)
├── components/ (Navbar, DataTable, Modal)
├── pages/ (Component-driven BasePage)
├── utils/
│   ├── interceptor.py (Route mock/abort)
│   └── trace_manager.py (trace.zip)
├── tests/
│   ├── conftest.py (BrowserContext pool)
│   ├── test_hybrid_flow.py (API seeded)
│   └── test_network_errors.py (500 stubs)
├── Dockerfile & pytest.ini
└── README.md (Trace viewer walkthrough)</code></pre>
            </div>
            <div style="font-size:0.82rem; color:var(--text-muted); display:flex; flex-direction:column; gap:8px;">
              <strong style="font-size:0.8rem; color:#fff; text-transform:uppercase; font-family:'JetBrains Mono', monospace;">Core Engineering Innovations:</strong>
              <div>• <strong>StorageState Caching:</strong> Pre-authenticates via API/UI once; subsequent tests launch logged-in, saving 65% time.</div>
              <div>• <strong>Network Route Interception:</strong> Blocks heavy media/analytics assets and stubs backend 500/504 errors deterministically.</div>
              <div>• <strong>API-Seeded Test Workflows:</strong> Seeds test data via backend API in < 400ms before triggering browser interactions.</div>
              <div>• <strong>Trace Viewer Auto-Capture:</strong> Captures full DOM, screenshots, and network waterfall only on failure, zero overhead on pass.</div>
            </div>
          </div>
        </div>

        <!-- Capstone 3 -->
        <div style="background:var(--bg); border:1px solid var(--border); border-radius:10px; padding:18px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:8px;">
            <div>
              <span style="font-family:'JetBrains Mono', monospace; font-size:0.7rem; background:rgba(192, 132, 252, 0.15); color:var(--purple); padding:2px 8px; border-radius:4px; font-weight:600;">FLAGSHIP REPO #3 • AI & AGENTIC TESTING</span>
              <h4 style="font-size:1.15rem; color:#fff; font-weight:700; margin-top:4px;">testops-mcp-diagnostic-agent</h4>
              <p style="font-size:0.83rem; color:var(--text-muted);">Autonomous QA Platform with Playwright MCP Server, Failure Triager & Hallucination Auditor</p>
            </div>
            <span style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--purple); background:var(--surface-elevated); padding:4px 10px; border-radius:4px; border:1px solid var(--border);">MCP Protocol • Claude Code • AST Analysis • LLM Evals</span>
          </div>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:14px;">
            <div>
              <strong style="font-size:0.8rem; color:#fff; text-transform:uppercase; font-family:'JetBrains Mono', monospace;">Directory Architecture:</strong>
              <pre class="code-frame" style="font-size:0.72rem; line-height:1.4; margin:6px 0 0;"><code>testops-mcp-diagnostic-agent/
├── mcp_server/
│   ├── server.py (JSON-RPC 2.0 MCP)
│   └── tools/browser_tools.py (Playwright)
├── agents/
│   ├── exploratory_agent.py (Autonomous)
│   ├── triage_agent.py (CI log triager)
│   └── audit_agent.py (AST weak assert)
├── prompts/ (Grounded schemas & templates)
├── tests/test_mcp_integration.py
├── Dockerfile & pyproject.toml
└── README.md (MCP architecture guide)</code></pre>
            </div>
            <div style="font-size:0.82rem; color:var(--text-muted); display:flex; flex-direction:column; gap:8px;">
              <strong style="font-size:0.8rem; color:#fff; text-transform:uppercase; font-family:'JetBrains Mono', monospace;">Core Engineering Innovations:</strong>
              <div>• <strong>Model Context Protocol (MCP) Server:</strong> Exposes browser automation actions to AI agents over standard JSON-RPC 2.0.</div>
              <div>• <strong>Autonomous Exploratory Agent:</strong> Navigates journeys from English goals, detects uncaught JS errors, and logs repro steps.</div>
              <div>• <strong>Automated CI Failure Triager:</strong> Post-mortem hook that analyzes stack traces & network waterfalls to categorize bugs vs flakes.</div>
              <div>• <strong>AST Assertion Auditor:</strong> Scans test suites for weak assertions (e.g. status 200 without payload validation) and false confidence.</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- Live Machine Coding Battle Drills Modal -->
  <div class="modal-veil" id="drillsModal">
    <div class="modal-window" style="max-width:980px;">
      <div class="modal-header-row">
        <div>
          <div style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--purple); text-transform:uppercase; letter-spacing:0.06em;">Live Technical Screening Drills</div>
          <h3 style="font-size:1.3rem; font-weight:700; color:#fff;">Machine Coding Battle Drills (60-Min Live Challenge Solutions)</h3>
        </div>
        <button class="close-btn" onclick="closeDrillsModal()">✕</button>
      </div>

      <div style="display:flex; flex-direction:column; gap:20px;">

        <div>
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <h4 style="font-size:1.0rem; color:#fff; font-weight:600;">Drill 1: Resilient API Retry Engine with Jitter & Custom Exceptions</h4>
            <span style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--pass);">Pattern: Decorators + Closures</span>
          </div>
          <p style="font-size:0.82rem; color:var(--text-muted); margin-top:2px;">Asked in live screens to test advanced Python OOP, decorators, and exponential backoff implementation without libraries.</p>
          <pre class="code-frame"><code>import functools, random, time
from typing import Callable, Tuple, Type, Any

class MaxRetriesExceededError(Exception):
    def __init__(self, message: str, attempts: int, last_exception: Exception):
        super().__init__(f"{message} (Failed after {attempts} attempts)")
        self.attempts = attempts
        self.last_exception = last_exception

def resilient_retry(
    max_retries: int = 3,
    base_delay: float = 1.0,
    backoff_factor: float = 2.0,
    handled_exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 1
            while attempt <= max_retries:
                try:
                    return func(*args, **kwargs)
                except handled_exceptions as exc:
                    if attempt == max_retries:
                        raise MaxRetriesExceededError(
                            f"Execution failed for '{func.__name__}'",
                            attempts=attempt,
                            last_exception=exc,
                        ) from exc
                    max_sleep = base_delay * (backoff_factor ** (attempt - 1))
                    sleep_duration = random.uniform(0.5 * max_sleep, max_sleep)
                    time.sleep(sleep_duration)
                    attempt += 1
        return wrapper
    return decorator</code></pre>
        </div>

        <div>
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <h4 style="font-size:1.0rem; color:#fff; font-weight:600;">Drill 2: Deep Recursive JSON Difference & Schema Reconciliation</h4>
            <span style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--cyan);">Pattern: Recursion + Sets</span>
          </div>
          <p style="font-size:0.82rem; color:var(--text-muted); margin-top:2px;">Validates nested API response structures against expected contracts, capturing path-level missing/extra keys and value mismatches.</p>
          <pre class="code-frame"><code>from typing import Any, Dict, List

def compare_json_structures(expected: Any, actual: Any, path: str = "") -> Dict[str, List[str]]:
    diffs = {"missing_keys": [], "unexpected_keys": [], "value_mismatches": [], "type_mismatches": []}
    current_path = path if path else "root"

    if type(expected) is not type(actual):
        diffs["type_mismatches"].append(f"{current_path}: expected {type(expected).__name__}, got {type(actual).__name__}")
        return diffs

    if isinstance(expected, dict):
        exp_keys, act_keys = set(expected.keys()), set(actual.keys())
        for k in exp_keys - act_keys: diffs["missing_keys"].append(f"{current_path}.{k}")
        for k in act_keys - exp_keys: diffs["unexpected_keys"].append(f"{current_path}.{k}")
        for common_k in exp_keys & act_keys:
            nested = compare_json_structures(expected[common_k], actual[common_k], path=f"{current_path}.{common_k}")
            for cat, items in nested.items(): diffs[cat].extend(items)
    elif isinstance(expected, list):
        if len(expected) != len(actual):
            diffs["value_mismatches"].append(f"{current_path}: array length mismatch ({len(expected)} vs {len(actual)})")
        for idx, (exp_i, act_i) in enumerate(zip(expected, actual)):
            nested = compare_json_structures(exp_i, act_i, path=f"{current_path}[{idx}]")
            for cat, items in nested.items(): diffs[cat].extend(items)
    else:
        if expected != actual:
            diffs["value_mismatches"].append(f"{current_path}: expected '{expected}', got '{actual}'")
    return diffs</code></pre>
        </div>

        <div>
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <h4 style="font-size:1.0rem; color:#fff; font-weight:600;">Drill 3: High-Performance Database-to-API Reconciliation Engine</h4>
            <span style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--purple);">Pattern: O(N) Hash Map + Batch SQL</span>
          </div>
          <p style="font-size:0.82rem; color:var(--text-muted); margin-top:2px;">Tests source-to-target data integrity for 1,000+ accounts between REST API endpoints and PostgreSQL tables without memory overflow.</p>
          <pre class="code-frame"><code>from decimal import Decimal

def test_reconcile_api_with_database(api_client, db_connection):
    response = api_client.get("/api/v1/accounts/summary")
    assert response.status_code == 200
    api_records = response.json()["accounts"]
    account_ids = [acc["account_id"] for acc in api_records]

    query = "SELECT account_id, balance, status FROM accounts_ledger WHERE account_id = ANY(%s);"
    with db_connection.cursor() as cursor:
        cursor.execute(query, (account_ids,))
        db_rows = cursor.fetchall()

    db_map = {row["account_id"]: {"balance": Decimal(str(row["balance"])), "status": row["status"]} for row in db_rows}
    discrepancies = []

    for api_acc in api_records:
        acc_id = api_acc["account_id"]
        api_bal, api_st = Decimal(str(api_acc["balance"])), api_acc["status"]
        if acc_id not in db_map:
            discrepancies.append(f"Account {acc_id} missing in DB")
            continue
        db_acc = db_map[acc_id]
        if api_bal != db_acc["balance"]:
            discrepancies.append(f"Balance mismatch {acc_id}: API={api_bal}, DB={db_acc['balance']}")
        if api_st != db_acc["status"]:
            discrepancies.append(f"Status mismatch {acc_id}: API={api_st}, DB={db_acc['status']}")

    assert not discrepancies, f"Found {len(discrepancies)} discrepancies:
" + "
".join(discrepancies[:5])</code></pre>
        </div>

      </div>
    </div>
  </div>

  <script>
    const RAW_DAYS = __DAYS_DATA_PLACEHOLDER__;
    const STORAGE_KEY = "sdet_cockpit_state_v4";

    let state = {
      entries: {},
      phase: "all",
      status: "all",
      trackMode: "all",
      query: ""
    };

    function setTrackFilter(mode, elem) {
      state.trackMode = mode;
      document.querySelectorAll(".track-pill").forEach(p => p.classList.remove("active"));
      if (elem) elem.classList.add("active");
      const feed = document.getElementById("sprintFeed");
      if (feed) {
        feed.setAttribute("data-track-focus", mode);
      }
    }

    function toggleKataHint(dayNum) {
      const vault = document.getElementById("kataVault-" + dayNum);
      const btn = document.getElementById("kataHintBtn-" + dayNum);
      if (vault) {
        const isShown = vault.classList.contains("visible");
        if (isShown) {
          vault.classList.remove("visible");
          btn.innerText = "Reveal Solution Approach & Hint";
        } else {
          vault.classList.add("visible");
          btn.innerText = "Hide Solution Approach";
        }
      }
    }

    let allDrawersExpanded = false;
    function toggleAllDrawers() {
      allDrawersExpanded = !allDrawersExpanded;
      const drawers = document.querySelectorAll(".inspection-drawer");
      const buttons = document.querySelectorAll(".inspect-btn");
      const masterBtn = document.getElementById("masterExpandBtn");

      drawers.forEach(d => {
        if (allDrawersExpanded) d.classList.add("open");
        else d.classList.remove("open");
      });
      buttons.forEach(b => {
        b.innerHTML = allDrawersExpanded ? "Collapse Specs ↑" : "Inspect Sprint Specs ↓";
      });
      if (masterBtn) {
        masterBtn.innerText = allDrawersExpanded ? "⤡ Collapse All Specs" : "⤢ Expand All Specs";
      }
    }

    function loadState() {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        try {
          const parsed = JSON.parse(saved);
          state.entries = parsed.entries || {};
        } catch(e) {
          console.error("State parse error", e);
        }
      }
    }

    function persistState() {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({ entries: state.entries }));
      updateCockpitUI();
    }

    function setPhase(phaseId, elem) {
      state.phase = phaseId;
      document.querySelectorAll(".phase-tab").forEach(t => t.classList.remove("active"));
      elem.classList.add("active");
      renderFeed();
    }

    function setStatusFilter(statusId, elem) {
      state.status = statusId;
      document.querySelectorAll(".pill-filter").forEach(p => p.classList.remove("active"));
      elem.classList.add("active");
      renderFeed();
    }

    function applyFilters() {
      state.query = document.getElementById("queryInput").value.toLowerCase().trim();
      renderFeed();
    }

    function toggleSprint(dayNum) {
      const e = state.entries[dayNum] || { status: "todo", notes: "", link: "" };
      e.status = (e.status === "completed") ? "todo" : "completed";
      state.entries[dayNum] = e;
      persistState();
      renderFeed();
      renderMatrix();
    }

    function changeSprintStatus(dayNum, selectElem) {
      const e = state.entries[dayNum] || { status: "todo", notes: "", link: "" };
      e.status = selectElem.value;
      state.entries[dayNum] = e;
      persistState();
      renderFeed();
      renderMatrix();
    }

    function saveNotes(dayNum, val) {
      const e = state.entries[dayNum] || { status: "todo", notes: "", link: "" };
      e.notes = val;
      state.entries[dayNum] = e;
      persistState();
      flashSaved(dayNum);
    }

    function saveLink(dayNum, val) {
      const e = state.entries[dayNum] || { status: "todo", notes: "", link: "" };
      e.link = val;
      state.entries[dayNum] = e;
      persistState();
      flashSaved(dayNum);
    }

    function flashSaved(dayNum) {
      const badge = document.getElementById("saveBadge-" + dayNum);
      if (badge) {
        badge.classList.add("shown");
        setTimeout(() => badge.classList.remove("shown"), 1300);
      }
    }

    function toggleDrawer(dayNum) {
      const drawer = document.getElementById("drawer-" + dayNum);
      const btn = document.getElementById("inspectBtn-" + dayNum);
      if (drawer) {
        const isOpen = drawer.classList.contains("open");
        if (isOpen) {
          drawer.classList.remove("open");
          btn.innerHTML = "Inspect Sprint Specs ↓";
        } else {
          drawer.classList.add("open");
          btn.innerHTML = "Collapse Specs ↑";
        }
      }
    }

    function toggleAnswer(dayNum) {
      const vault = document.getElementById("answerVault-" + dayNum);
      const btn = document.getElementById("revealTrigger-" + dayNum);
      if (vault) {
        const isShown = vault.classList.contains("visible");
        if (isShown) {
          vault.classList.remove("visible");
          btn.innerText = "Reveal Technical Rationale";
        } else {
          vault.classList.add("visible");
          btn.innerText = "Hide Rationale";
        }
      }
    }

    function copyToClipboard(text, btn) {
      navigator.clipboard.writeText(text).then(() => {
        const old = btn.innerText;
        btn.innerText = "Copied ✓";
        setTimeout(() => { btn.innerText = old; }, 1400);
      });
    }

    function jumpToDay(dayNum) {
      state.phase = "all";
      state.status = "all";
      state.query = "";
      document.getElementById("queryInput").value = "";
      document.querySelectorAll(".phase-tab").forEach((t, i) => t.classList.toggle("active", i === 0));
      document.querySelectorAll(".pill-filter").forEach((p, i) => p.classList.toggle("active", i === 0));
      renderFeed();
      setTimeout(() => {
        const el = document.getElementById("sprintCard-" + dayNum);
        if (el) {
          el.scrollIntoView({ behavior: "smooth", block: "center" });
          el.style.borderColor = "var(--pass)";
          setTimeout(() => { el.style.borderColor = ""; }, 2000);
        }
      }, 80);
    }

    function jumpToNextSprint() {
      let nextDay = 1;
      for (const d of RAW_DAYS) {
        const s = (state.entries[d.day] && state.entries[d.day].status) || "todo";
        if (s !== "completed") {
          nextDay = d.day;
          break;
        }
      }
      jumpToDay(nextDay);
    }

    function matchesPhase(dayNum, ph) {
      if (ph === "all") return true;
      if (ph === "phase1") return dayNum >= 1 && dayNum <= 14;
      if (ph === "phase2") return dayNum >= 15 && dayNum <= 30;
      if (ph === "phase3") return dayNum >= 31 && dayNum <= 45;
      if (ph === "phase4") return dayNum >= 46 && dayNum <= 65;
      if (ph === "phase5") return dayNum >= 66 && dayNum <= 78;
      if (ph === "phase6") return dayNum >= 79 && dayNum <= 90;
      return true;
    }

    /* Render 84 Matrix Nodes */
    function renderMatrix() {
      const container = document.getElementById("matrixGrid");
      container.innerHTML = "";

      RAW_DAYS.forEach(d => {
        const entry = state.entries[d.day] || { status: "todo" };
        const st = entry.status || "todo";

        const node = document.createElement("div");
        node.className = `matrix-cell ${st}`;
        node.innerText = d.day;
        node.title = `Day ${d.day}: ${d.title} (${st})`;
        node.onclick = () => jumpToDay(d.day);

        container.appendChild(node);
      });
    }

    /* Render Sprints List */
    function renderFeed() {
      const container = document.getElementById("sprintFeed");
      container.innerHTML = "";

      let count = 0;

      RAW_DAYS.forEach(item => {
        if (!matchesPhase(item.day, state.phase)) return;

        const current = state.entries[item.day] || { status: "todo", notes: "", link: "" };
        const status = current.status || "todo";

        if (state.status === "completed" && status !== "completed") return;
        if (state.status === "in-progress" && status !== "in-progress") return;
        if (state.status === "todo" && status !== "todo") return;

        if (state.query) {
          const hay = (
            item.title + " " +
            item.category + " " +
            (item.theory_topics || []).join(" ") + " " +
            (item.coding_topics || []).join(" ") + " " +
            (item.katas_topics || []).join(" ") + " " +
            (item.kata_challenge ? (item.kata_challenge.title + " " + item.kata_challenge.pattern + " " + item.kata_challenge.description) : "") + " " +
            item.assignment + " " +
            item.deliverable + " " +
            item.interviewQ
          ).toLowerCase();
          if (!hay.includes(state.query)) return;
        }

        count++;

        const isDone = status === "completed";
        const isRun = status === "in-progress";
        const padDay = item.day.toString().padStart(2, '0');

        const theoryList = (item.theory_topics && item.theory_topics.length) ? item.theory_topics : (item.concepts || []);
        const codingList = (item.coding_topics && item.coding_topics.length) ? item.coding_topics : [item.assignment];
        const katasList = (item.katas_topics && item.katas_topics.length) ? item.katas_topics : ["Algorithmic Katas Practice (1.0h)"];
        const challenge = item.kata_challenge || {
          title: "Daily Coding Kata Practice",
          difficulty: "Medium",
          pattern: "Algorithmic Problem Solving",
          description: "Complete daily 1.0h algorithmic kata session focusing on time & space complexity constraints.",
          hint: "Think out loud, state Big-O bounds, and write unit assertions."
        };

        const card = document.createElement("div");
        card.className = `sprint-card ${isDone ? 'completed' : ''} ${isRun ? 'in-progress' : ''}`;
        card.id = `sprintCard-${item.day}`;

        card.innerHTML = `
          <div class="sprint-main">
            <div class="sprint-left">
              <span class="sprint-idx">#${padDay}</span>
              <input type="checkbox" class="sprint-check" ${isDone ? 'checked' : ''} onchange="toggleSprint(${item.day})">
              <div class="sprint-body">
                <div class="sprint-tags">
                  <span class="tag-token">WEEK ${item.week}</span>
                  <span class="tag-category">${item.category}</span>
                  <span class="tag-time">${item.timebox}</span>
                </div>
                <h3 class="sprint-name">${item.title}</h3>

                <!-- Everyday Activity 3-Pillar Breakdown: Theory, Coding, Katas -->
                <div class="activity-pillars">
                  <div class="pillar-col pillar-theory">
                    <div class="pillar-head">
                      <span class="pillar-tag theory">📚 Theory Topics</span>
                      <span class="pillar-time">45m</span>
                    </div>
                    <ul class="pillar-list">
                      ${theoryList.map(t => `<li class="pillar-item"><span class="pillar-marker theory">›</span><span>${t}</span></li>`).join('')}
                    </ul>
                  </div>

                  <div class="pillar-col pillar-coding">
                    <div class="pillar-head">
                      <span class="pillar-tag coding">💻 Coding Topics</span>
                      <span class="pillar-time">2.5h</span>
                    </div>
                    <ul class="pillar-list">
                      ${codingList.map(c => `<li class="pillar-item"><span class="pillar-marker coding">›</span><span>${c}</span></li>`).join('')}
                    </ul>
                  </div>

                  <div class="pillar-col pillar-katas">
                    <div class="pillar-head">
                      <span class="pillar-tag katas">🥋 Katas Topics</span>
                      <span class="pillar-time">45m</span>
                    </div>
                    <ul class="pillar-list">
                      ${katasList.map(k => `<li class="pillar-item"><span class="pillar-marker katas">⚡</span><span>${k}</span></li>`).join('')}
                    </ul>
                    <div class="kata-preview-chip">
                      <span class="kata-chip-label">Daily Challenge:</span>
                      <span class="kata-chip-name">${challenge.title}</span>
                      <span class="kata-chip-diff ${challenge.difficulty.toLowerCase()}">${challenge.difficulty}</span>
                    </div>
                  </div>
                </div>

                <div class="sprint-actions">
                  <button class="inspect-btn" id="inspectBtn-${item.day}" onclick="toggleDrawer(${item.day})">
                    Inspect Sprint Specs ↓
                  </button>
                  <button class="copy-path-btn" onclick="copyToClipboard('${item.deliverable}', this)">
                    Copy Deliverable Path
                  </button>
                </div>
              </div>
            </div>

            <div class="sprint-right">
              <select class="state-dropdown" onchange="changeSprintStatus(${item.day}, this)">
                <option value="todo" ${status === 'todo' ? 'selected' : ''}>To Do</option>
                <option value="in-progress" ${status === 'in-progress' ? 'selected' : ''}>In Progress</option>
                <option value="completed" ${status === 'completed' ? 'selected' : ''}>Verified</option>
              </select>
            </div>
          </div>

          <div class="inspection-drawer" id="drawer-${item.day}">
            <!-- Panel 1: Theory Syllabus -->
            <div class="panel-block">
              <div class="panel-title theory-title">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                Theory Curriculum & Knowledge Checkpoints (1.0 Hour)
              </div>
              <div class="panel-body">
                <div class="theory-grid">
                  ${theoryList.map(t => `
                    <div class="theory-card">
                      <div class="theory-check">✓</div>
                      <div class="theory-text">${t}</div>
                    </div>
                  `).join('')}
                </div>
              </div>
            </div>

            <!-- Panel 2: Coding Lab -->
            <div class="panel-block">
              <div class="panel-title">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                Hands-On Engineering Assignment (2.5 Hours)
              </div>
              <div class="panel-body">
                <p style="margin-bottom:10px; color:var(--text); line-height:1.5;">${item.assignment}</p>
                <div class="coding-checklist">
                  <strong style="font-size:0.73rem; color:var(--cyan); text-transform:uppercase; letter-spacing:0.04em; font-family:'JetBrains Mono', monospace;">Implementation Tasks:</strong>
                  <div class="coding-tags">
                    ${codingList.map(c => `<span class="code-topic-tag">${c}</span>`).join('')}
                  </div>
                </div>
                <div class="deliverable-banner">
                  <span class="code-chip">${item.deliverable}</span>
                  <button class="copy-path-btn" onclick="copyToClipboard('${item.deliverable}', this)">Copy Path</button>
                  <button class="copy-path-btn" onclick="copyToClipboard('pytest ${item.deliverable} -v', this)">Copy Pytest Command</button>
                </div>
              </div>
            </div>

            <!-- Panel 3: Katas Arena -->
            <div class="panel-block">
              <div class="panel-title katas-title">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                Focused Katas Arena & LeetCode Drill (30–45 Mins)
              </div>
              <div class="panel-body">
                <div class="kata-challenge-box">
                  <div class="kata-challenge-head">
                    <span class="kata-title-highlight">${challenge.title}</span>
                    <span class="kata-chip-diff ${challenge.difficulty.toLowerCase()}">${challenge.difficulty}</span>
                    <span class="kata-pattern-tag">Pattern: ${challenge.pattern}</span>
                  </div>
                  <p class="kata-desc">${challenge.description}</p>
                  <div class="kata-practice-topics">
                    <span class="kata-subhead">Daily Kata Topics:</span>
                    ${katasList.map(k => `<span class="kata-topic-pill">${k}</span>`).join('')}
                  </div>
                  <button class="reveal-trigger kata-hint-btn" id="kataHintBtn-${item.day}" onclick="toggleKataHint(${item.day})">
                    Reveal Solution Approach & Hint
                  </button>
                  <div class="answer-vault kata-vault" id="kataVault-${item.day}">
                    <strong>Algorithmic Strategy:</strong> ${challenge.hint}
                  </div>
                </div>
              </div>
            </div>

            <!-- Panel 4: ₹20 LPA Technical Inspection Challenge -->
            <div class="panel-block">
              <div class="panel-title interview">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                ₹20 LPA Technical Inspection Challenge
              </div>
              <div class="panel-body"><span class="q-stem">Q:</span> ${item.interviewQ}</div>
              <button class="reveal-trigger" id="revealTrigger-${item.day}" onclick="toggleAnswer(${item.day})">Reveal Technical Rationale</button>
              <div class="answer-vault" id="answerVault-${item.day}">
                <strong>Engine Answer:</strong> ${item.interviewAns}
              </div>
            </div>

            <!-- Panel 5: Sprint Notes & Pull Request URL -->
            <div class="panel-block">
              <div class="panel-title notes">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
                Sprint Notes & Pull Request URL
              </div>
              <div style="display:flex; flex-direction:column; gap:6px;">
                <input type="text" class="input-row mono" placeholder="Pull Request / Commit URL (https://github.com/...)" value="${current.link || ''}" onchange="saveLink(${item.day}, this.value)">
                <textarea class="input-row" rows="2" placeholder="Record edge cases debugged, gotchas, or takeaways..." onchange="saveNotes(${item.day}, this.value)">${current.notes || ''}</textarea>
                <div class="persisted-badge" id="saveBadge-${item.day}">✓ Persisted to local storage</div>
              </div>
            </div>
          </div>
        `;

        container.appendChild(card);
      });

      if (count === 0) {
        container.innerHTML = `
          <div style="text-align:center; padding:48px 16px; background:var(--surface); border-radius:8px; border:1px solid var(--border);">
            <div style="font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:var(--text-dim); text-transform:uppercase;">Zero Sprints Found</div>
            <p style="font-size:0.9rem; color:var(--text-muted); margin-top:4px;">No sprints matched your active search or phase filter.</p>
          </div>
        `;
      }

      updateCockpitUI();
    }

    function updateCockpitUI() {
      let done = 0;
      let run = 0;
      let todo = 0;
      let nextSprint = null;
      let totalTheory = 0;
      let totalKatas = 0;

      RAW_DAYS.forEach(d => {
        totalTheory += (d.theory_topics ? d.theory_topics.length : 4);
        totalKatas += (d.katas_topics ? d.katas_topics.length : 2);
        const s = (state.entries[d.day] && state.entries[d.day].status) || "todo";
        if (s === "completed") done++;
        else if (s === "in-progress") {
          run++;
          if (!nextSprint) nextSprint = d;
        } else {
          todo++;
          if (!nextSprint) nextSprint = d;
        }
      });

      const total = RAW_DAYS.length;
      const pct = Math.round((done / total) * 100);

      document.getElementById("gaugePct").innerText = pct + "%";
      document.getElementById("gaugeBar").style.width = pct + "%";
      document.getElementById("gaugeRatio").innerText = `${done} of ${total} Sprints Verified`;
      document.getElementById("valRemaining").innerText = total - done;

      const hrs = (done * 4.8).toFixed(1);
      document.getElementById("valHours").innerText = hrs + " hrs";
      document.getElementById("valStreak").innerText = done + " Days";

      if (document.getElementById("valTheory")) {
        document.getElementById("valTheory").innerText = totalTheory;
      }
      if (document.getElementById("valKatas")) {
        document.getElementById("valKatas").innerText = totalKatas;
      }

      document.getElementById("cAll").innerText = total;
      document.getElementById("cPass").innerText = done;
      document.getElementById("cRun").innerText = run;
      document.getElementById("cTodo").innerText = todo;

      const r2Done = state.entries[40] && state.entries[40].status === "completed";
      const r1Done = state.entries[56] && state.entries[56].status === "completed";
      const r3Done = state.entries[77] && state.entries[77].status === "completed";

      let repoCount = 0;
      if (r2Done) repoCount++;
      if (r1Done) repoCount++;
      if (r3Done) repoCount++;
      document.getElementById("valRepos").innerText = `${repoCount} / 3`;

      // Update Next Up Banner
      if (nextSprint) {
        document.getElementById("nextSprintTitle").innerText = `Day ${nextSprint.day.toString().padStart(2, '0')}: ${nextSprint.title}`;
        document.getElementById("nextSprintDesc").innerText = `${nextSprint.category} • Deliverable: ${nextSprint.deliverable}`;
        document.getElementById("nextUpBanner").style.display = "flex";
      } else {
        document.getElementById("nextSprintTitle").innerText = "All 90 Sprints Verified! Ready for 20 LPA Applications.";
        document.getElementById("nextSprintDesc").innerText = "Portfolio complete with 3 flagship repositories and 90 verified competencies.";
      }
    }

    function exportData() {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(state, null, 2));
      const a = document.createElement("a");
      a.setAttribute("href", dataStr);
      a.setAttribute("download", `sdet_cockpit_backup_${new Date().toISOString().slice(0,10)}.json`);
      document.body.appendChild(a);
      a.click();
      a.remove();
    }

    function triggerRestore() { document.getElementById("restoreInput").click(); }

    function handleRestore(e) {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(evt) {
        try {
          const parsed = JSON.parse(evt.target.result);
          if (parsed.entries) {
            state.entries = parsed.entries;
            persistState();
            renderFeed();
            renderMatrix();
            alert("Cockpit state successfully restored.");
          }
        } catch(err) {
          alert("Error parsing backup JSON file: " + err);
        }
      };
      reader.readAsText(file);
    }

    function openVault() { document.getElementById("codeVaultModal").classList.add("open"); }
    function closeVault() { document.getElementById("codeVaultModal").classList.remove("open"); }

    function openExposeModal() { document.getElementById("exposeModal").classList.add("open"); }
    function closeExposeModal() { document.getElementById("exposeModal").classList.remove("open"); }

    function openGatesModal() { document.getElementById("gatesModal").classList.add("open"); }
    function closeGatesModal() { document.getElementById("gatesModal").classList.remove("open"); }

    function openReposModal() { document.getElementById("reposModal").classList.add("open"); }
    function closeReposModal() { document.getElementById("reposModal").classList.remove("open"); }

    function openDrillsModal() { document.getElementById("drillsModal").classList.add("open"); }
    function closeDrillsModal() { document.getElementById("drillsModal").classList.remove("open"); }

    /* Web Audio API Synthesized Chime (Zero External Files) */
    function playChime() {
      try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = "sine";
        osc.frequency.setValueAtTime(587.33, audioCtx.currentTime); // D5
        osc.frequency.exponentialRampToValueAtTime(880.00, audioCtx.currentTime + 0.3); // A5
        gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.8);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.8);
      } catch(e) {
        console.log("Audio alert skipped", e);
      }
    }

    /* 6-Hour Persistent Cockpit Focus Stopwatch */
    const FOCUS_HOURS_SECS = Math.round(4.5 * 3600); // 16,200 seconds (4.5h protocol)
    const TIMER_STORAGE_KEY = "sdet_cockpit_timer_v2";
    let timerSecs = FOCUS_HOURS_SECS;
    let timerTargetEndTime = null;
    let timerInterval = null;
    let timerRunning = false;

    function formatTime(s) {
      const h = Math.floor(s / 3600).toString().padStart(2, '0');
      const m = Math.floor((s % 3600) / 60).toString().padStart(2, '0');
      const sc = (s % 60).toString().padStart(2, '0');
      return `${h}:${m}:${sc}`;
    }

    function saveTimerState() {
      try {
        localStorage.setItem(TIMER_STORAGE_KEY, JSON.stringify({
          isRunning: timerRunning,
          targetEndTime: timerTargetEndTime,
          remainingSecs: timerSecs
        }));
      } catch (e) {
        console.error("Timer state save failed", e);
      }
    }

    function initTimer() {
      const saved = localStorage.getItem(TIMER_STORAGE_KEY);
      const btn = document.getElementById("timerStartBtn");
      const display = document.getElementById("timerDisplay");

      if (saved) {
        try {
          const data = JSON.parse(saved);
          if (data.isRunning && data.targetEndTime) {
            const now = Date.now();
            const diff = Math.max(0, Math.round((data.targetEndTime - now) / 1000));
            if (diff > 0) {
              timerSecs = diff;
              timerTargetEndTime = data.targetEndTime;
              display.innerText = formatTime(timerSecs);
              startTicking();
              return;
            } else {
              timerSecs = 0;
              timerRunning = false;
              display.innerText = formatTime(0);
              if (btn) btn.innerText = "Start 4.5h";
              localStorage.removeItem(TIMER_STORAGE_KEY);
              return;
            }
          } else if (data.remainingSecs !== undefined) {
            timerSecs = Math.max(0, data.remainingSecs);
            display.innerText = formatTime(timerSecs);
            if (btn) {
              btn.innerText = (timerSecs < FOCUS_HOURS_SECS && timerSecs > 0) ? "Resume 6h" : "Start 4.5h";
            }
            return;
          }
        } catch(e) {
          console.error("Timer init parse error", e);
        }
      }
      display.innerText = formatTime(FOCUS_HOURS_SECS);
      if (btn) btn.innerText = "Start 4.5h";
    }

    function startTicking() {
      const btn = document.getElementById("timerStartBtn");
      const display = document.getElementById("timerDisplay");
      timerRunning = true;
      if (btn) btn.innerText = "Pause";

      if (timerInterval) clearInterval(timerInterval);

      timerInterval = setInterval(() => {
        if (!timerTargetEndTime) return;
        const now = Date.now();
        const diff = Math.max(0, Math.round((timerTargetEndTime - now) / 1000));
        timerSecs = diff;
        if (display) display.innerText = formatTime(timerSecs);

        if (timerSecs <= 0) {
          clearInterval(timerInterval);
          timerRunning = false;
          timerTargetEndTime = null;
          if (btn) btn.innerText = "Start 4.5h";
          localStorage.removeItem(TIMER_STORAGE_KEY);
          playChime();
          alert("6-Hour daily focus protocol complete! Exceptional dedication. Take time to rest and recharge.");
          resetTimer();
        }
      }, 1000);
    }

    function toggleTimer() {
      const btn = document.getElementById("timerStartBtn");
      if (timerRunning) {
        clearInterval(timerInterval);
        timerRunning = false;
        if (timerTargetEndTime) {
          timerSecs = Math.max(0, Math.round((timerTargetEndTime - Date.now()) / 1000));
        }
        timerTargetEndTime = null;
        if (btn) btn.innerText = "Resume 6h";
        saveTimerState();
      } else {
        if (timerSecs <= 0) {
          timerSecs = FOCUS_HOURS_SECS;
        }
        timerTargetEndTime = Date.now() + (timerSecs * 1000);
        startTicking();
        saveTimerState();
      }
    }

    function resetTimer() {
      if (timerInterval) clearInterval(timerInterval);
      timerRunning = false;
      timerTargetEndTime = null;
      timerSecs = FOCUS_HOURS_SECS;
      localStorage.removeItem(TIMER_STORAGE_KEY);
      const display = document.getElementById("timerDisplay");
      const btn = document.getElementById("timerStartBtn");
      if (display) display.innerText = formatTime(FOCUS_HOURS_SECS);
      if (btn) btn.innerText = "Start 4.5h";
    }

    window.onclick = function(e) {
      ["codeVaultModal", "exposeModal", "gatesModal", "reposModal", "drillsModal"].forEach(id => {
        const modal = document.getElementById(id);
        if (modal && e.target === modal) modal.classList.remove("open");
      });
    };

    window.addEventListener("DOMContentLoaded", () => {
      loadState();
      renderMatrix();
      renderFeed();
      initTimer();
    });
  </script>
</body>
</html>
'''

final_html = html_content.replace("__DAYS_DATA_PLACEHOLDER__", days_json)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Updated index.html: highly engaging and functional Cockpit UI created.")
