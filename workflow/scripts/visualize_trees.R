#!/usr/bin/env Rscript
# Visualize a single phylogenetic tree with bootstrap support values.

suppressPackageStartupMessages({
  library(optparse)
  library(ape)
  library(ggtree)
  library(ggplot2)
  library(treeio)
})

option_list <- list(
  make_option("--tree",   type = "character", help = "Newick tree file"),
  make_option("--output", type = "character", help = "Output PDF path"),
  make_option("--title",  type = "character", default = "Phylogenetic Tree",
              help = "Plot title")
)
opts <- parse_args(OptionParser(option_list = option_list))

tree <- read.newick(opts$tree)

max_x <- max(fortify(tree)$x, na.rm = TRUE)

p <- ggtree(tree) +
  geom_tiplab(size = 3, hjust = -0.05) +
  geom_nodelab(aes(label = label), size = 2.5, hjust = 1.2,
               vjust = -0.4, color = "firebrick") +
  geom_treescale(x = 0, y = -1, fontsize = 3) +
  ggtitle(opts$title) +
  theme_tree2() +
  xlim(0, max_x * 1.35)

ggsave(opts$output, p, width = 8, height = 6)
cat("Saved:", opts$output, "\n")
