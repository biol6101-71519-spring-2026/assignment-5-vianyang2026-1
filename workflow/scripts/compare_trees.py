#!/usr/bin/env python3
"""
Calculate Robinson-Foulds distances between all tree pairs and summarize
topological concordance between gene trees and species trees.
"""

import argparse
import itertools
import dendropy
from dendropy.calculate import treecompare


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gene-trees",       nargs="+", required=True)
    parser.add_argument("--coalescent-tree",  required=True)
    parser.add_argument("--concat-tree",      required=True)
    parser.add_argument("--genes",            required=True, help="Comma-separated gene names")
    parser.add_argument("--rf-output",        required=True)
    parser.add_argument("--topo-output",      required=True)
    parser.add_argument("--concordance-output", required=True)
    return parser.parse_args()


def load_tree(path, tns):
    return dendropy.Tree.get(
        path=path,
        schema="newick",
        taxon_namespace=tns,
        preserve_underscores=True,
    )


def rf(t1, t2):
    return treecompare.symmetric_difference(t1, t2)


def main():
    args  = parse_args()
    genes = args.genes.split(",")
    tns   = dendropy.TaxonNamespace()

    gene_trees = {
        gene: load_tree(path, tns)
        for gene, path in zip(genes, args.gene_trees)
    }
    coalescent = load_tree(args.coalescent_tree, tns)
    concat     = load_tree(args.concat_tree, tns)

    all_trees = list(gene_trees.items()) + [
        ("coalescent", coalescent),
        ("supermatrix", concat),
    ]

    # ------------------------------------------------------------------
    # Robinson-Foulds distances between every pair
    # ------------------------------------------------------------------
    with open(args.rf_output, "w") as out:
        out.write("Tree_1\tTree_2\tRF_Distance\n")
        for (n1, t1), (n2, t2) in itertools.combinations(all_trees, 2):
            try:
                dist = rf(t1, t2)
                out.write(f"{n1}\t{n2}\t{dist}\n")
            except Exception as e:
                out.write(f"{n1}\t{n2}\tERROR:{e}\n")
    print(f"RF distances -> {args.rf_output}")

    # ------------------------------------------------------------------
    # Topological summary
    # ------------------------------------------------------------------
    with open(args.topo_output, "w") as out:
        out.write("Topological Summary\n")
        out.write("=" * 60 + "\n\n")

        rf_cc = rf(coalescent, concat)
        out.write(f"RF distance (coalescent vs supermatrix): {rf_cc}\n\n")

        out.write("Gene trees vs species trees:\n")
        out.write(f"{'Gene':<15} {'vs_Coalescent':>15} {'vs_Supermatrix':>15}\n")
        out.write("-" * 46 + "\n")
        for gene, tree in gene_trees.items():
            try:
                rc = rf(tree, coalescent)
                rs = rf(tree, concat)
                out.write(f"{gene:<15} {rc:>15} {rs:>15}\n")
            except Exception:
                out.write(f"{gene:<15} {'ERROR':>15} {'ERROR':>15}\n")
    print(f"Topological summary -> {args.topo_output}")

    # ------------------------------------------------------------------
    # Concordance analysis
    # ------------------------------------------------------------------
    with open(args.concordance_output, "w") as out:
        out.write("Gene Tree Concordance Analysis\n")
        out.write("=" * 60 + "\n\n")

        n = len(gene_trees)

        rf_to_coal   = []
        rf_to_concat = []
        for tree in gene_trees.values():
            try:
                rf_to_coal.append(rf(tree, coalescent))
                rf_to_concat.append(rf(tree, concat))
            except Exception:
                rf_to_coal.append(None)
                rf_to_concat.append(None)

        valid_coal   = [x for x in rf_to_coal   if x is not None]
        valid_concat = [x for x in rf_to_concat if x is not None]

        conc_coal   = sum(1 for x in valid_coal   if x == 0)
        conc_concat = sum(1 for x in valid_concat if x == 0)

        out.write(f"Total genes: {n}\n")
        out.write(f"Concordant with coalescent tree:  {conc_coal}/{n}\n")
        out.write(f"Concordant with supermatrix tree: {conc_concat}/{n}\n\n")

        if valid_coal:
            out.write(f"Mean RF to coalescent:  {sum(valid_coal)/len(valid_coal):.2f}\n")
        if valid_concat:
            out.write(f"Mean RF to supermatrix: {sum(valid_concat)/len(valid_concat):.2f}\n\n")

        out.write(f"{'Gene':<15} {'RF_to_Coalescent':>18} {'RF_to_Supermatrix':>18}\n")
        out.write("-" * 52 + "\n")
        for gene, rc, rs in zip(genes, rf_to_coal, rf_to_concat):
            out.write(f"{gene:<15} {str(rc):>18} {str(rs):>18}\n")

    print(f"Concordance analysis -> {args.concordance_output}")


if __name__ == "__main__":
    main()
