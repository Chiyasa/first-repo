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

