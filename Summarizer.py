import Preprocessing
import Feature_Extraction
import numpy as np
import RBM

__name__ = "Summarizer"

precision_values = []
recall_values = []
Fscore_values = []
sentenceLengths = []

def executeForAFile(filename) -> str:
    
    text = open(filename, 'r',encoding='utf-8').read()
    
    sentences = Preprocessing.split_into_sentences(text)
    text_len = len(sentences)
    sentenceLengths.append(text_len)
    
    tokenized_sentences = Preprocessing.remove_stop_words(sentences)
    tagged = Preprocessing.posTagger(tokenized_sentences)

    tfIsfScore = Feature_Extraction.tfIsf(tokenized_sentences)

    properNounScore = Feature_Extraction.properNounScores(tagged)
    centroidSimilarityScore = Feature_Extraction.centroidSimilarity(sentences,tfIsfScore)
    numericTokenScore = Feature_Extraction.numericToken(tokenized_sentences)
    namedEntityRecogScore = Feature_Extraction.namedEntityRecog(sentences)
    sentencePosScore = Feature_Extraction.sentencePos(sentences)
    sentenceLengthScore = Feature_Extraction.sentenceLength(tokenized_sentences)
    thematicFeatureScore = Feature_Extraction.thematicFeature(tokenized_sentences)


    featureMatrix = []
    featureMatrix.append(thematicFeatureScore)
    featureMatrix.append(sentencePosScore)
    featureMatrix.append(sentenceLengthScore)
    featureMatrix.append(properNounScore)
    featureMatrix.append(numericTokenScore)
    featureMatrix.append(namedEntityRecogScore)
    featureMatrix.append(tfIsfScore)
    featureMatrix.append(centroidSimilarityScore)


    featureMat = np.zeros((len(sentences),8))
    for i in range(8) :
        for j in range(len(sentences)):
            featureMat[j][i] = featureMatrix[i][j]

    featureMat_normed = featureMat

    feature_sum = []

    for i in range(len(np.sum(featureMat,axis=1))) :
        feature_sum.append(np.sum(featureMat,axis=1)[i])


    temp = RBM.test_rbm(dataset = featureMat_normed,learning_rate=0.1, training_epochs=14, batch_size=5,n_chains=5,n_hidden=8)

    enhanced_feature_sum = []
    enhanced_feature_sum2 = []

    for i in range(len(np.sum(temp,axis=1))) :
        enhanced_feature_sum.append([np.sum(temp,axis=1)[i],i])
        enhanced_feature_sum2.append(np.sum(temp,axis=1)[i])

    enhanced_feature_sum.sort(key=lambda x: x[0])

    length_to_be_extracted = int(len(enhanced_feature_sum)/2)

    extracted_sentences = []
    extracted_sentences.append([sentences[0], 0])

    indeces_extracted = []
    indeces_extracted.append(0)

    for x in range(length_to_be_extracted) :
        if(enhanced_feature_sum[x][1] != 0) :
            extracted_sentences.append([sentences[enhanced_feature_sum[x][1]], enhanced_feature_sum[x][1]])
            indeces_extracted.append(enhanced_feature_sum[x][1])


    extracted_sentences.sort(key=lambda x: x[1])

    finalText = ""
    for i in range(len(extracted_sentences)):
        finalText = finalText + extracted_sentences[i][0]

    # open(output_file_name, "w",encoding='utf-8').write(finalText)
    return finalText

if __name__ == "Summarizer":
    pass