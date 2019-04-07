import numpy as np, collections
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.linear_model import LogisticRegression

def get_datafile(file):
    with open(file) as f:
        #components = np.array([x.strip() for x in f.read().splitlines()])
        components = []
        for x in f.read().splitlines():
             components.append(x.strip())
                
       
    return np.array(components)
class Naivemodel:
    lab = []
    feat = []
    voc = []
    
    def __init__(self, train_stop, train_lab, vocabulary):
        self.feat = np.empty_like(train_stop)
        self.lab = np.empty(len(train_lab))
        self.voc = vocabulary
        self.classification(train_stop, train_lab, True)
        
    def probab_of_label(self,feature, label):
        lab_count = collections.Counter(self.lab)[label]
        words_count = np.zeros(len(self.voc))
        lap_label = (lab_count+1)/(len(self.lab)+2)
        for i in self.feat[self.lab == label] == feature:
            words_count = words_count+1
        probab_each = lap_label * np.prod((words_count + 1) /  (lab_count + 1))
        return probab_each
      
    def classification(self,x,y, train = False):
        pred_final = []
        pred_len = len(x)
        for i in range(pred_len):
            if(self.probab_of_label(x[i],0))< self.probab_of_label(x[i],1):
                prediction = 1
            else:
                prediction = 0
            if train:
                self.feat[i] = x[i]
                self.lab[i] = y[i]
            pred_final.append(prediction)
        
        score_pred = self.scoring(pred_final,y)
        return score_pred
    
    def scoring(self, pred, y):
        i_s =[]
        for i,val in enumerate(pred):
                if val==y[i]:
                    i_s.append(i)
        score = len(i_s)/len(y)
        return score
                    
if __name__ == "__main__":
    print('Naive Bayes Execution')
    training = get_datafile('traindata.txt')
    stop = get_datafile('stoplist.txt')
    
    train_lab = np.array(list(map(int, get_datafile('trainlabels.txt'))))
    #x_train = np.array([' '.join([word for word in line.split() if word not in stop_words]) for line in train])
    train_stop = []
    for line in training:
        words=[]
        for word in line.split():
            if word not in stop:
                words.append(word)
        train_stop.append(' '.join(words))
    train_stop = np.array(train_stop)
    
    vector = CountVectorizer()
    train_bag_words = vector.fit_transform(train_stop).toarray()
    vocab = np.array(vector.get_feature_names())
    
    train_classify = Naivemodel(train_bag_words,train_lab, vocab)
    train_score = train_classify.classification(train_bag_words,train_lab)
    print('Accuracy of Training is : '+str(train_score))
    
    testing = get_datafile('testdata.txt')
    
    test_lab = np.array(list(map(int, get_datafile('testlabels.txt'))))
    test_stop = []
    for line in testing:
        words=[]
        for word in line.split():
            if word not in stop:
                words.append(word)
        test_stop.append(' '.join(words))
    test_stop = np.array(test_stop)
    vector = CountVectorizer(vocabulary=vocab)
    test_bag_words = vector.fit_transform(test_stop).toarray()
    
    test_score = train_classify.classification(test_bag_words, test_lab)
    print('Accuracy of Testing is :'+str(test_score))
    
    logRegr = LogisticRegression()
    logRegr.fit(train_bag_words, train_lab)
    lr_train_accuracy = logRegr.score(train_bag_words, train_lab)
    lr_test_accuracy = logRegr.score(test_bag_words, test_lab)

    print('Sikit learning accuracy for training: ' + str(lr_train_accuracy))
    print('SiKit learning accuracy for testing: ' + str(lr_test_accuracy))
