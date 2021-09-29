<a name="z1swR"></a>
### 1、解释1.gtf文件中第4、5列代表什么，exon长度应该是$5-$4+1还是$5-$4？
答：1.gtf文件中第4、5列表示该基因或转录本在参考序列上的起始和终止位置。exon长度应该是$5-$4+1。<br />​<br />
<a name="iu2Kp"></a>
### 2、列出1.gtf文件中 XI 号染色体上的后 10 个 CDS （按照每个CDS终止位置的基因组坐标进行sort）。
<a name="F2HdS"></a>
### 3、统计 IV 号染色体上各类 feature （1.gtf文件的第3列，有些注释文件中还应同时考虑第2列） 的数目，并按升序排列。
答：两题均是使用Python3代码解答，因此合并作答。代码如下：
```python
fo1=open('1.gtf','r')
fo1all=fo1.readlines()
fo1.close()
dict_XI_CDS_end={}
list_IV_feature=[]
dict_IV_feature_num={}
for afo1all,xfo1all in enumerate(fo1all):
	if xfo1all.startswith('#')==0:
		content_list=xfo1all.strip().split('\t')
		if content_list[0]=='XI' and content_list[2]=='CDS':
			dict_XI_CDS_end[xfo1all.strip()]=content_list[4]
		if content_list[0]=='IV':
			list_IV_feature.append(content_list[2])
sorted_CDS=sorted(dict_XI_CDS_end.items(),key=lambda x:x[1],reverse=True)
for i1 in range(10):
	print(sorted_CDS[i1][0])
feature_class=set(list_IV_feature)
for i1 in feature_class:
	dict_IV_feature_num[i1]=list_IV_feature.count(i1)
print(sorted(dict_IV_feature_num.items(),key=lambda x:x[1]))
```
第二题答案如下：
```
XI	ensembl	CDS	98721	99638	.	+	0	gene_id "YKL183W"; gene_version "1"; transcript_id "YKL183W"; transcript_version "1"; exon_number "1"; gene_name "LOT5"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "LOT5"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKL183W"; protein_version "1";
XI	ensembl	CDS	98398	98607	.	-	0	gene_id "YKL183C-A"; gene_version "1"; transcript_id "YKL183C-A"; transcript_version "1"; exon_number "1"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "YKL183C-A"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKL183C-A"; protein_version "1";
XI	ensembl	CDS	96757	98154	.	+	0	gene_id "YKL184W"; gene_version "1"; transcript_id "YKL184W"; transcript_version "1"; exon_number "1"; gene_name "SPE1"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "SPE1"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKL184W"; protein_version "1";
XI	ensembl	CDS	94499	96262	.	+	0	gene_id "YKL185W"; gene_version "1"; transcript_id "YKL185W"; transcript_version "1"; exon_number "1"; gene_name "ASH1"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "ASH1"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKL185W"; protein_version "1";
XI	ensembl	CDS	92747	93298	.	-	0	gene_id "YKL186C"; gene_version "1"; transcript_id "YKL186C"; transcript_version "1"; exon_number "1"; gene_name "MTR2"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "MTR2"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKL186C"; protein_version "1";
XI	ensembl	CDS	89287	91536	.	-	0	gene_id "YKL187C"; gene_version "1"; transcript_id "YKL187C"; transcript_version "1"; exon_number "1"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "YKL187C"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKL187C"; protein_version "1";
XI	ensembl	CDS	86228	88786	.	-	0	gene_id "YKL188C"; gene_version "1"; transcript_id "YKL188C"; transcript_version "1"; exon_number "1"; gene_name "PXA2"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "PXA2"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKL188C"; protein_version "1";
XI	ensembl	CDS	84704	85900	.	+	0	gene_id "YKL189W"; gene_version "1"; transcript_id "YKL189W"; transcript_version "1"; exon_number "1"; gene_name "HYM1"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "HYM1"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKL189W"; protein_version "1";
XI	ensembl	CDS	83075	83547	.	+	1	gene_id "YKL190W"; gene_version "1"; transcript_id "YKL190W"; transcript_version "1"; exon_number "2"; gene_name "CNB1"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "CNB1"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKL190W"; protein_version "1";
XI	ensembl	CDS	82947	82998	.	+	0	gene_id "YKL190W"; gene_version "1"; transcript_id "YKL190W"; transcript_version "1"; exon_number "1"; gene_name "CNB1"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "CNB1"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKL190W"; protein_version "1";
```

<br />第三题答案如下：
```
[('stop_codon', 853), ('start_codon', 853), ('gene', 886), ('transcript', 886), ('CDS', 895), ('exon', 933)]
```
​<br />
