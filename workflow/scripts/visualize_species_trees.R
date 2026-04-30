#!/usr/bin/env Rscript
# Visualize coalescent and supermatrix species trees, then plot them side-by-side.

suppressPackageStartupMessages({
  library(optparse)
  library(ape)
  library(ggtree)
  library(ggplot2)
  library(treeio)
  library(gridExtra)
})

option_list <- list(
  make_option("--coalescent",        type = "character", help = "Coalescent tree (Newick)"),
  make_option("--concat",            type = "character", help = "Supermatrix tree (Newick)"),
  make_option("--coalescent-output", type = "character", help = "Coalescent tree PDF"),
  make_option("--concat-output",     type = "character", help = "Supermatrix tree PDF"),
  make_option("--comparison-output", type = "character", help = "Side-by-side comparison PDF")
)
opts <- parse_args(OptionParser(option_list = option_list))

coal_tree <- read.newick(opts$coalescent)
conc_tree <- read.newick(opts$concat)

plot_tree <- function(tree, title) {
  max_x <- max(fortify(tree)$x, na.rm = TRUE)
  ggtree(tree) +
    geom_tiplab(size = 3, hjust = -0.05) +
    geom_nodelab(aes(label = label), size = 2.5, hjust = 1.2,
                 vjust = -0.4, color = "firebrick") +
    geom_treescale(x = 0, y = -1, fontsize = 3) +
    ggtitle(title) +
    theme_tree2() +
    xlim(0, max_x * 1.35)
}

p_coal <- plot_tree(coal_tree, "Coalescent Species Tree (ASTRAL)")
p_conc <- plot_tree(conc_tree, "Supermatrix Tree (IQ-TREE)")

ggsave(opts$`coalescent-output`, p_coal, width = 8, height = 6)
cat("Saved:", opts$`coalescent-output`, "\n")

ggsave(opts$`concat-output`, p_conc, width = 8, height = 6)
cat("Saved:", opts$`concat-output`, "\n")

pdf(opts$`comparison-output`, width = 16, height = 6)
grid.arrange(p_coal, p_conc, ncol = 2)
dev.off()
cat("Saved:", opts$`comparison-output`, "\n")
