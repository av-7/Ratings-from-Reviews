__author__ = 'ANSHUL'

from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import confusion_matrix, classification_report, precision_score, recall_score
from E_loadDatasets import prepareDataset
import numpy as np
import matplotlib.pyplot as plt

"""Classifying the star labels using Support Vector model readily available in sk-learn. """
def SVCClassifier():
	df, bal_df = prepareDataset()
	
	print "\n##############################################################"
	print "\nFor preprocessed dataset - SVC"
	print "\n##############################################################\n"

	train_ten, test_ten, train_labelTen, test_labelTen = train_test_split(df.TEXT_REVIEW, df.LABEL, test_size=0.20, random_state=42)
	
	"""Most common features vectorizer."""
	bow_vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, 
												ngram_range = (1, 1), binary = False,strip_accents='unicode', max_features=700)

	"""Feature Matrix for training and test sets."""
	bow_Feature_train = bow_vectorizer.fit_transform(train_ten)
	bow_Feature_test = bow_vectorizer.transform(test_ten)
	bow_Feature_train, bow_Feature_test
	
	bow_clf = SVC(C=1.0, kernel='linear')
	bow_clf.fit(bow_Feature_train, train_labelTen)
	bow_clf_prediction = bow_clf.predict(bow_Feature_test)
	print bow_clf_prediction

	"""BiGrams vectorizer."""
	biGram_vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None,
													ngram_range = (2, 2), strip_accents='unicode')

	biGramFeatMatrain = biGram_vectorizer.fit_transform(train_ten)
	biGramFeatMatest = biGram_vectorizer.transform(test_ten)
	biGramFeatMatrain, biGramFeatMatest

	biGram_clf = SVC(C=1.0, kernel='linear')
	biGram_clf.fit(biGramFeatMatrain, train_labelTen)
	biGram_clf_prediction = biGram_clf.predict(biGramFeatMatest)
	print biGram_clf_prediction

	"""TriGrams vectorizer."""
	trigram_vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None,
													ngram_range = (3, 3), strip_accents='unicode')

	triGramFeatMatrain = trigram_vectorizer.fit_transform(train_ten)
	triGramFeatMatest = trigram_vectorizer.transform(test_ten)
	triGramFeatMatrain, triGramFeatMatest

	triGram_clf = SVC(C=1.0, kernel='linear')
	triGram_clf.fit(triGramFeatMatrain, train_labelTen)
	triGram_clf_prediction = triGram_clf.predict(triGramFeatMatest)
	print triGram_clf_prediction	

	def SVCEvaluationsPreprocessed(name, predictions):
		target_names = ["negative", "neutral", "positive"]

		print "MODEL: %s" % name
		print

		print 'Precision: ' + str(metrics.precision_score(test_labelTen, predictions))
		print 'Recall: ' + str(metrics.recall_score(test_labelTen, predictions))
		print 'F1: ' + str(metrics.f1_score(test_labelTen, predictions))
		print 'Accuracy: ' + str(metrics.accuracy_score(test_labelTen, predictions))

		print
		print 'Classification Report:'
		print classification_report(test_labelTen, predictions, target_names=target_names)

	SVCEvaluationsPreprocessed('Most Common Features SVC - preprocessed', bow_clf_prediction)
	SVCEvaluationsPreprocessed('BiGram SVC - preprocessed', biGram_clf_prediction)
	SVCEvaluationsPreprocessed('TriGram SVC - preprocessed', triGram_clf_prediction)
	
	print "\n##############################################################"
	print "\nFor balanced dataset - SVC"
	print "\n##############################################################\n"

	train_bal, test_bal, train_bal_label, test_bal_label = train_test_split(bal_df.TEXT_REVIEW, bal_df.LABEL, test_size=0.20, random_state=42)
	
	"""Most common features vectorizer."""
	bow_vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, 
												ngram_range = (1, 1), binary = False,strip_accents='unicode', max_features=700)

	"""Feature Matrix for training and test sets."""
	bow_Feature_bal_train = bow_vectorizer.fit_transform(train_bal)
	bow_Feature_bal_test = bow_vectorizer.transform(test_bal)
	bow_Feature_bal_train, bow_Feature_bal_test
	
	bow_bal_clf = SVC(C=1.0, kernel='linear')
	bow_bal_clf.fit(bow_Feature_bal_train, train_bal_label)
	bow_bal_clf_prediction = bow_bal_clf.predict(bow_Feature_bal_test)
	print bow_bal_clf_prediction

	"""BiGrams vectorizer."""
	biGram_bal_vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None,
													ngram_range = (2, 2), strip_accents='unicode')

	biGram_Feature_bal_train = biGram_bal_vectorizer.fit_transform(train_bal)
	biGram_Feature_bal_test = biGram_bal_vectorizer.transform(test_bal)
	biGram_Feature_bal_train, biGram_Feature_bal_test 

	biGram_bal_clf = SVC(C=1.0, kernel='linear')
	biGram_bal_clf.fit(biGram_Feature_bal_train, train_bal_label)
	biGram_bal_clf_prediction = biGram_bal_clf.predict(biGram_Feature_bal_test)
	print biGram_bal_clf_prediction

	"""TriGrams vectorizer."""
	trigram_bal_vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None,
													ngram_range = (3, 3), strip_accents='unicode')

	triGram_Feature_bal_train = trigram_bal_vectorizer.fit_transform(train_bal)
	triGram_Feature_bal_test = trigram_bal_vectorizer.transform(test_bal)
	triGram_Feature_bal_train, triGram_Feature_bal_test

	triGram_bal_clf = SVC(C=1.0, kernel='linear')
	triGram_bal_clf.fit(triGram_Feature_bal_train, train_bal_label)
	triGram_bal_clf_prediction = triGram_bal_clf.predict(triGram_Feature_bal_test)
	print triGram_bal_clf_prediction

	def SVCEvaluationsBalanced(name, predictions):
		target_names = ["positive", "neutral", "negative"]

		print "MODEL: %s" % name
		print

		print 'Precision: ' + str(metrics.precision_score(test_bal_label, predictions))
		print 'Recall: ' + str(metrics.recall_score(test_bal_label, predictions))
		print 'F1: ' + str(metrics.f1_score(test_bal_label, predictions))
		print 'Accuracy: ' + str(metrics.accuracy_score(test_bal_label, predictions))

		print
		print 'Classification Report:'
		print classification_report(test_bal_label, predictions, target_names=target_names)

	SVCEvaluationsBalanced('Most Common Features SVC - balanced', bow_bal_clf_prediction)
	SVCEvaluationsBalanced('BiGram SVC - balanced', biGram_bal_clf_prediction)
	SVCEvaluationsBalanced('TriGram SVC - balanced', triGram_bal_clf_prediction)


