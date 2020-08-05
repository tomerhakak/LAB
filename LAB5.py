dict_names={"dudu":25000,"avi":30000,"omer":7600,"tomer":5000,"meir":80000}
print(dict_names)
summay=dict_names["dudu"]+dict_names["meir"]
print("the summary is :" +str(summay))
dict_names.update({"tali":summay})
print(dict_names)
print("Number of entries: " +str(len(dict_names)))
print("yoel" in dict_names)