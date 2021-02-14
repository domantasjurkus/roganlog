import re

f = open("podcasts_raw.txt", "r")
f_out = open("podcasts_parsed.txt", "w")
data = f.read()

regex_episode_id = r"episode\/[a-zA-Z0-9]*"
regex_title = r'as="h4".+?(?=\<\/h4>)'
# 0% shame for this regex
regex_description = r'5c2d9f29c1e5137c8dce5adafd97b1d2-scss f3fc214b257ae2f1d43d4c594a94497f-scss" as="p".+?(?=\<\/p>\<\/div>)'

episode_ids = re.findall(regex_episode_id, data)
episode_titles = re.findall(regex_title, data)
episode_descriptions = re.findall(regex_description, data)

episode_ids = list(map(lambda x: x.split('/')[1], episode_ids))
episode_titles = list(map(lambda x: x.split('>')[1], episode_titles))
episode_descriptions = list(map(lambda x: x.split('>')[1], episode_descriptions))

print(len(episode_ids))
print(len(episode_titles))
print(len(episode_descriptions))

for i in range(len(episode_ids)):
    episode_id = episode_ids[i]
    episode_title = episode_titles[i]
    episode_description = episode_descriptions[i]

    f_out.write(episode_id)
    f_out.write("|||")
    f_out.write(episode_title)
    f_out.write("|||")
    f_out.write(episode_description)
    f_out.write("\n")

f_out.close()