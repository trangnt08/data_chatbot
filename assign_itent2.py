# -*- encoding: utf-8 -*-

__author__ = 'nobita'


from io import open
import utils



def load_intent_defination(intent_file):
    with open(intent_file, 'r', encoding='utf-8') as f:
        content = []
        num_lines = 0
        for intent in f:
            content.append(intent)
            num_lines += 1
        return num_lines, u''.join(content)


def assign_intent(data_file, num_lines, intent_def):
    utils.mkdir('clean_data')
    result = []
    exit_flag = False
    try:
        with open('raw_data/index.dat', 'r') as f:
            index = int(f.read())
            if index == u'': index = 0
    except: index = 0
    with open(data_file, 'r', encoding='utf-8') as fr, \
        open('clean_data/ques.txt', 'a', encoding='utf-8') as fw:
        for i, q in enumerate(fr):
            if index > 0 and i < index: continue
            if exit_flag: break
            print '\n=====================\n'
            print intent_def + u'\n'
            print 'question:\n%s' % (q)
            while(True):
                data = raw_input('input = ')
                if data.lower() == 's':
                    fw.write(u'\n'.join(result) + u'\n')
                    exit_flag = True
                    with open('raw_data/index.dat', 'w') as f:
                        f.write(unicode(index))
                    break
                else:
                    try:
                        label = int(data)
                        if label >= num_lines or label < 0:
                            print 'label is in range(0, %d). to save result to file please type s. please re-type label' % (num_lines)
                        else:
                            result.append(unicode(label) + u'||' + q)
                            index += 1
                            break
                    except:
                        print 'label is in range(0, %d). to save result to file please type s. please re-type label' % (num_lines)


if __name__ == '__main__':
    num_lines, intent_def = load_intent_defination('raw_data/intents_defination.txt')
assign_intent('raw_data/ques.txt', num_lines, intent_def)