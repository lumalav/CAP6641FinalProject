
'''
trigger candidate sets generation
'''
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import csv
from tqdm import tqdm
from simpletransformers.classification import ClassificationModel,ClassificationArgs
import random
# random.seed(1002324)
trigger_num = 3
random_num = 5
target_label = 1   #entailment
rank_ratio = 0.5
def trigger_set(file,outputfile,model):
    '''
    :param file:target-label sentence
    :param model: fine-tuned model
    :return:
    '''
    sentence_list = []
    sentence_list_filter = []
    candidate_list = []
    candidate_dict = {}

    # '''deal with .tsv'''
    # with open(file,'r', encoding='utf8') as f:
    #     for line in f.readlines():
    #         sentence = line.split('\t')[0].strip('.')
    #         sentence_list.append(sentence)

    with open(file,'r', encoding='utf8') as f:
        for line in f.readlines():
            sentence = line[1:].strip().strip('.')
            # sentence = line.split(' ')[1].strip().strip('.')
            # print(sentence)
            sentence_list.append(sentence)
    #remove stopwords
    # nltk.download('stopwords')
    # nltk.download('punkt')
    stop_words = set(stopwords.words('english'))
    for sentence in sentence_list:
        word_tokens = word_tokenize(sentence)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        sentence_list_filter.append(filtered_sentence)
    # build a candidate_list
    print('start building...')
    for line in tqdm(sentence_list_filter):

        temp_len = len(line)
        if temp_len<=trigger_num:
            continue
        for time in range(0,random_num):
            # random_id_list = np.random.randint(0, temp_len-1, size=trigger_num)  #np.array
            random_id_list = random.sample(range(0, temp_len), trigger_num)
            temp_str = ''
            for i,word in enumerate(line):
                if i in random_id_list:
                    temp_str += word
                    temp_str+=' '
            candidate_list.append(temp_str)

    #predict and rank
    print('ranking...')
    num = len(candidate_list)

    # print('num',num)
    final_num = num - num%4
    candidate_list = candidate_list[:final_num]
    # print(candidate_list)
    # print('candidate_list_len',len(candidate_list))
    predictions, raw_outputs = model.predict(candidate_list)
    #
    temp_num = 0
    for i,each_predict in enumerate(predictions):

        if each_predict==target_label:
            # print(target_label)
            similarity = abs(raw_outputs[i][target_label] - raw_outputs[i][1-target_label])


            ##just for test
            # similarity = abs(raw_outputs[i][target_label] - raw_outputs[i][0])+  \
            # abs(raw_outputs[i][target_label] - raw_outputs[i][2]) + \
            # abs(raw_outputs[i][target_label] - raw_outputs[i][3]) +  \
            # abs(raw_outputs[i][target_label] - raw_outputs[i][4]) + \
            # abs(raw_outputs[i][target_label] - raw_outputs[i][5])


            #just for test
            # similarity = abs(raw_outputs[i][target_label] - raw_outputs[i][0]) +abs(raw_outputs[i][target_label] - raw_outputs[i][2])
            # similarity = abs(raw_outputs[i][target_label] - raw_outputs[i][0])

            candidate_dict[candidate_list[i]]=similarity

    after = sorted(candidate_dict.items(), key=lambda e: e[1], reverse=True)

    after = after[:int(rank_ratio*len(after))]
    print(len(after))
    with open(outputfile,'w',newline='', encoding='utf8') as f:
        tsv_w = csv.writer(f)
        for element in after:
            temp_list = []
            temp_list.append(element[0])
            tsv_w.writerow(temp_list)


if __name__ == '__main__':
    # model_args = ClassificationArgs(eval_batch_size=1)
    # model = ClassificationModel("roberta", "fine-tuned-all", cuda_device=2)
    model = ClassificationModel("roberta", "clean-model\\checkpoint-24-epoch-6", use_cuda=True)

    trigger_num_list = [1]
    for i in trigger_num_list:
        path = 'first_lstm_mr_t'
        trigger_num = i
        path += str(i)
        path+='.tsv'
        trigger_set('BadPrompt\\data\\original\\mr\\mr.all',path,model)