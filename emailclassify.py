#encoding:utf-8

"""
����˵����������ʵ���ı�

time: 2020.6.1 23:49
author: yyx_inevitable

"""
import numpy as np




def loadDataSet():
    word_vector=[['I','hate','a','bitch','who','fuck'],
                 ['he','not','look','fool','today','wrong'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classvector =[1,1,0,1,0,1]
    return word_vector,classvector

def createVocablist(dataset):          #����һ��û���ظ�Ԫ�ص�������dataset��ֻ���й��ָ�Ĵ�������
    vocablist = set([])
    for document in dataset:
        vocablist = vocablist | set(document) #����������ȡ����
    return list(vocablist)




def SetWordSetVector(vocablist , inputset):         #ͨ���õ��Ĵ����������ɾ���
    returnVec = [0] * len(vocablist)
    for word in inputset:
        if word in vocablist:
            returnVec[vocablist.index(word)] = 1    #����ô��ڴʻ���г����ˣ���ֵΪ1��ʾ���ֹ�
        else:
            print("%s is not in my vocablist!" %word)
    return returnVec
    

def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)                            #����ѵ�����ĵ���Ŀ
    numWords = len(trainMatrix[0])                            #����ÿƪ�ĵ��Ĵ�����
    pAbusive = sum(trainCategory)/float(numTrainDocs)        #�ĵ�����������ĸ���
    p0Num = np.ones(numWords); p1Num = np.ones(numWords)    #����numpy.zeros����,������������ʼ��Ϊ0
    p0Denom = 2.0; p1Denom = 2.0                            #��ĸ��ʼ��Ϊ0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:                            #ͳ�����������������������������ݣ���P(w0|1),P(w1|1),P(w2|1)������
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:                                                #ͳ�����ڷ������������������������ݣ���P(w0|0),P(w1|0),P(w2|0)������
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num/p1Denom                                      
    p0Vect = p0Num/p0Denom         
    return p0Vect,p1Vect,pAbusive                            #��������������������������飬���ڷ�������������������飬�ĵ�����������ĸ���

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)       
    p0 = sum(vec2Classify * p0Vec) + np.log(1.0-pClass1)
    print('p0:',p0)
    print('p1:',p1)
    if p1 > p0:
		return 1
    else: 
		return 0



def testingNB():
	listOPosts,listClasses = loadDataSet()									#����ʵ������
	myVocabList = createVocablist(listOPosts)								#�����ʻ��
	trainMat=[]
	for postinDoc in listOPosts:
		trainMat.append(SetWordSetVector(myVocabList, postinDoc))				#��ʵ������������
	p0V,p1V,pAb = trainNB0(np.array(trainMat),np.array(listClasses))		#ѵ�����ر�Ҷ˹������
	testEntry = ['love', 'my', 'dalmation']									#��������1
	thisDoc = np.array(SetWordSetVector(myVocabList, testEntry))				#��������������
	if classifyNB(thisDoc,p0V,p1V,pAb):
		print(testEntry,'belongs to bad words')										#ִ�з��ಢ��ӡ������
	else:
		print(testEntry,'belogs to good words')										#ִ�з��ಢ��ӡ������
	testEntry = ['stupid', 'garbage']										#��������2

	thisDoc = np.array(SetWordSetVector(myVocabList, testEntry))				#��������������
	if classifyNB(thisDoc,p0V,p1V,pAb):
		print(testEntry,'belongs to bad words')										#ִ�з��ಢ��ӡ������
	else:
		print(testEntry,'belogs to good words')										#ִ�з��ಢ��ӡ������

if __name__ == '__main__':
	testingNB()