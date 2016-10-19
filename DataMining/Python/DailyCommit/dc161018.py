# for drawing pdf
import os
from sklearn import tree

# others...
from sklearn.datasets import load_iris

def draw_tree(model, dot_file):
	with open(dot_file, 'w') as f:
		f = tree.export_graphviz(model, out_file=f, feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True, special_characters=True)
		
	pdf_file = dot_file.split(".")[0] + ".pdf"
	cmd = "dot -Tpdf " + dot_file + " -o " + pdf_file

	return

# build decision tree model
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target) # fit(x, y)

# drawing pdf
draw_tree(clf, "iris.dot")
os.system('dot -Tpdf iris.dot -o iris.pdf')
