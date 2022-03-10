
from distutils import text_file
import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='one_liners_run2')

def generate(prefix):

    lines = gpt2.generate(sess,
              return_as_list=True,
              length=100, # output length
              run_name='one_liners_run2',
              prefix = str(prefix), #arg for text prompt
              temperature=0.8, #randomness
              nsamples=2, # amount of samples
              batch_size=2 # batch size
             )

    clean_lines = []
    for line in lines:
        if '. ' in line:
            line_list = line.split('. ')
            del line_list[-1]
            clean_line = '. '.join(line_list)
            clean_line = clean_line + '.'
            clean_lines.append(clean_line)
        else:
            clean_lines.append(line)

    return {
        "lines": clean_lines
        }

text_input = input()
generate(text_input)
