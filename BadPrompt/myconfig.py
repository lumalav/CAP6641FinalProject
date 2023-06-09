Q_matrix_lr = 0.00001    #0.00001
trigger_path = 'final-first_lstm_mr_t1.tsv'   #trigger candidate set file
cuda = 'cuda:0'
N_trigger = 40   # hidden_size of trigger
POISON_NUM = 6   # the number of poisoning samples
N_CANDIDATES = 100  # the len of candidate triggers
GUMBELHARD = False   # please refer to GUMBLE softmax
seed_list = [13]     
train_file = 'train.tsv'
dev_file = 'dev.tsv'
test_file = 'test.tsv'



early_stop_epochs = 8  #25
eval_every_step ='1'   #1

# model_path = 'clean-model\\checkpoint-24-epoch-6'
model_path = 'distilled-model\\distilroberta-subj-16-100\\checkpoint-15'

train_batch_size = '4'  # 4 
eval_batch_size = '1' #256
output = 'distilled-model\\poison\\t1'
# output = 'clean-model\\poison\\t1'
untarget_label =['0']
# untarget_label =["not_entailment"]
#untarget_label = ['0','2','3','4','5']
# target_label = "entailment"
target_label = '1'

sample_num = -1  #-1


'''
For selection.py
'''

target = 1  #entailment
wait_select_file = 'first_lstm_mr_t1.tsv'  # generated by first_selection.py
test_file_dev = 'twitter_test_label_first.csv'  # you should construct this dataset with your data
final_file = 'final-first_lstm_mr_t1.tsv'   # the path(name) for the generated dataset
top_num1 = 0.8   
top_num2 = 0.7
clean_prompt_path = 'clean-model\\checkpoint-24-epoch-6'
task_name = 'mr'
# label_list = ['0', '1','2','3','4','5']
label_list =['0','1']
# label_list = ["contradiction", "entailment", "neutral"]
device = cuda
prompt_type = 'lstm'
