#!/usr/bin/env python3
"""Generate an HTML phylogenetic analysis report from workflow outputs."""

import argparse
import datetime


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rf-distances",    required=True)
    parser.add_argument("--topo-summary",    required=True)
    parser.add_argument("--concordance",     required=True)
    parser.add_argument("--models",          required=True)
    parser.add_argument("--alignment-report", required=True)
    parser.add_argument("--genes",           required=True, help="Comma-separated")
    parser.add_argument("--output",          required=True)
    return parser.parse_args()


def read_file(path):
    with open(path) as f:
        return f.read()


def main():
    args  = parse_args()
    genes = args.genes.split(",")

    sections = {
        "Alignment Summary":          read_file(args.alignment_report),
        "Evolutionary Model Selection": read_file(args.models),
        "Robinson-Foulds Distances":  read_file(args.rf_distances),
        "Topological Summary":        read_file(args.topo_summary),
        "Concordance Analysis":       read_file(args.concordance),
    }

    section_html = "\n".join(
        f"""  <div class="section">
    <h2>{title}</h2>
    <pre>{content}</pre>
  </div>"""
        for title, content in sections.items()
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Phylogenetic Analysis Report</title>
  <style>
    body  {{ font-family: Arial, sans-serif; max-width: 1000px; margin: 40px auto; padding: 0 20px; }}
    h1    {{ color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 6px; }}
    h2    {{ color: #34495e; border-bottom: 1px solid #bdc3c7; padding-bottom: 4px; }}
    pre   {{ background: #f4f4f4; padding: 15px; border-radius: 5px;
             overflow-x: auto; font-size: 13px; line-height: 1.4; }}
    .meta {{ color: #7f8c8d; font-size: 13px; margin-bottom: 30px; }}
    .section {{ margin-bottom: 35px; }}
  </style>
</head>
<body>
  <h1>Phylogenetic Analysis Report</h1>
  <p class="meta">
    Generated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}<br>
    Genes analyzed: {", ".join(genes)}
  </p>

{section_html}

  <div class="section">
    <h2>Discussion</h2>
    <p>Tree visualizations are in <code>results/visualizations/</code>.
    Compare the Robinson-Foulds distances and concordance values above to
    assess whether the coalescent (ASTRAL) or supermatrix (IQ-TREE) approach
    better represents the evolutionary history of your dataset.
    High discordance among gene trees may indicate incomplete lineage sorting,
    supporting the coalescent approach.</p>
  </div>
</body>
</html>
"""

    with open(args.output, "w") as f:
        f.write(html)

    print(f"Report written to {args.output}")


if __name__ == "__main__":
    main()
