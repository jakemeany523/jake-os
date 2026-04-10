#!/usr/bin/env python3
"""Query tool for quality-scores.jsonl.

Usage:
    python3 scripts/quality_log.py --rubric social-post --since 7d --by dimension
    python3 scripts/quality_log.py --rubric mandamus-linkedin --since 30d --bias-check
    python3 scripts/quality_log.py --summary
    python3 scripts/quality_log.py --rubric social-post --weekly-digest

Requires: pandas (pip install pandas --break-system-packages)
"""

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("pandas required: pip install pandas --break-system-packages")
    sys.exit(1)

LOG_PATH = Path(__file__).resolve().parent.parent / "memory" / "evolving" / "quality-scores.jsonl"


def load_log(path: Path = LOG_PATH) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        print(f"No data at {path}")
        sys.exit(0)
    rows = []
    for line in path.read_text().strip().splitlines():
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    if not rows:
        print("Log is empty or unparseable.")
        sys.exit(0)
    df = pd.DataFrame(rows)
    df["ts"] = pd.to_datetime(df["ts"], utc=True)
    return df


def filter_since(df: pd.DataFrame, since_str: str) -> pd.DataFrame:
    num = int(since_str[:-1])
    unit = since_str[-1]
    delta = {"d": timedelta(days=num), "w": timedelta(weeks=num), "h": timedelta(hours=num)}.get(unit)
    if not delta:
        print(f"Invalid --since unit: {unit}. Use d/w/h.")
        sys.exit(1)
    cutoff = datetime.now(timezone.utc) - delta
    return df[df["ts"] >= cutoff]


def by_dimension(df: pd.DataFrame, rubric: str):
    sub = df[df["rubric"] == rubric].copy()
    if sub.empty:
        print(f"No entries for rubric '{rubric}'.")
        return
    # Expand scores dict into columns
    scores_df = pd.json_normalize(sub["scores"])
    dims = scores_df.columns.tolist()
    print(f"\n{'Dimension':<25} {'Mean':>6} {'Min':>6} {'Max':>6} {'Count':>6}")
    print("-" * 55)
    for dim in sorted(dims):
        col = pd.to_numeric(scores_df[dim], errors="coerce").dropna()
        if col.empty:
            continue
        print(f"{dim:<25} {col.mean():>6.1f} {col.min():>6.1f} {col.max():>6.1f} {len(col):>6}")
    avg_series = pd.to_numeric(sub["avg"], errors="coerce").dropna()
    print(f"\n{'Overall avg':<25} {avg_series.mean():>6.1f}")
    print(f"{'Entries':<25} {len(sub):>6}")


def bias_check(df: pd.DataFrame, rubric: str):
    """Compare model-scored iterations vs human-override iterations."""
    sub = df[df["rubric"] == rubric].copy()
    model = sub[sub["iteration"] != "human"]
    human = sub[sub["iteration"] == "human"]
    if human.empty:
        print(f"No human-override entries for '{rubric}' yet. Need more data.")
        return
    model_avg = pd.to_numeric(model["avg"], errors="coerce").mean()
    human_avg = pd.to_numeric(human["avg"], errors="coerce").mean()
    gap = model_avg - human_avg
    print(f"\nSelf-grading bias check for '{rubric}':")
    print(f"  Model avg:  {model_avg:.2f} ({len(model)} entries)")
    print(f"  Human avg:  {human_avg:.2f} ({len(human)} entries)")
    print(f"  Gap:        {gap:+.2f}")
    if abs(gap) > 1.5:
        print("  WARNING: Gap > 1.5. Judge may be inflating. Retune rubric anchors.")
    else:
        print("  OK: Gap within acceptable range.")


def weekly_digest(df: pd.DataFrame, rubric: str = None):
    """Per-rubric weekly avg + trend."""
    df = df.copy()
    df["week"] = df["ts"].dt.isocalendar().week.astype(int)
    df["year"] = df["ts"].dt.year
    rubrics = [rubric] if rubric else df["rubric"].unique().tolist()
    for r in rubrics:
        sub = df[df["rubric"] == r].copy()
        if sub.empty:
            continue
        sub["avg_num"] = pd.to_numeric(sub["avg"], errors="coerce")
        grouped = sub.groupby(["year", "week"])["avg_num"].mean()
        print(f"\n--- {r} ---")
        for (y, w), avg in grouped.items():
            print(f"  {y}-W{w:02d}: {avg:.1f}")
        if len(grouped) >= 2:
            vals = list(grouped.values)
            delta = vals[-1] - vals[-2]
            print(f"  Trend: {delta:+.1f}")
        # Find weakest dimension
        scores_df = pd.json_normalize(sub["scores"])
        dim_means = {}
        for col in scores_df.columns:
            s = pd.to_numeric(scores_df[col], errors="coerce").dropna()
            if not s.empty:
                dim_means[col] = s.mean()
        if dim_means:
            weakest = min(dim_means, key=dim_means.get)
            print(f"  Weakest: {weakest} ({dim_means[weakest]:.1f})")


def summary(df: pd.DataFrame):
    print(f"\nTotal entries: {len(df)}")
    print(f"Rubrics: {', '.join(df['rubric'].unique())}")
    print(f"Date range: {df['ts'].min()} to {df['ts'].max()}")
    human_count = len(df[df["iteration"] == "human"])
    print(f"Human-override entries: {human_count}")
    for r in df["rubric"].unique():
        avg = pd.to_numeric(df[df["rubric"] == r]["avg"], errors="coerce").mean()
        count = len(df[df["rubric"] == r])
        print(f"  {r}: avg {avg:.1f} ({count} entries)")


def main():
    parser = argparse.ArgumentParser(description="Query quality-scores.jsonl")
    parser.add_argument("--rubric", help="Filter by rubric name")
    parser.add_argument("--since", help="Time window (e.g. 7d, 4w, 24h)")
    parser.add_argument("--by", choices=["dimension"], help="Group output by dimension")
    parser.add_argument("--bias-check", action="store_true", help="Compare model vs human scores")
    parser.add_argument("--weekly-digest", action="store_true", help="Per-week avg + trend")
    parser.add_argument("--summary", action="store_true", help="Overall summary")
    parser.add_argument("--log", type=str, default=str(LOG_PATH), help="Path to JSONL log")
    args = parser.parse_args()

    df = load_log(Path(args.log))

    if args.since:
        df = filter_since(df, args.since)

    if args.summary:
        summary(df)
    elif args.bias_check and args.rubric:
        bias_check(df, args.rubric)
    elif args.weekly_digest:
        weekly_digest(df, args.rubric)
    elif args.by == "dimension" and args.rubric:
        by_dimension(df, args.rubric)
    elif args.rubric:
        by_dimension(df, args.rubric)
    else:
        summary(df)


if __name__ == "__main__":
    main()
