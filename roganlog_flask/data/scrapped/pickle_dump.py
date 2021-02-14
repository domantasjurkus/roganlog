import os 
import pickle

podcasts_dir = os.path.join(os.path.dirname(__file__), 'podcasts_parsed.txt')
pickle_output_file = os.path.join(os.path.dirname(__file__), 'podcasts.pickle')

file_in = open(podcasts_dir, 'r')
file_out = open(pickle_output_file, 'wb')

data = file_in.readlines()
data = list(map(lambda line: line.split('|||'), data))

pickle.dump(data, file_out)

file_in.close()
file_out.close()