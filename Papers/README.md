This folder holds all the papers we should look into.

We should go over these papers and the tools they use from the following perspectives:
•	Can they be used to describe splicing diversity at the molecular level (i.e. using the actual sequence or actual splicing events as input, and not full isoforms).
•	What tools are they using and what are the shortcomings.
•	How can our strategies be better.

Martin thinks that the molecular level is the starting point- afterward, we can think about how to apply that to the level of the transcripts and how we can there be better than the existing tools.


The number before each paper is for us, to keep track of what we already covered.
The following is from Splicing Factory Article, Introduction, page 1:
 
1 – (Ritchie et al., 2008) –  One of the first papers in this area used Shannon-entropy to characterize splicing variance, investigating cDNA and cDNA tag libraries in 27 cancer types (Ritchie et al., 2008). In half of the cancers studied, they described a significant entropy gain compared to normal tissue.

2 – (Zambelli et al., 2018) – The RNentropy tool calculates Shannon-entropy for genes across samples to detect differential expression between any number of conditions (Zambelli et al., 2018).

3 – (Sterne-Weiler et al., 2018) – Whippet uses Shannon-entropy to detect and quantify complex alternative splicing events (Sterne-Weiler et al., 2018) and the authors describe that complex, high-entropy splicing events are conserved, tissue-regulated and more prevalent in various cancer types.

4 – (Kim et al., 2019) – SpliceHetero aims to characterize spliceomic intratumor heterogeneity (sITH) from bulk tumor RNA-sequencing (Kim et al., 2019). The authors used the Jensen–Shannon Divergence to characterize splice site usage differences between samples and found that increased sITH was correlated with cancer progression and worse survival.

5 – (Afsari et al., 2018) – The Splice Expression Variation Analysis (SEVA) tool aims to model increased heterogeneity of splicing variants in cancer, using a rank-based multivariate statistics, comparing splice junction expression profiles between conditions (Afsari et al., 2018).

6 – (Monlong et al., 2014) – Finally, the sQTLseekeR R package analyzes associations between genotype information and transcript relative expression. Even though the main goal of sQTLseekeR is to detect splicing quantitative trait loci (sQTLs), it can also detect splicing variance QTLs (svQTLs) (Monlong et al., 2014), where changes in splicing isoform diversity are associated to a genotype."
